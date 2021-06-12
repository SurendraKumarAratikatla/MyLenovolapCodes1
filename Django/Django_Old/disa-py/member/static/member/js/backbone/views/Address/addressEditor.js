/**
 * View to add/edit addresses details of specified member
 *
 * @param {Member}   member  Member model for which the addresses is to be added / edited
 * @param {Address}  model   Address model that is to be added / edited
 */
var AddressEditorView = FormView.extend({
    template: "#addressEditor",

    events: {
        'click [name="submit"]': 'save',
        'click [name="cancel"]': 'cancel',
        'keydown input': 'onSubmitKeyPress'
    },

    initialize: function () {
        _.bindAll(this);
        this.addresses = new AddressCollection();
        this.map = [];
    },

    render: function () {
        var template = _.template(
            $(this.template).html()
        );
        var data = this.model.toJSON();
        this.$el.empty().append(template({data: data}));

        var self = this;
        this.$el.find(':input[name="country"],:input[name="state"],:input[name="district"],:input[name="city"]').typeahead({
            source: function (query, process) {
                this.list = new Backbone.Collection();
                this.list.url = this.$element.attr('data-typeahead-url');
                this.list.fetch({
                    data: {
                        q: query
                    },
                    success: function (collection) {
                        var items = [];
                        collection.each(function (model) {
                            var item = [];
                            if (model.has('city')) {
                                item.push(model.get('city').trim());
                            }
                            if (model.has('district')) {
                                item.push(model.get('district').trim());
                            }
                            if (model.has('state')) {
                                item.push(model.get('state').trim());
                            }
                            if (model.has('country')) {
                                item.push(model.get('country').trim());
                            }

                            item = item.join(',');
                            items.push(item);
                            self.map[item] = model;
                        });
                        process(items);
                    }
                })
            },
            updater: this.updater,
            sorter: this.sorter,
            minLength: 2
        });

//        this.$el.find('[name="district"]').typeahead({
//            source: this.districtsSource,
//            updater: this.districtsUpdater,
//            sorter: this.sorter,
//            minLength: 2
//        });

        return this;
    },


    updater: function (item) {
        var model = this.map[item];
        if (model.has('city')) {
            this.$el.find('[name="city"]').val(model.get('city').trim());
        }
        if (model.has('district')) {
            this.$el.find('[name="district"]').val(model.get('district').trim());
        }
        if (model.has('state')) {
            this.$el.find('[name="state"]').val(model.get('state').trim());
        }
        if (model.has('country')) {
            this.$el.find('[name="country"]').val(model.get('country').trim());
        }

        item = item.split(',');

        return item[0];
    },

    sorter: function (items) {
        return items.sort();
    },

    getAttributes: function () {
        var attrs = {};
        var isValid = false;
        var isPrimary = false;
        attrs.member = this.options.member.id;
        attrs.address = $.trim(this.$el.find('textarea[name="address"]').val());
        attrs.city = $.trim(this.$el.find('input[name="city"]').val());
        attrs.district = $.trim(this.$el.find('input[name="district"]').val());
        attrs.state = $.trim(this.$el.find('input[name="state"]').val());
        attrs.country = $.trim(this.$el.find('input[name="country"]').val());
        attrs.pin = $.trim(this.$el.find('input[name="pin"]').val());
        attrs.phone = $.trim(this.$el.find('input[name="phone"]').val());
        var valid = this.$el.find('input[name="valid"]:checked').val();
        if (valid == "valid") {
            isValid = true;
        }
        var primary = this.$el.find('input[name="primary"]:checked').val();
        if (primary == "primary") {
            isPrimary = true;
        }

        attrs.isValid = isValid;
        attrs.isPrimary = isPrimary;

        return attrs;
    },
    save: function () {
        var attributes = this.getAttributes();
        this.model.save(attributes, {
            success: this.success,
            error: this.errorHandler,
            patch: true
        });
    },

    success: function (model) {
        var addresses = this.options.member.get('addresses');
        if (addresses) {
            addresses.add(model);
        }
        notify.success("Address saved successfully");
        // On success take to the member details page
        app.memberDetails(this.options.member);
    },

    cancel: function () {
        // On cancel take to member details page
        app.memberDetails(this.options.member);
    },

    /**
     * Called when any key is pressed
     * @param e
     */
    onSubmitKeyPress: function (e) {
        if (event.which == 13 || e.keyCode == 13) {
            this.save();
        }
    }



//    /**
//     * Populate district, state and country
//     */
//    populateInformation: function () {
//        var city = this.$el.find("#city").val();
//        this.addresses.fetch({
//            url: '/api/cities',
//            success: this.returnSuccess,
//            data: {
//                q: city
//            }
//        });
//    },

//    returnSuccess: function () {
//        // TODO: Render auto suggest for state,country and district
//    }
});
