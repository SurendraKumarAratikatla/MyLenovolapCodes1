/**
 * Add new seva category or edit existing seva category
 *
 * @param {SevaCategory} [model]  SevaCategory model which is to be edited. If not passed a new SevaCategory model will be instantiated
 *
 */
var SevaCategoryEditorView = FormView.extend({
    template: '#sevaCategoryEditTpl',
    className: 'edit-seva-category',

    initialize: function () {
        this.model = this.model || new SevaCategory();
        FormView.prototype.initialize.apply(this, arguments);
    },

    events: {
        'click [name=submit]': 'save',
        'click [name=cancel]': 'cancel',
        'change [name=location]': 'handleLocationChange',
        'change [name=organisation]': 'handleOrganisationChange',
        'blur [name=code]' : 'checkAvailability',
        'change [name=durationType]' : 'handleDurationType',
        'change [name=recurrence]' : 'handleRecurrenceChange'
    },

    render: function () {
        var template = _.template(
            $(this.template).html()
        );

        var data = this.model.toJSON();

        // Get all seva categorys
        data.locations = {};
        app.collection.each(function (sevaCategory) {
            if (!data.locations[sevaCategory.get('organisation').id + sevaCategory.get('location')] && sevaCategory.get('location') != "") {
                data.locations[sevaCategory.get('organisation').id + sevaCategory.get('location')] = {
                    "location": sevaCategory.get('location'),
                    "organisation": sevaCategory.get('organisation').id
                }
            }
        });

        // Get organisation collection
        data.organisations = app.organisationColl.toJSON();

        this.$el.empty().append(template({data: data}));
        return this;
    },

    /**
     * Called when organisation value gets changed.
     * Populate available seva category locations list in location drop down for the selected organisation.
     */
    handleOrganisationChange: function () {
        // Get the selected organisation
        var oid = this.$el.find('select[name="organisation"]').val();

        var locations = this.$el.find('[name="location"]');
        // Hide all location options
        locations.find('option').hide();
        // Show options for the selected organisation
        locations.find('option[data-organisation="' + oid + '"]').show();
        // Always show other location
        locations.find('option[value="other"]').show();
    },

    /**
     * Called when locations value gets changed.
     * Shows input field if other location is selected, else, hides it.
     */
    handleLocationChange: function () {
        var location = $.trim(this.$el.find('select[name="location"]').val());
        if (location == 'other') {
            $('.other').show();
        } else {
            $('.other').hide();
        }
    },

    /**
     * Get all the form field values and return array.
     * This function will be call when we click submit button
     */
    getAttributes: function () {
        var attrs = {};
        var location = $.trim(this.$el.find('select[name="location"]').val());
        var recurrence = $.trim(this.$el.find('select[name="recurrence"]').val());
        var showStartDate = this.$el.find('input[name="showStartDate"]:checked').val();
        if (location == 'other') {
            attrs.location = $.trim(this.$el.find('input[name="locationName"]').val());
        } else {
            attrs.location = location;
        }
        attrs.code = $.trim(this.$el.find('input[name="code"]').val().toUpperCase());
        attrs.amount = $.trim(this.$el.find('input[name="amount"]').val());
        attrs.name = $.trim(this.$el.find('input[name="name"]').val());
        attrs.organisation = $.trim(this.$el.find('select[name="organisation"]').val());
		attrs.status = $.trim(this.$el.find('select[name="status"]').val());
        attrs.sponsorItemType = $.trim(this.$el.find('input[name="sponsorItemType"]').val());
        attrs.showStartDate = (showStartDate) ? showStartDate : false ;
        attrs.recurrence = recurrence;
        if(recurrence && recurrence != 'onetime'){
            attrs.duration = $.trim(this.$el.find('input[name="duration"]').val());
            attrs.durationType = $.trim(this.$el.find('select[name="durationType"]').val());
        }else{
            attrs.duration = 1;
            attrs.durationType = 'day';
        }

        return attrs;
    },

    /**
     * To save (create or update) seva category data.
     */
    save: function () {
        var attributes = this.getAttributes();
        this.model.save(attributes, {
            success: this.saveSuccess,
            error: this.errorHandler,
            patch: true
        });
    },
    saveSuccess: function () {
        // add model to the seva category collection
        app.collection.add(this.model);
        notify.success('Seva category data saved successfully');
        // fording to organisations home page.
        setTimeout(function(){
            window.location.href="/admin/sevacategoreis";
        },2000);
    },
    cancel: function () {
        window.history.back();
    },

    errorHandler: function(){
       $('.error-seva-code').html('Code exists');
    },

    /**
     * To check availability of seva code
     * @param e
     */
    checkAvailability: function(e){
        var code=$(e.currentTarget).val().toUpperCase();
        var self=this;
        $.ajax({
            //TODO: Use seva categories api to check for a seva category by code If found, code is not available
            url: "/api/availabilityCheck?code="+code,
            success:function(result){
                console.log(result);
                if(result=="available"){
                    self.$el.find('.error-seva-code').html('Code exists');
                    return false;
                }else{
                    self.$el.find('.error-seva-code').html('');
                    return true;
                }
            }
        });
    },

    /**
     * Displaying duration text field if duration type is life time
     *
     * @param e
     */
    handleDurationType: function(e){
        var durationType = $(e.currentTarget).val();
        if(durationType == 'life_time'){
            this.$el.find('#duration').removeClass('show');
            this.$el.find('#duration').addClass('hide');
        }else{
            this.$el.find('#duration').addClass('show');
            this.$el.find('#duration').removeClass('hide');
        }
    },

    handleRecurrenceChange: function(e){
        var recurrence = $(e.currentTarget).val();
        if(recurrence == 'onetime'){
            this.$el.find('#duration_div').hide();
        }else{
            this.$el.find('#duration_div').show();
        }
    }
});