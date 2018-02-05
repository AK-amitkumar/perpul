flectra.define('widget_tag_state.field_state', function (require) {
"use strict";

var core = require('web.core');
var common = require('web.form_common');
var Model = require('web.Model');
var time = require('web.time');
var utils = require('web.utils');
var FieldBinaryFile = core.form_widget_registry.get('binary');

var _t = core._t;


var SetBulletStatus = common.AbstractField.extend(common.ReinitializeFieldMixin,{
    init: function(field_manager, node) {
        this._super(field_manager, node);
        this.classes = this.options && this.options.classes || {};
    },
    render_value: function() {
        this._super.apply(this, arguments);
        if (this.get("effective_readonly")) {
            var bullet_class = this.classes[this.get('value')] || 'default';
            if (this.get('value')){
                var title = this.get('value');
                this.$el.attr({'title': title, 'style': 'display:inline'});
                this.$el.removeClass('text-success text-danger text-default');
                this.$el.html($('<span>' + title + '</span>').addClass('label label-' + bullet_class));
            }
        }
    },
});

core.form_widget_registry.add('bullet_state', SetBulletStatus);
});
