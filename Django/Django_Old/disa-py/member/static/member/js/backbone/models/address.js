/**
 * Model to hold address data
 */
var Address = Backbone.Model.extend({
    urlRoot: '/api/address',

    validate: function(attr){
        var errors={};

        // loop through each field and validate
        _.each(attr,function(val,field){
            // eliminate by trimming any spaces in the value before validating
            if(_.isString(val)){
                val= $.trim(val);
            }

            switch(field){
                case 'address':
                    if(!val || val ===""){
                        // Empty string
                        errors[field]="Required";
                    }
                    break;
                // TODO: Validation is required for checkbox
            }

        },this);

        // Return any validation errors
        if(!_.isEmpty(errors)) {
            return errors;
        }
    }
});

/**
 * Collection to hold address models
 */
var AddressCollection = Backbone.Collection.extend({
   model:Address
});