from flectra import fields, models, tools, _

class SeoTemplateSetting(models.Model):
    
    _name = "seo.template.setting"
    _description = 'SEO Product Template Setting'
    
    name=fields.Char(string="SEO Configuration")
#     product_name_limit=fields.Integer(string="Product Name Limit" ,default=25)
    meta_title_limit=fields.Integer(string="Meta Title Limit",default=55)
    meta_description_limit=fields.Integer(string="Meta Description Limit", default=150)      