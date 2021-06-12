/**
 * Model to hold seva category data
 */
var SevaCategory = Backbone.Model.extend({
    'urlRoot': '/api/seva-categories',

    validate: function(attr){
        var errors={};

        // loop through each field and validate
        _.each(attr,function(val,field){
            // eliminate by trimming any spaces in the value before validating
            if(_.isString(val)){
                val= $.trim(val);
            }

            switch(field){
                case 'organisation':
                    if(!val || val===""){
                        // Empty string
                        errors[field]='Required';
                    }
                    break;
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
                case 'amount':
                    // Empty field validation
                    if(!val || val===""){
                        // Empty string
                        errors[field]='Required';
                    }

                    if(val){
                        // Check whether the value is a number or not
                        if(isNaN(val)){
                            // If value is string
                            errors[field]='It should be a Number';
                        }else{
                            // Check whether the value is positive or not
                            if(val<=0){
                                errors[field]='It should be a positive number';
                            }
                        }
                    }

                    break;
                case 'durationType':
                    var recurrence = $.trim($("#recurrence").val());
                    if(recurrence && recurrence !='onetime'){
                        var durationValue = $.trim($("#durationType").val());
                        if(durationValue != '' && durationValue != 'life_time'){
                            var duration = $.trim($("#duration").val());
                            if(!duration || duration==="" || !durationValue || durationValue ===""){
                                errors['duration']='Required';
                            }
                        }
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
 * Collection to hold seva category models
 */
var SevaCategoryCollection = Backbone.Collection.extend({
    model:SevaCategory
});
