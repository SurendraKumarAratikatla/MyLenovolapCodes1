var OrganisationsEditorView = FormView.extend({
    template: '#organisationEditorTpl',
    className: 'edit-organisation',

    initialize: function () {
        this.model = this.model || new Organisation();
        FormView.prototype.initialize.apply(this, arguments);
    },

    events: {
        'click [name="submit"]': 'submit',
        'click [name="cancel"]': 'cancel'
    },

    render: function () {
        var template = _.template(
            $(this.template).html()
        );
        var data = {
            data: this.model.toJSON()
        };
        data.data.organisations = app.collection.toJSON();
        this.$el.empty().append(template(data));
        return this;
    },

    /**
     * To get all attributes
     */
    getAttrs: function () {
        var attrs = {};
        attrs.code = $.trim(this.$el.find('input[name="code"]').val());
        attrs.uri = $.trim(this.$el.find('input[name="uri"]').val());
        attrs.name = $.trim(this.$el.find('input[name="name"]').val());
        attrs.description = $.trim(this.$el.find('textarea[name="description"]').val());
        attrs.parentId =this.$el.find('select[name="parentId"]').val();
        attrs.city = $.trim(this.$el.find('input[name="city"]').val());
        attrs.address = $.trim(this.$el.find('textarea[name="address"]').val());
        attrs.state = $.trim(this.$el.find('input[name="state"]').val());
        attrs.country = $.trim(this.$el.find('input[name="country"]').val());
        attrs.pincode = $.trim(this.$el.find('input[name="pincode"]').val());
        attrs.email = $.trim(this.$el.find('input[name="email"]').val());
        attrs.phone = $.trim(this.$el.find('input[name="phone"]').val());
        attrs.mobile = $.trim(this.$el.find('input[name="mobile"]').val());
        attrs.fax = $.trim(this.$el.find('input[name="fax"]').val());
        attrs.website = $.trim(this.$el.find('input[name="website"]').val());

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

    cancel: function () {
        app.organisationsHome();
    },

    success: function () {
        app.collection.add(this.model);
        notify.success('Organisation data saved successfully.');
        // fording to organisations home page.
        setTimeout(function () {
            window.location.href = "/admin/organisations";
        }, 2000);
    },

    errorHandler: function () {
        // TODO : handel the exceptions
    }
});