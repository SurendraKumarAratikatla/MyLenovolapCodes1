var MemberEditorView = FormView.extend({
    template: '#memberEditorTpl',
    className: 'member-detail',

    events: {
        'click [name="submit"]': 'submit',
        'click [name="cancel"]': 'cancel',
        'keydown input': 'onSubmitKeyPress'
    },

    initialize: function (options) {
        _.bindAll(this);
    },

    render: function () {
        if (this.model.syncing) {
            // model is still syncing i.e. Fetch request has been made. So do not continue with render. View is already
            // listening for the model
            this.listenToOnce(this.model, 'sync', this.render);
            return;
        }

        var template = _.template(
            $(this.template).html()
        );

        var data = this.model.toJSON();
        // For getting member id If member is exists
        if (!$.isEmptyObject(data)) {
            data.mid = this.model.getMid();
        }

        data.nakshatramColl = app.nakshatramCollection.toJSON();
        this.$el.empty().append(template({data: data}));
        this.initDatePicker();
        if (data.id) {
            var date = data['birthDate'];
            var year = data['birthYear'];
            this.setDate(date, year);
        }
        return this;
    },

    initDatePicker: function () {
        var year = new Date().getFullYear();
        // initialise date picker for birth date
        this.$el.find("input[name='birthDateInput']").datepicker({
            dateFormat: "d MM, yy",
            altFormat: "yy-mm-dd",
            changeMonth: true,
            changeYear: true,
            yearRange: '1930:' + year,
            altField: "input[name='birthDate']"
        });

        // pre-select date
        this.$el.find("input[name='birthDateInput']").datepicker("setDate", new Date());
    },

    /**
     * Convert date format to
     */
    setDate: function (date, year) {
        if (date != null) {
            var day = date.substr(2, 2);
            var month = date.substr(0, 2);
            var formattedDate = year + '-' + month + '-' + day;
            this.$el.find("input[name='birthDateInput']").datepicker("setDate", getDateObject(formattedDate));
        }
    },

    getAttrs: function () {
        var attrs = {};
        attrs.salutation = this.$el.find('select[name="salutation"]').val();
        attrs.name = $.trim(this.$el.find('input[name="name"]').val());
        attrs.surname = $.trim(this.$el.find('input[name="surname"]').val());
        attrs.place = $.trim(this.$el.find('input[name="place"]').val());
        attrs.gender = this.$el.find('select[name="gender"]').val();
        attrs.birthDate = $.trim(this.$el.find('input[name="birthDate"]').val());
        attrs.gotram = $.trim(this.$el.find('input[name="gotram"]').val());
        attrs.nakshatram = this.$el.find('select[name="nakshatram"]').val();
        attrs.email = $.trim(this.$el.find('input[name="email"]').val());
        attrs.phone = $.trim(this.$el.find('input[name="phone"]').val());
        attrs.mobile = $.trim(this.$el.find('input[name="mobile"]').val());

        return attrs;
    },

    submit: function () {
        var attrs = this.getAttrs();
        this.model.save(attrs, {
            success: this.success,
            error: this.errorHandler,
            patch: true
        });
    },

    success: function () {
        notify.success('Member data saved successfully');
        if (this.options.success) {
            // success callback is specified. Call the callback function
            this.options.success.apply(this, arguments);
        }
        else {
            // no callback specified
            app.memberDetails(this.model);
        }
    },

    cancel: function () {
        if (this.options.cancel) {
            // cancel callback is specified. Call the callback function
            this.options.cancel();
        }
        else {
            // no callback specified
            if (this.model.id) {
                // this is an existing model take to the member detail page
                app.memberDetails(this.model);
            }
            else {
                // This is a new model take to the members home page
                app.membersHome();
            }
        }
    },

    /**
     * Called when any key is pressed
     * @param e
     */
    onSubmitKeyPress: function (e) {
        if (event.which == 13 || e.keyCode == 13) {
            this.submit();
        }
    }
});

var EditProfileView = Backbone.View.extend({
    template: '#editProfileTpl',
    className: 'member-detail',

    render: function () {
        var template = _.template(
            $(this.template).html()
        );
        var data = this.model.toJSON();
        this.$el.empty().append(template(data));
        return this;
    }
});