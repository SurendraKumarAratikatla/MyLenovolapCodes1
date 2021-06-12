/**
 * A Backbone view that provides several helper functions specific to forms.
 */
var FormView = Backbone.View.extend({
    /**
     * A CSS selector that indicates all the form elements in this view
     */
    formSelector : 'button, .btn, input, textarea',

    // validation errors in the form need to be set to this.formErrors as the
    // common this.errorHandler will access it and check to see if the save errors can be shown or not
    // for  partial saves. for partial saves if the form has errors then save errors are not shown.
    formErrors : null,

    events : {},

    extraEvents : {
        "keypress input" : "keypress",
        'change input, textarea, select' : 'validateChange'
    },

    delegateEvents : function(events){
        // Merge extra events
        events || (events = {});
        _.defaults(events, (_.isFunction(this.events) ? this.events() : this.events), this.extraEvents);
        Backbone.View.prototype.delegateEvents.call(this, events);
    },

    initialize : function(options){
        Backbone.View.prototype.initialize.call(this, options);

        var self = this;
        if(this.$el.hasClass('modal')){
            // This form is within a modal
            this.$el.on('hide', function(){
                // Listen to "hide" modal events so that we can remove all
                // tooltips when the modal closes
                self.clearErrors();
            });
        }
    },

    render : function(){
        Backbone.View.prototype.render.call(this);
        this.$el.find('input[type!="hidden"]').first().focus();
    },

    destroy : function(){
        // Remove all error bubbles (if we don't remove them, they
        // keep hanging around even after a navigation)
        this.clearErrors();

        // Call the parent destroy
        Backbone.View.prototype.destroy.call(this);
    },

    keypress : function(e){
        if(e.which == 10 || e.which == 13){
            var btn = this.$el.find('button[type="submit"]');
            if(btn.length > 0){
                // This view has a submit button

                // Prevent keypress from propagating to parent views
                e.stopImmediatePropagation();
                e.cancelBubble = true;

                // Trigger the submit button in this view
                btn.trigger("click");
                return false;

            }
        }
    },

    disable : function(){
        $(this.el).find(this.formSelector).attr('disabled', 'disabled');
    },

    enable : function(){
        $(this.el).find(this.formSelector).removeAttr('disabled');
    },

    /**
     * Persists edits to the server
     * Save function that will call the bind on the view renders errors if any, goes ahead saving the partial form as well
     * If different functionality is required override the  function
     */
    submit : function(){
        // If the view is not associated with a model, there is nothing to save
        if(!this.model) return;

        this.formErrors = this.bind();
        this.renderErrors(this.formErrors);

        if(!this.model.hasChanged()){
            // There are no changes to the form, so do nothing
            return;
        }

        if(_.isEmpty(this.formErrors)){
            // disable the button only if the there are no errors and user knows that he is saving form
            this.disable();
        }

        // Persist to server in any case
        this.model.save(null, {
            success : this.saveSuccess,
            error : this.errorHandler
        });

    },

    /**
     * Validates a field.
     *
     * @param {Event} e Change event
     */
    validateChange : function(e){
        // Prevent the change from bubbling to parent views
        e.stopImmediatePropagation();

        var el = $(e.currentTarget);
        var fields = {};
        var name = el.attr('name');

        // support for the validation of fields associated with values that are stored within another object
        // eg. input field with name "party.child" is assocated with a value that resides within party object which is
        // the actual attribute. Hence convert such a key value pair into a key value pair, where in the value
        // is the object.
        // eg {"party.child":9} -> {"party":{"child":9}}
        var nameArr = name.split('.');
        for(var i = nameArr.length - 1 ; i >= 0 ; i--){
            if(i == nameArr.length - 1){
                fields[nameArr[i]] = el.val();
            }
            else{
                var newFields = {};
                newFields[nameArr[i]] = fields;
                fields = newFields;
            }
        }
        var errors = this.model ? this.model.validateAll(fields) : {};
        this.renderErrors(errors, fields);
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
    _objToAssoc : function(obj, keyPrefix){
        if(!_.isObject(obj)){
            return obj;
        }
        var retObj = {};
        if(!keyPrefix){
            keyPrefix = '';
        }
        else{
            keyPrefix = keyPrefix + '.';
        }
        for(var i in obj){
            // recursive case. value is an object convert it to associative array recursively with updated keyPrefix
            if(_.isObject(obj[i])){
                var newObj = this._objToAssoc(obj[i], keyPrefix + i);
                retObj = _.extend(retObj, newObj);
            }
            else{
                // base case. value is not an object. Create a key value pair in the return object with prefix key
                // added to the current key
                retObj[keyPrefix + i] = obj[i];
            }
        }
        return retObj;
    },
    /**
     * Renders error messages for form fields in this view. For this function to
     * work, each form element must define a "name" attribute which corresponds
     * to the field name in the errors parameter.
     *
     * @param {Object} errors   Key-value list of fields and related errors
     * @param {Object} [fields] Fields that were validated
     */
    renderErrors : function(errors, fields){
        errors = this._objToAssoc(errors);
        fields = this._objToAssoc(fields);

        if(fields == undefined){
            // If no fields were passed, it means that the entire model was
            // validated, so we'll clear out all errors from the form and
            // re-render any errors passed to us
            this.clearErrors();
            fields = errors;
            if(!_.isEmpty(errors)){
                this.focusFirstErrorField(errors);
            }
        }

        _.each(fields, function(i, field){
            var el = this.$el.find('[name="' + field + '"]').first();
            if(el.length > 0){
                if(errors && errors[field]){
                    if(el.attr('type') != 'hidden'){
                        // to change tool tip text update data-original-title
                        $(el).attr({
                            'data-original-title' : errors[field]
                        });

                        var placement = 'right';
                        if(el.hasClass('placement-top')){
                            placement = 'top';
                        }

                        // This field has an error
                        el.tooltip({
                            animation : false,
                            placement : placement,
                            trigger : 'manual',
                            title : errors[field]
                        });
                        el.tooltip('show');
                    }
                    // Mark the field's container as having an error
                    el.closest('.control-group').addClass('error');
                } else{
                    // This field has no error
                    if(el.closest('.control-group').hasClass('error')){
                        el.closest('.control-group').removeClass('error');
                        if(el.attr('type') != 'hidden'){
                            el.tooltip('hide');
                        }
                    }

                }

            } else{
                // Could not locate form element by field name
                console.log('Unable to render error for field "' + field + '"');
            }
        }, this);
    },

    /**
     * Removes all errors from within the element passed.
     *
     * @param [el] defaults to el of the view
     */
    clearErrors : function(el){
        if(!el){
            el = this.$el;
        }
        // Remove all the tooltips for fields that have errors
        el.find('.control-group.error').find('[name]').tooltip('hide');
        // remove tool tip on div that have name attribute with control-group class
        el.find('.control-group.error').tooltip('hide');

        // Remove error state from all fields
        el.find('.control-group.error').removeClass('error');
    },

    /**
     * Focuses on the first error field and scrolls to it.
     *
     * @param {Object} errors
     */
    focusFirstErrorField : function(errors){
        // We want to select the first error field on the form. jQuery's
        // selector returns results sorted by the DOM order, so build a
        // selector containing all the error fields and pick the first one
        // that jQuery returns.
        var selector = '';
        _.each(_.keys(errors), function(key){
            selector += '[name="' + key + '"],';
        });
        var first = this.$el.find(selector).first();

        if(this.$el.closest('.modal').length == 0){
            // This form is not within a modal, so scroll smoothly to first
            // error field
            if(first.offset()){
                $('html,body').animate({
                    scrollTop : first.offset().top - 100
                }, 500);
            }
        }
        // focus on first error field
        $(first).focus();
    },

    saveSuccess : function(){
        if(_.isEmpty(this.formErrors)){
            // enable the button only if the there are no errors and user knows that he is saving form
            this.enable();
            notify.success('Success');
        }
    },

    /**
     * function to be called on model.save(). expects the errors from bind to be in this.formErrors
     * if there are form errors, error handler is not called as it could be the call during partial save that happens silently
     *
     * @param modelOrCollection
     * @param resp
     * @param options
     */
    errorHandler : function(modelOrCollection, resp, options){
        // if form has errors, no need of showing server errors to the user
        // as it could be due the partial saving that is done silently
        if(_.isEmpty(this.formErrors)){
            Backbone.View.prototype.errorHandler.call(this, modelOrCollection, resp, options);
        }

        // enable all the form fields in any case
        this.enable();
    }
});