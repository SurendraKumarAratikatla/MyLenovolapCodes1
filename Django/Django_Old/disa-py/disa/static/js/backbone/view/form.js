/**
 * A Backbone view that provides several helper functions specific to forms.
 */
var FormView = Backbone.View.extend({
    /**
     * A CSS selector that indicates all the form elements in this view
     */
    formSelector: 'button, .btn, input, textarea , select',

    initialize: function (options) {
        _.bindAll(this);
        this.listenTo(this.model, 'change', this.change);
        this.listenTo(this.model, 'invalid', this.handleErrors);
    },


    disable: function () {
        $(this.el).find(this.formSelector).attr('disabled', 'disabled');
    },

    enable: function () {
        $(this.el).find(this.formSelector).removeAttr('disabled');
    },

    /**
     * Called when model is validated and has invalid attributes
     */
    handleErrors: function () {
        this.renderErrors(this.model.validationError);
    },

    /**
     * Renders error messages for form fields in this view. For this function to
     * work, each form element must define a "name" attribute which corresponds
     * to the field name in the errors parameter.
     *
     * @param {Object} errors   Key-value list of fields and related errors
     * @param {Object} [fields] Fields that were validated. If null assumes all the fields werr validated
     */
    renderErrors: function (errors, fields) {
        errors = errors || {};
        var unrenderedErrors = {};
        errors = this._objToAssoc(errors);
        fields = this._objToAssoc(fields);

        if (fields == undefined) {
            // If no fields were passed, it means that the entire model was
            // validated, so we'll clear out all errors from the form and
            // re-render any errors passed to us
            this.clearErrors();
            fields = errors;
        }

        _.each(fields, function (i, field) {
            // Get the field with the specified name attribute that is visible
            var el = this.$el.find('[name="' + field + '"]:visible').first();

            if (el.length > 0) {
                if (errors && errors[field]) {
                    if (el.attr('type') != 'hidden') {
                        // to change tool tip text update data-original-title
                        $(el).attr({
                            'data-original-title': errors[field]
                        });

                        var placement = 'right';
                        if (el.hasClass('placement-top')) {
                            placement = 'top';
                        } else if (el.hasClass('placement-bottom')) {
                            placement = 'bottom';
                        }

                        // This field has an error
                        el.tooltip({
                            animation: false,
                            placement: placement,
                            trigger: 'manual',
                            title: errors[field]
                        });
                        el.tooltip('show');
                    }
                    // Mark the field's container as having an error
                    el.closest('.control-group').addClass('error');
                } else {
                    // This field has no error
                    if (el.closest('.control-group').hasClass('error')) {
                        // This field already had error previously. Close it.
                        el.closest('.control-group').removeClass('error');
                        if (el.attr('type') != 'hidden') {
                            el.tooltip('hide');
                        }
                    }
                }

            } else {
                // check if the field exists in error. Some times errors is undefined with fields being defined.
                // In that case error will occur if the input element for the field is hidden.
                // Eg. Click on any of the cities in the drop down suggested by geonames API in seller basic profile page.
                if (errors && errors.hasOwnProperty(field)) {
                    unrenderedErrors[field] = errors[field];
                    // Could not locate form element by field name
                    console.log('Unable to render error for field "' + field + '"');
                }
            }
        }, this);

        return unrenderedErrors;
    },

    /**
     * Removes all errors from within the element passed.
     *
     * @param [el] defaults to el of the view
     */
    clearErrors: function (el) {
        if (!el) {
            el = this.$el;
        }

        if (!(el.hasClass('control-group') && el.hasClass('error'))) {
            el = el.find('.control-group.error');
        }
        // Remove all the tooltips for fields that have errors
        el.find('[name]').tooltip('hide');
        // remove tool tip on div that have name attribute with control-group class
        el.tooltip('hide');

        // Remove error state from all fields
        el.removeClass('error');
    },

    /**
     * Converts a multilevel structured object to a simple object with key value pairs.
     * Key of the object is the concatenation of the keys at each level up to the value of the original object
     *
     * eg.
     * keyPrefix : "discount"
     * obj :
     * {
     *       "child" : {
     *                       "age" : 3,
     *                       "amount" 4
     *                   }
     * }
     *
     *
     * returnObj:
     * {
     *         "discount.child.age" : 3,
     *         "discount.child.amount":4
     * }
     *
     * @param obj
     * @param keyPrefix
     * @return {*}
     * @private
     */
    _objToAssoc: function (obj, keyPrefix) {
        if (!_.isObject(obj)) {
            return obj;
        }
        var retObj = {};
        if (!keyPrefix) {
            keyPrefix = '';
        }
        else {
            keyPrefix = keyPrefix + '.';
        }
        for (var i in obj) {
            // recursive case. value is an object convert it to associative array recursively with updated keyPrefix
            if (_.isObject(obj[i])) {
                var newObj = this._objToAssoc(obj[i], keyPrefix + i);
                retObj = _.extend(retObj, newObj);
            }
            else {
                // base case. value is not an object. Create a key value pair in the return object with prefix key
                // added to the current key
                retObj[keyPrefix + i] = obj[i];
            }
        }
        return retObj;
    }

//    errorHandler : function(modelOrCollection, resp, options){
//        // if form has errors, no need of showing server errors to the user
//        // as it could be due the partial saving that is done silently
//        if(_.isEmpty(this.formErrors)){
//            Backbone.View.prototype.errorHandler.call(this, modelOrCollection, resp, options);
//        }
//
//        // enable all the form fields in any case
//        this.enable();
//    }
});