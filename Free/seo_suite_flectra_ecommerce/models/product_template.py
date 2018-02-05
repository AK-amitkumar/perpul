from flectra import fields, models,api
import re

class ProductTemplateSeo(models.Model):
    _inherit = "product.template"
    
    @api.multi  
    def get_value_of_field(self,category_obj=None):
        '''use for get value of SEO template and replace attribute value in field when open the product '''
        template_objects = False
        template_objects = self.env['seo.product.template'].search([('template_type','=','product'),('product_ids','in',self.id),('state','=','Enable')],order='priority desc,id desc' ,limit=1)
        if category_obj and not template_objects :
            template_objects = self.env['seo.product.template'].search([('template_type','=','product'),('category_ids', 'in', category_obj.id),('state','=','Enable')],order='priority desc,id desc' ,limit=1) 
        if not template_objects :
            template_objects = self.env['seo.product.template'].search([('template_type','=','product'),('is_global','=',True),('state','=','Enable')],order='priority desc,id desc' ,limit=1)
        if template_objects :
            list_field_name={
#                             'title_h1':template_objects.title_h1,
                             'meta_title' :template_objects.meta_title,
                             'meta_keywords' : template_objects.meta_keywords,
                             'meta_description': template_objects.meta_description,
                             'additional_seo_description' : template_objects.additional_seo_description,
                             'image_alt_text': template_objects.image_alt_text,
                             'product_short_description': template_objects.product_short_description,
                             'product_description': template_objects.product_description
                             }
            
            for key,value in list_field_name.items() :
                if key and value :
                    attribute_list=re.findall("\[var (.*?)\]", value)
                    attribute_list=set(attribute_list)
                    for attribute in attribute_list:
                        result = list_field_name[key]
                        if len(attribute.split("_")) > 2:
                            if attribute.split("_")[0] == 'category' :
                                field_name=attribute.split("_")[1]
                                if field_name == 'parent' :
                                    if category_obj and category_obj.parent_id and category_obj.parent_id.name :   
                                        result=list_field_name[key].replace("[var " + attribute + "]" ,category_obj.parent_id.name)
                                    else :
                                        result=list_field_name[key].replace("[var " + attribute + "]" , ' ')
                                list_field_name[key]=result
                        elif len(attribute.split("_")) > 1 :
                            if attribute.split("_")[0] == 'category' :
                                field_name=attribute.split("_")[1]
                                if 'name' in field_name :
                                    if category_obj and category_obj.name:     
                                        result=list_field_name[key].replace("[var " + attribute + "]" , category_obj.name)
                                    else :
                                        result=list_field_name[key].replace("[var " + attribute + "]" , ' ')
                            elif attribute.split("_")[0] == 'product' :
                                field_name=attribute.split("_")[1]
                                if 'price' in field_name:
                                    field_name = field_name.replace("price" ,"list_price")
                                try:    
                                    self._cr.execute("""select %s from product_template where id = %s""" %(field_name,self.id))
                                except Exception as e:
                                    self._cr.rollback()
                                    continue
                                field_value=self._cr.fetchall()
                                if field_value[0][0] :
                                    result=list_field_name[key].replace("[var " + attribute + "]" ,str(field_value[0][0]))
                                else :
                                    result=list_field_name[key].replace("[var " + attribute + "]" ,' ')
                            elif attribute.split("_")[0] == 'store' :
                                field_name=attribute.split("_")[1]
                                if 'name' in field_name and self.env.user.company_id.name :  
                                    result=list_field_name[key].replace("[var " + attribute + "]" ,self.env.user.company_id.name)
                                elif 'email' in field_name and self.env.user.company_id.email : 
                                    result=list_field_name[key].replace("[var " + attribute + "]" ,self.env.user.company_id.email)
                                elif 'website' in field_name and self.env.user.company_id.website : 
                                    result=list_field_name[key].replace("[var " + attribute + "]" ,self.env.user.company_id.website)
                                else :
                                    result=list_field_name[key].replace("<var " + attribute + "]" ,' ')
                            list_field_name[key]=result
                                 
#             product_name=list_field_name['title_h1']          
            meta_title=list_field_name['meta_title']
            meta_description=list_field_name['meta_description']
            
            seo_setting_obj=self.env['seo.template.setting'].search([],limit=1)
            if meta_title and seo_setting_obj and len(meta_title) > seo_setting_obj.meta_title_limit :
                if seo_setting_obj.meta_title_limit >= 25:
                    meta_title=meta_title[:seo_setting_obj.meta_title_limit]
                else :
                    meta_title=meta_title[:55]
            
            if meta_description and seo_setting_obj and len(meta_description) > seo_setting_obj.meta_description_limit :
                if seo_setting_obj.meta_description_limit >= 25:
                    meta_description=meta_description[:seo_setting_obj.meta_description_limit]
                else :
                    meta_description=meta_description[:150]
                
#             if product_name and len(product_name) > seo_setting_obj.product_name_limit :
#                 if seo_setting_obj.product_name_limit >= 10:
#                     product_name=product_name[:seo_setting_obj.product_name_limit]
#                 else :
#                     product_name=product_name[:25]
#             
#             list_field_name['title_h1']=product_name
            list_field_name['meta_title']=meta_title
            list_field_name['meta_description']=meta_description            
        
                 
            if list_field_name :
                list_field_name.update({'seo_product':template_objects })
            return list_field_name
        
            
              