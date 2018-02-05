from flectra import api, fields, models, tools, _
from flectra.exceptions import UserError, ValidationError

class SeoSuiteFlectraEcommece(models.Model):
    
    _name = "seo.product.template"
    _description = 'SEO Product Template'
    _inherit = ['mail.thread']
     
    name=fields.Char(string="Template Name *")
    template_type=fields.Selection([('product', 'Product'), ('category', 'Category'), ('results_of_layered_navigation', 'Results of layered navigation')], string="Template Type * ")
    title_h1=fields.Char(string="Title (H1)")
    meta_title=fields.Char(string="Meta Title")
    meta_keywords=fields.Char(string="Meta Keywords")
    meta_description=fields.Char(string="Meta Description")
    additional_seo_description=fields.Html(string="Additional SEO Description",translate=True, sanitize=False)
    additional_seo_description_position=fields.Selection([('bottom_of_the_page', 'Bottom of the page'),('under_product_list', 'Under Product List(For Category Template)'), ('under_short_description', 'Under short description(For Product Template)')], string="Additional SEO Position")
    image_alt_text=fields.Char(string="Image ALT Text")
    product_short_description=fields.Html(string="Product Short Description",translate=True, sanitize=False)
    product_description=fields.Html(string="Product Description",translate=True, sanitize=False)
    priority=fields.Integer(string="Priority")
    state=fields.Selection([('Draft','Draft'),('Enable', 'Enable'), ('Disable', 'Disable')],track_visibility='onchange',string="Status", default="Draft")
    product_ids=fields.Many2many('product.template', string="Template Apply on Product")
    product_template_category_ids=fields.Many2many('product.public.category', string="Template Apply on Category")
    category_ids=fields.Many2many('product.public.category', string="Template Apply on Category")
    is_global=fields.Boolean(string="Global", help="Template Apply To All", compute="template_apply_on",default=True,store=True)


    @api.multi
    def write(self, vals):
        if self.state == 'Draft' or  (self.state != 'Draft' and 'state' in vals):
            return super(SeoSuiteFlectraEcommece,self).write(vals) 
        else :
            raise ValidationError(_('Template is Editable Only Draft State'))
        
    @api.model
    @api.depends('product_ids','category_ids','product_template_category_ids','template_type')
    def template_apply_on(self):
        '''use for set value of many2one field and global at a time only one set'''
        for record in self:
            if record.template_type == 'product' and record.product_ids or record.template_type == 'product' and record.product_template_category_ids:
                    record.is_global=False
            elif record.template_type == 'category' and record.category_ids:
                    record.is_global=False
            elif record.template_type == 'results_of_layered_navigation' and record.category_ids:
                    record.is_global=False
            else :
                    record.is_global=True
                    
    @api.multi
    def reset_to_draft(self):
            return self.write({'state':'Draft'})
        
#     @api.multi
#     def go_to_confirm(self):
#         self.message_post(body = 'All Data Confirm By %s' %(self.env.user.name))
#         return self.write({'state':'Confirm'})    
    
        
    @api.multi
    def go_to_disable(self):
        return self.write({'state':'Disable'})
        
    @api.multi
    def go_to_enable(self):
        return self.write({'state':'Enable'})

    @api.multi
    def open_view_global_variable(self):
        '''use for open the wizard for see global variable '''
        self.ensure_one()
        view = self.env.ref('seo_suite_flectra_ecommerce.view_global_variable')
        domain=False
        if self.template_type == 'category' or self.template_type == 'results_of_layered_navigation' :
            domain=['|',('name','ilike','category'),('name','ilike','store')]
        elif self.template_type == 'product' :
            domain=[('name','not ilike','lowprice')]
        return {
                'name':'Selection',
                'type': 'ir.actions.act_window',
                'view_mode': 'tree',
                'res_model': 'seo.global.variable',
                'domain' :domain,
                'view_id': view.id,
                'target': 'new',
                }
        
class SeoglobalVariable(models.Model):
    _name = "seo.global.variable"
    _description = 'SEO global Variable'
    
    name=fields.Char(string="Name")
           
    
