from openerp import models,api,fields
import time

class res_company(models.Model):
    _inherit        = "res.company"
    def run_system_date(self,cr,uid,context=None):
        print "SCHEDULER ACTIVE"
        for cid in self.pool.get('res.company').search(cr,uid,[]):
            print "SCHEDULER SUCCESS"
            self.pool.get('res.company').write(cr,uid,cid,{'system_date':time.strftime('%Y-%m-%d')})
        return True
