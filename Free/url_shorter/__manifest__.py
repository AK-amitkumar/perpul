# -*- coding: utf-8 -*-
# Copyright 2017 Hugo Rodrigues
# License BSD-3-Clause
{
    "name": "URL Shorter",
    "summary": "Convert long URLs to shorter ones",
    "version": "11.0.1.0.0",
    "category": "Tools",
    "website": "https://hugorodrigues.net",
    "author": "Hugo Rodrigues",
    "license": "Other OSI approved licence",
    "application": True,
    "installable": True,
    "depends": [
        "base_automation"
        ],
    "data": [
        "views/url_shorter_view.xml",
        "security/ir.model.access.csv",
        "security/security.xml",
        "data/action_rule.xml",
        "data/cron.xml"
        ]
}
