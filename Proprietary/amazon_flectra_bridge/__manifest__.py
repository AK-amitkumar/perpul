# -*- coding: utf-8 -*-
#################################################################################
# Author      : Webkul Software Pvt. Ltd. (<https://webkul.com/>)
# Copyright(c): 2017-Present Webkul Software Pvt. Ltd.
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
{
  "name"                 :  "Amazon Perpul Bridge(AOB)",
  "summary"              :  "Amazon Perpul Bridge extension provides in-depth integration with Perpul and Amazon.",
  "category"             :  "Website",
  "version"              :  "0.1",
  "sequence"             :  1,
  "author"               :  "Webkul Software Pvt. Ltd.",
  "license"              :  "Other proprietary",
  "website"              :  "https://store.webkul.com/Amazon-Perpul-Bridge.html",
  "description"          :  """https://webkul.com/blog/amazon-flectra-bridge/,
                                Amazon Perpul Bridge  is the Perpul Extension to connect Amazon Marketplace and Perpul.
                                it import order , partner , product , category in flectra from Amazon,
                                it also manage product stock / Inventory ,
                                This module also support feature of product export/update over Amazon .""",
  "live_test_url"        :  "http://flectra.webkul.com:8010/web?db=Amazon_Odoo_Bridge",
  "depends"              :  ['flectra_multi_channel_sale'],
  "data"                 :  [
                             'security/ir.model.access.csv',
                             'wizard/wizard.xml',
                             'wizard/inherits.xml',
                             'views/views.xml',
                             'views/search.xml',
                             'views/inherits.xml',
                             'data/report.xml',                             
                             'data/data.xml',
                             'data/cron.xml',
                             'views/dashboard_view_inherited.xml',
                            ],
  "images"               :  ['static/description/Banner.png'],
  "application"          :  True,
  "installable"          :  True,
  "auto_install"         :  False,
  "price"                :  200,
  "currency"             :  "EUR",
  "external_dependencies":  {'python': ['mws']},
}
