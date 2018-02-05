# -*- coding: utf-8 -*-
#################################################################################
# Author      : Webkul Software Pvt. Ltd. (<https://webkul.com/>)
# Copyright(c): 2015-Present Webkul Software Pvt. Ltd.
# All Rights Reserved.
#
#
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
#
# You should have received a copy of the License along with this program.
# If not, see <https://store.webkul.com/license.html/>
#################################################################################

from flectra import api, fields, models, _
from flectra.exceptions import Warning

class WebkulWebsiteAddons(models.TransientModel):
	_name = 'webkul.website.addons'
	_inherit = 'res.config.settings'

	# Social Network

	# Product Management
	module_dynamic_bundle_products = fields.Boolean(string="Website Customize Bundle Products")
	module_wk_review = fields.Boolean(string="Website: Product Review")

	#Delivery Method

	# Stock Management
	module_website_stock = fields.Boolean(string = "Website: Product Stock")

	# web Page
	module_website_360degree_view = fields.Boolean(string="Website: Product 360° VIEW")
	module_email_verification = fields.Boolean(string = "Email Verification")
	module_website_seo = fields.Boolean(string = "Website SEO")
	module_website_country_restriction = fields.Boolean(string="Website Country Restriction")
	module_website_estimated_delivery = fields.Boolean(string = "Website Estimated Delivery")
	# Sales Promotion
	module_website_daily_deals = fields.Boolean(string = "Website Daily Deals")
	module_website_terms_conditions = fields.Boolean(string = "Website: Terms and Conditions")
	module_social_network_tabs = fields.Boolean(string="Social Network Tabs")
	module_website_sales_count = fields.Boolean(string="Website Sales Count")
	module_website_product_vote = fields.Boolean(string = "Website: Product Vote")
	module_website_cart_settings = fields.Boolean(string = "Website Cart Settings")        