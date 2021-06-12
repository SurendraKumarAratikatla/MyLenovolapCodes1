/**
 * Model to hold organisation data
 */
var Organisation = Backbone.Model.extend({
    urlRoot: '/api/organisations',

    validate: function(attr){
        var errors={};

        // loop through each field and validate
        _.each(attr,function(val,field){
            // eliminate by trimming any spaces in the value before validating
            if(_.isString(val)){
                val= $.trim(val);
            }

            switch(field){
                case 'code':
                    if(!val || val===""){
                        // Empty string
                        errors[field]='Required';
                    }
                    break;
                case 'name':
                    if(!val || val===""){
                        // Empty string
                        errors[field]='Required';
                    }
                    break;
            }
        },this);

        // Return any validation errors
        if(!_.isEmpty(errors)) {
            return errors;
        }
    }
});

/**
 * Collection to hold list of Organisation Models
 */
var OrganisationCollection = Backbone.Collection.extend({
    model: Organisation
});