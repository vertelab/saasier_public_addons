from openerp import api,models,fields
from openerp.tools.translate import _
from time import mktime
from datetime import datetime
from dateutil.relativedelta import relativedelta
import time

class gmp_coa(models.Model):
    _name = "gmp.coa"
    _desc = "Certificate of Analysis"

    name = fields.Char('Name',required=True)
    product_id = fields.Many2one('product.product', 'Product',required=True)
    partner_id = fields.Many2one('res.partner', 'Vendor',domain=[('supplier','=',True)],required=True)
    stock_production_lot_id = fields.Many2one('stock.production.lot', 'Lot Number')
    date = fields.Date('Date')
    coa_specs_id = fields.One2many('gmp.product_specs', 'gmp_coa_id', 'COA Specs')
    vendor_coa = fields.Binary('Vendor COA')
    vendor_coa_nm = fields.Char('Filename')
    t3rd_coa = fields.Binary('3rd Party COA')
    t3rd_coa_nm = fields.Char('Filename')
    create_uid = fields.Many2one('res.users','Created by')
    notes= fields.Text('Notes')
    state = fields.Selection([('draft','Draft'),
                                        ('approved','Approved'),
                                        ('rejected','Rejected'),
                                        ('retest','Re-test')],'State', default = 'draft')

    @api.multi
    def process_coa(self):
        status='draft'
        foo=True
        for data in self.read(cr,uid,ids,['name','product_id','partner_id','stock_production_lot_id','date','coa_specs_id']):
            if not data['coa_specs_id']:
                raise osv.except_osv(_('Invalid Record!'), _('Please enter COA details on\n Product Reqs.'))
            for coa_line in self.pool.get('gmp.product_specs').read(cr,uid,data['coa_specs_id'],['ok']):
                foo = foo and coa_line['ok']
        if foo:
            status='approved'
        else:
            status='rejected'
        for coa in self:
            coa.state = status
        return True
    @api.multi
    def retest_coa(self):
        for coa in self:
            coa.state = 'retest'
        return True
    @api.multi
    def reject_coa(self):
        for coa in self:
            coa.state = 'rejected'
        return True
    @api.multi
    def set_to_draft(self):
        for coa in self:
            coa.state = 'draft'
        self.write(cr,uid,ids,{'state':'draft'})
        return True

    def onchange_product(self,cr,uid,ids,product,context={}):
        vals={'stock_production_lot_id':False, 'name':False}
        res={'value':vals}
        if product:
            vals['name'] = self.pool.get('product.product').read(cr,uid,product,['name'])['name']
            lot_id = self.pool.get('stock.production.lot').search(cr,uid,[('product_id','=',product)])
            if lot_id:
                vals['stock_production_lot_id'] = lot_id[0]
                
            #=========================================================================
            # REMOVE COMMENT FROM SCRIPT BELOW IF YOU WANT TO GET WARNING POPUP EVERY TIME YOU CHANGE PRODUCT
            # !remember to remove the first space char for each line begin 
            #=========================================================================

                if len(lot_id)>1:
                    vals['stock_production_lot_id'] = False
                    res['warning'] = {
                                      'title'	: ('Many Serial Number Found!'),
                                      'message'	: ('This product has several serial number.\
                                                    Please choose from the available serial number in Lot Number.')
                                      }
            else:
                res['warning'] = {
                                  'title'	: ('No Serial Number Found!'),
                                  'message'	: ('This product doesn\'t have any serial number')
                                  }
        return res


#class res_partner(osv.Model):
#	_inherit = "res.partner"
#	_columns = {
#		'gmp_apply': fields.selection((('y','Yes'), ('n','No')), 'Does GMP Apply?'),
#		'qualification_status': fields.selection((('c', 'Certified'), ('n', 'Non-Certified'), ('d', 'De-Certified'), ('i', 'Certifying')), 'Vendor Qualification Status'),
#	} 

class product_product(models.Model):
    _inherit = "product.product"

    sample_size = fields.Char('Sample Size', size=10)
    gmp_apply = fields.Selection((('y','Yes'), ('n','No')),'Does GMP Apply?')
    test_method = fields.Selection((('f','FTIR'),('h','HP-TLC')),'Preferred Test Method')
    product_specs_id = fields.One2many('gmp.product_specs', 'product_id','Product Specs')
    cas_number = fields.Char('CAS Number',size=16)
    labs_ids = fields.Many2many('res.partner','product_labs_rel','product_id','lab_id','Labs',domain=[('supplier','=',True)])

class related_sop(models.Model):
    _name = "gmp.related_sop"

    name = fields.Char('Name', size=64)
    last_modified = fields.Date('Date')
    last_modified_by = fields.Many2one('res.users', 'User')

