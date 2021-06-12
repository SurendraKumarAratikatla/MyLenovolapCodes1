/**
 * @param {Member} model    Member whose data is to be shown
 * @param {string} selected SevaId that is selected for highlighting
 */
var MemberDetailsContainerView = Backbone.View.extend({
    template: "#memberDetailsContainerTpl",
    className: 'member-details-main',

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
        this.$el.empty().append(template(data));
        this.renderMemberDetail();
        this.renderSevaDetails();
        return this;
    },

    renderMemberDetail: function () {
        var view = new MemberDetailsView({
            model: this.model
        });
        $('.member-details').empty().append(view.el);
        view.render();
    },

    renderSevaDetails: function () {
        var sevaCollection = this.model.get('sevas');
        var selectedSeva = sevaCollection.get(this.options.selected);
        var view = new SevaDetailsCollectionContainerView({
            collection: sevaCollection,
            member: this.model,
            selected: selectedSeva
        });
        $('.seva-details').empty().append(view.el);
        view.render();
    }
});