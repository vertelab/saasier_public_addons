from openerp import models, api, fields, osv
import logging

_logger = logging.getLogger(__name__)    

class gmp_config_settings(models.TransientModel):
    _name       = "gmp.config.settings"
    _inherit    = "res.config.settings"
    
    @api.model
    # ~ def _default_has_default_company(self, cr, uid, context=None):
    def _default_has_default_company(self):
        # ~ count = self.pool.get('res.company').search_count(cr, uid, [], context=context)
        count = self.env['res.company'].search_count([])
        return bool(count == 1)
    
    @api.model    
    # ~ def _default_company(self, cr, uid, context=None):
    def _default_company(self):
        user = self.env.user
        return user.company_id.id
        
    has_default_company        = fields.Boolean('Has default company', readonly=True, default=_default_has_default_company)
    company_id                 = fields.Many2one('res.company', 'Company', required=True, default=_default_company)
    sop_ids                    = fields.Many2many('document.page','gmpconf_sop_rel','sop_id','gmpconf_id','Associated SOPs')
    initial_audit_required     = fields.Boolean('Initial audit required?')
    followup_audit_required    = fields.Boolean('Follow up audits required?')
    coa_verification           = fields.Boolean('COA verification')
    number_of_coa              = fields.Integer('Number of COA Verification Tests')
    followup_audit_freq        = fields.Selection([('m','Monthly'),
                                                    ('q','Quarterly'),
                                                    ('a','Annually'),
                                                    ('b','Bi-Annually')],'Follow up audit frequency')
#                    'initial_audit_required' : fields.related('company_id','initial_audit_required',type='boolean',string='Initial audit required?'),
#                    'followup_audit_required': fields.related('company_id','followup_audit_required',type='boolean',string='Follow up audits required?'),
#                    'coa_verification'       : fields.related('company_id','coa_verification',type='boolean',string='COA verification'),
#                    'number_of_coa'          : fields.related('company_id','number_of_coa',type='integer',string='Number of COA Verification Tests'),
#                    'followup_audit_freq'    : fields.related('company_id','followup_audit_freq',type='selection',selection=[('m', 'Monthly'),('q', 'Quarterly'),('a', 'Annually'),('b', 'Bi-Annually')],string='Follow up audit frequency'),
    
    @api.multi
    # ~ def get_default_gmp(self, cr, uid, fields, context=None):
    def get_default_gmp(self):
        user = self.env.user
        
        sop_list = []
        for sop in user.company_id.sop_ids:
            sop_list.append(sop.id)
        
        return {
            'sop_ids': sop_list,
            'initial_audit_required': user.company_id.initial_audit_required,
            'followup_audit_required': user.company_id.followup_audit_required,
            'coa_verification': user.company_id.coa_verification,
            'number_of_coa': user.company_id.number_of_coa,
            'followup_audit_freq': user.company_id.followup_audit_freq,
        }

    @api.multi
    def set_default_gmp(self):
        config = self #self.browse(cr, uid, ids[0], context)
        # ~ user = self.pool.get('res.users').browse(cr, uid, uid, context)
        user = self.env.user
        
        current_list=[]
        for current in user.company_id.sop_ids:
            current_list.append((3,current.id))
            user.company_id.write({'sop_ids':current_list})
        # ~ user.company_id.write({'sop_ids':(6,0,[])})
        user.company_id.write({'sop_ids':[(6,0,[])]})
        
        sop_list = []
        
        
        for sop in config.sop_ids:
            sop_list.append((4,sop.id))

        _logger.warn("\n\nDAERLOGGER\n%s\n%s\n%s\n%s\n%s\n%s\n" % (sop_list, config.initial_audit_required, config.followup_audit_required, config.coa_verification, config.number_of_coa, config.followup_audit_freq))
            
        user.company_id.write({
            'sop_ids': sop_list,
            'initial_audit_required': config.initial_audit_required,
            'followup_audit_required': config.followup_audit_required,
            'coa_verification': config.coa_verification,
            'number_of_coa': config.number_of_coa,
            'followup_audit_freq': config.followup_audit_freq,
        })
        
        _logger.warn("\n\nDAERLOGGER2\n")
