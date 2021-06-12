/**
 * Model to hold member resp
 */
var Member = Backbone.Model.extend({
    midPrefix: 'MID#',
    urlRoot: '/api/members',

    defaults: function () {
        return  {
            sevas: new SevaCollection()
        };
    },

    parse: function (resp) {
        // Parse sevas and ensure its a collection
        if (resp.sevas) {
            // Get the existing sevas attributes.
            var sevas = this.get('sevas');
            if (sevas && sevas._byId) {
                // Sevas is already a collection. Merge existing sevas response to the existing collection
                sevas = sevas.add(resp.sevas, {merge: true});
            }
            else {
                // Sevas is not already a collection. Create new.
                sevas = new SevaCollection(resp.sevas);
            }
            resp.sevas = sevas;
        }

        // Parse addresses and ensure its a collection
        if (resp.addresses) {
            // Get the existing addresses attributes.
            var addresses = this.get('addresses');
            if (addresses && addresses._byId) {
                // Addresses is already a collection. Merge existing addresses response to the existing collection
                addresses = addresses.add(resp.addresses, {merge: true});
            }
            else {
                // Addresses is not already a collection. Create new.
                addresses = new AddressCollection(resp.addresses);
            }
            resp.addresses = addresses;
        }

        return resp;
    },

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
                case 'surname':
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
                case 'place':
                    if (!val || val === "") {
                        // Empty string
                        errors[field] = "Required";
                    }
                    break;

                case 'email':
                    if (val) {
                        var pattern = new RegExp(/^((([a-z]|\d|[!#\$%&'\*\+\-\/=\?\^_`{\|}~]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])+(\.([a-z]|\d|[!#\$%&'\*\+\-\/=\?\^_`{\|}~]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])+)*)|((\x22)((((\x20|\x09)*(\x0d\x0a))?(\x20|\x09)+)?(([\x01-\x08\x0b\x0c\x0e-\x1f\x7f]|\x21|[\x23-\x5b]|[\x5d-\x7e]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(\\([\x01-\x09\x0b\x0c\x0d-\x7f]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]))))*(((\x20|\x09)*(\x0d\x0a))?(\x20|\x09)+)?(\x22)))@((([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.)+(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.?$/i);
                        if (!pattern.test(val)) {
                            errors[field] = "Invalid"
                        }
                    }
                    break;
            }
        }, this);

        // Return any validation errors
        if (!_.isEmpty(errors)) {
            return errors;
        }
    },

    /**
     * Padding 0's to member id
     * @returns {string}
     */
    getMid: function () {
        if (!this.has('mid')) return null;

        var memberId = this.get('mid').toString();
        var mid = $.strPad(memberId, 3, 0, 'left');
        return this.midPrefix + mid;
    },

    /**
     * Gets complete name of the member.
     *
     * @returns {string}
     */
    getFullName: function () {
        var name = "";

        // Set salutation. Default to "Sri"
        var salutation = this.get('salutation');
        if (salutation && salutation != "" || salutation == null) {
            salutation = "Sri"
        }

        return salutation + " " + this.get('name') + " " + (this.get('surname')||'');
    },

    /**
     * Get the url for members photo.
     */
    getPhoto: function () {
        if (this.has('photo')) {
            // Return the photo url as saved in the db.
            // We now have a symfony2 controller method mapped to the route to serve photos
            return this.get('photo');
        }
    },

    /**
     * Get Primary address for the member that is valid. This is used in printing dispatch letter
     */
    getValidPrimaryAddress: function(){
        // Get the first address that satisfies the conditions
        return this.get('addresses').find(function(address) {
            // Address is valid and primary. This is what we need
            return address.get('isValid') && address.get('isPrimary');
        });
    }

});

/**
 * Collection to hold member models
 */
var MemberCollection = Backbone.Collection.extend({
    url: '/api/members',
    model: Member
});
