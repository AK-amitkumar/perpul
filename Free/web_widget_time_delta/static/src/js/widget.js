flectra.define('web.web_widget_time_delta', function(require) {
    "use strict";

    var field_registry = require('web.field_registry');
    var Field = field_registry.get('char');

    var FieldTimeDelta = Field.extend({

        template: 'FieldTimeDelta',
        widget_class: 'oe_form_field_time_delta',

        _renderReadonly: function () {
            var total = parseInt(this.value, 10);
            this.$el.text(humanizeDuration(total*1000));

        },

        _getValue: function () {
            var $input = this.$el.find('input');
            return $input.val();
        },

        _renderEdit: function () {

                var show_value = parseInt(this.value, 10);
                var $input = this.$el.find('input');
                $input.val(show_value);

                $input.durationPicker({
                    showSeconds: true,
                    onChanged: function (newVal) {
                        $input.val(newVal);
                    }
                });
                this.$input = $input;

        },


    });



    field_registry
        .add('time_delta_list', FieldTimeDelta)
        .add('time_delta', FieldTimeDelta);


return {
    FieldTimeDelta: FieldTimeDelta
};

});
