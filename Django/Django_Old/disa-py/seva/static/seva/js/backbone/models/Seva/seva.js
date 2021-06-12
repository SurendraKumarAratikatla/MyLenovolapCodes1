/**
 * Model to hold seva data
 */
var Seva = Backbone.Model.extend({
    TYPE_DONOR: 'Donor',
    TYPE_OTHER: 'Other',
    urlRoot: '/api/sevas',

    parse: function (resp) {
        if (resp.member) {
            var member = this.get('member');
            if (member && member.cid) {
                // Member attribute of the seva is already a Member model. Set the new values to the Member model
                member = member.set(resp.member, {parse: true});
            }
            else {
                // Member attribute of seva not a model. Create an instance of Member model.
                member = new Member(resp.member, {parse: true});
            }
            resp.member = member;
        }
        return resp;
    },

    /**
     * Calculating end date using date-pai.js
     *
     * @param startDate
     * @param durationType
     * @param duration
     * @returns {string}
     */
    calculateEndDate: function (startDate, durationType, duration) {
        var endDate;
        switch (durationType) {
            case "day":
                endDate = startDate.add(duration).day();
                break;
            case "month":
                endDate = startDate.addMonths(duration);
                break;
            case "year":
                endDate = startDate.addYears(duration);
                break;
            case "week":
                endDate = startDate.addWeeks(duration);
                break;
        }

        return endDate;

    },

    /**
     * Preparing seva summary
     *
     * @param startDate
     * @param endDate
     * @param recurrence
     * @returns {string}
     */
    sevaSummary: function (startDate, endDate, recurrence) {
        var summary = '';
        if (recurrence != "onetime") {
            var format = '';
            switch (recurrence) {
                case "year":
                    format = 'MMMM d';
                    break;
                case "month":
                    format = 'd';
                    break;
                case "week":
                    format = 'dddd';
                    break;
            }

            summary = (format && startDate.toString(format));

            summary += ', repeats every ' + recurrence;

            if (endDate) {
                summary += ' till ' + endDate.toString('MMMM d, yyyy');
            }
        }
        else {
            summary = startDate.toString('MMMM d, yyyy');
        }
        return summary;
    },

    validate: function (attr) {
        var errors = {};

        // loop through each field and validate
        _.each(attr, function (val, field) {
            // eliminate by trimming any spaces in the value before validating
            if (_.isString(val)) {
                val = $.trim(val);
            }

            switch (field) {
                case 'organisation':
                    if (!val || val === "") {
                        // Empty string
                        errors[field] = "Required";
                    }
                    break;
                case 'sevaCategory':
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
    } // validate
});

/**
 * Collection to hold seva models
 */
var SevaCollection = Backbone.Collection.extend({
    model: Seva,
    url: '/api/sevas'
});
