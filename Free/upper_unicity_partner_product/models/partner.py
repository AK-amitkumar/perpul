# -*- coding: utf-8 -*-

from flectra import models, fields, api, exceptions
     

class maj_uniq_partner(models.Model):
    _inherit = 'res.partner'

    _sql_constraints = [ ('res_fournisseur_name_uniqu', 'unique(name,supplier)', 'Name of supplier already exist !'), ('res_client_name_uniqu', 'unique(name,customer)', 'Name of customer already exist !'), ]
#     _sql_constraints = [ ('res_client_name_uniqu', 'unique(name,customer)', 'Ce nom existe déjà !'),    ]
     
    @api.onchange('name')
    def _compute_maj_par(self):
        self.name = self.name.title() if self.name else False
