from flectra import fields, models,api
from flectra.models import Model

class menu(Model):
    _inherit = "ir.ui.menu"
    _order = "name asc"    