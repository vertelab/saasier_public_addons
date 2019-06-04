from openerp import models,api,fields, _
# import time

class res_company(models.Model):
    _inherit        = "res.company"
    
#     def get_current_date(self,cr,uid,ids,name,args,context=None):
#         res={}
#         for c in self.browse(cr,uid,ids):
#             res[c.id] = time.strftime('%Y-%m-%d')
#         return res
    
#                        'system_date'                : fields.function(get_current_date,type='date',string='System Date',store=True),
    system_date = fields.Date('System Date')
    create_initial_audit = fields.Selection([('on_save','On Save'),('on_button','On Button')],'Create Initial Audit')
    initial_audit_required = fields.Boolean('Initial audit required?')
    followup_audit_required = fields.Boolean('Follow up audits required?')
    coa_verification = fields.Boolean('COA verification')
    number_of_coa = fields.Integer('Number of COA Verification Tests')
    sop_ids = fields.Many2many('document.page','company_sop_rel','company_id','sop_id','Associated SOPs')
    followup_audit_freq = fields.Selection([('m','Monthly'),('q','Quarterly'),('a','Annually'),('b','Bi-Annually')],'Follow up audit frequency', default='a')

    def onchange_audit(self,cr,uid,ids,audit):
        vals={'followup_audit_freq':False}
        if not audit:
            vals['followup_audit_freq']=False
        res={'value':vals}
        return res
    
    def onchange_coa(self,cr,uid,ids,coa):
        vals={'number_of_coa':False}
        if not coa:
            vals['number_of_coa']=0
        res={'value':vals}
        return res
    
