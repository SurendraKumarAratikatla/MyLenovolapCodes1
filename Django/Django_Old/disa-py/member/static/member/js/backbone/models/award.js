/**
 * Model to hold Award
 */
var Award= Backbone.Model.extend({
    urlRoot: '/api/awards',

    /**
     * Validates the attributes passed
     *
     * @param attrs
     * @returns {{}}
     */
    validate: function (attrs) {
        var errors = {};

        // loop through each field and validate
        _.each(attrs, function (val, field) {
            // eliminate by trimming any spaces in the value before validating
            if (_.isString(val)) {
                val = $.trim(val);
            }

            switch (field) {
                case 'description':
                    if (!val || val === "") {
                        errors[field] = "Required";
                    }
                    break;
                case 'name':
                    if (!val || val === "") {
                        // Empty string
                        errors[field] = "Required";
                    }
                    break;
                case 'year':
                    if (!val || val === "") {
                        // Empty string
                        errors[field] = "Required";
                    }
                    break;
            }
        }, this);

        // Return any validation errors
        if (!_.isEmpty(errors)) {
            return errors;
        }
    }
});

/**
 * Collection to hold award models
 */
var AwardCollection = Backbone.Collection.extend({
    url: '/api/awards',
    model: Award
});
