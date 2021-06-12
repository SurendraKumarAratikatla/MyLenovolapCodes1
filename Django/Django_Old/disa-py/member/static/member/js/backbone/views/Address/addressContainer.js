/**
 * View to add/edit addresses details of specified member
 *
 * @param {Member}   member  Member model for which the addresses is to be added / edited
 * @param {Address}  model   Address model that is to be added / edited
 */
var AddressContainerView = Backbone.View.extend({
    template: "#addressContainer",

    render: function () {
        if (this.options.member.syncing) {
            // member model is still syncing i.e. Fetch request has been made. So do not continue with render. View is already
            // listening for the model
            this.listenToOnce(this.options.member, 'sync', this.render);
            return;
        }
        if (!this.model.isNew()) {
            // Get the current address model from member. This is needed because some times, a dummy address
            // model may be sent while instantiating the view for the cases where member model is still fetching.
            this.model = this.options.member.get('addresses').get(this.model.id);
        }

        var template = _.template(
            $(this.template).html()
        );

        this.$el.empty().append(template());
        this.addressEditor();
        this.addressesDetails();
        return this;
    },

    /**
     * add/edit addresses details of specified member
     */
    addressEditor: function () {
        var self = this;
        var view = new AddressEditorView({
            model: this.model,
            member: this.options.member
        });
        $('.address-editor').empty().append(view.el);
        view.render();
    },

    /**
     * To display all available addresses for a specific member.
     * Called this function when address container template is rendered
     *
     * Passing member model
     */
    addressesDetails: function () {
        var data = this.options.member.get('addresses');
        var view = new AddressTileCollectionView({
            collection: data,
            member: this.options.member
        });
        this.$el.find('.address-details').append(view.el);
        view.render();

    }
});