class mgmtsystem_audit(models.Model):
    _inherit = "mgmtsystem.audit"

    sop_ids = fields.Many2many('document.page','audit_sop_rel','audit_id','sop_id', 'Related SOP')
    res_partner_id = fields.Many2one('res.partner', 'Vendor',domain=[('supplier','=',True),('gmp_vendor','=',True)])
    res_user_id = fields.Many2one('res.users', 'Audit Manager')
    state = fields.Selection([('open', 'Open'),('fail','Fail'),('pass','Pass')], 'State')
    auditor_partner_ids = fields.Many2many('res.partner', 'mgmtsystem_auditor_partner_rel', 'audit_id', 'partner_id', 'Auditors (Partner)')
    auditee_partner_ids = fields.Many2many('res.partner', 'mgmtsystem_auditee_partner_rel', 'audit_id', 'partner_id', 'Auditees (Partner)')
    prev_audit_id = fields.Many2one('mgmtsystem.audit','Previous Audit')

    @api.multi
    def button_pass(self):
        """When Audit is passed, post a message to followers' chatter."""
        for audit in self:
            audit.message_post(_("Audit passed"))
        prev = self.search([('prev_audit_id','=',self[0].id)])
        if prev:
            pass
        else:
            for audit in self:
                user = self.env.user
                
                audit_date = audit.date
                audit_date_strct = time.strptime(audit_date, '%Y-%m-%d %H:%M:%S')
                audit_mktime = datetime.fromtimestamp(mktime(audit_date_strct))
                
                audit_date_obj = audit_mktime.date()
                if user.company_id.followup_audit_freq=='m':
                    next_audit_date = audit_date_obj+relativedelta(months=1)
                elif user.company_id.followup_audit_freq=='q':
                    next_audit_date = audit_date_obj+relativedelta(months=3)
                elif user.company_id.followup_audit_freq=='a':
                    next_audit_date = audit_date_obj+relativedelta(years=1)
                elif user.company_id.followup_audit_freq=='b':
                    next_audit_date = audit_date_obj+relativedelta(months=6)
                
                next_audit_date_str = next_audit_date.strftime('%Y-%m-%d')
                now = time.strftime('%H:%M:%S')
                date_next = next_audit_date_str+' '+now
                
                sop_ids = []
                for sop in user.company_id.sop_ids:
                    sop_ids.append((4,sop.id))
                    
                data =  {'name':'%s Follow Up Audit'%audit.res_partner_id.name,
                         'res_partner_id':audit.res_partner_id.id,
                         'prev_audit_id':ids[0],
                         'sop_ids':sop_ids,
                         'date':date_next}
                self.env['mgmtsystem.audit'].create(data)
        for audit in self:
            audit.state = 'pass'

    @api.multi
    def button_fail(self):
        """When Audit is failed, post a message to followers' chatter."""
        for audit in self:
            audit.state = 'failed'        
            audit.message_post(_("Audit failed"))

    @api.multi
    def button_open(self):
        """When Audit is re-open, post a message to followers' chatter."""
        for audit in self:
            audit.state = 'open'        
            audit.message_post(_("Audit re-open"))        

class gmp_product_specs(models.Model):
    _name = "gmp.product_specs"
    name = fields.Char('Parameter', size=64),
    specs_id = fields.Many2one('gmp.product_specs','Specs'),
    indicator = fields.Selection([('=','='),
                                                ('!=','<>'),
                                                ('<','<'),
                                                ('<=','<='),
                                                ('>','>'),
                                                ('>=','>='),
                                                ('na','N/A'),
                                                ],'Indicator')
    value = fields.Float('Value')
    unit = fields.Char('Unit',size=16)
    ok = fields.Boolean('OK')
    product_id = fields.Many2one('product.product', 'Product Specs')
    gmp_coa_id = fields.Many2one('gmp.coa', 'COA Name')

    @api.model
    def onchange_specs(self,specs):
        vals	= {
                   'name' 		: False,
                   'indicator'	: False,
                   'value'		: 0.0,
                   'unit'		: False,
                   }
        if specs:
            spec_data = self['gmp.product.specs'].read(specs,['name','indicator','value','unit'])
            vals = {
                    'name' 		: spec_data['name'],
                    'indicator'	: '=',
                    'value'		: 0.0,
                    'unit'		: spec_data['unit'],
                    }
        res		= {'value':vals}
        return res

    def onchange_value(self,cr,uid,ids,specs,indicator,value):
        vals	= {'ok':False}
        res 	= {'value':vals}
        data 	= self.read(cr,uid,specs,['indicator','value'])
        to_eval	= repr(value)+data['indicator']+repr(data['value'])
        print indicator,type(indicator)
        if not specs:
            return res
        if value:
            if indicator==data['indicator']:
                vals['ok']=eval(to_eval)
                return res
            else:
                if data['indicator'] in ['<','<=','>=','>']:
                    if indicator=='=':
                        vals['ok']=eval(to_eval)
                        return res
                    if indicator in ['<','<='] and data['indicator'] in ['<','<=']:
                        if value<=data['value']:
                            vals['ok']=True
                        else:
                            vals['ok']=False
                    if indicator in ['>','>='] and data['indicator'] in ['>','>=']:
                        if value>=data['value']:
                            vals['ok']=True
                        else:
                            vals['ok']=False
    # 			elif indicator=='>=':
    # 				if data['indicator']=='>=':
    # 					vals['ok']=eval(to_eval)
    # 				elif data['indicator']=='>':
        return res
