/**
 * @param {SevaCollection}  collection  List of sevas that needs to shown
 * @param {Member}          model       Member to which the sevas belong
 * @param {Seva}            selected    Selected seva that needs to be highlighted
 */
var SevaDetailsCollectionContainerView = Backbone.View.extend({
    template: '#sevaDetailsCollectionTpl',

    events: {
        'click .add-seva': 'addSeva'
    },
    render: function () {
        var template = _.template(
            $(this.template).html()
        );
        this.$el.empty().append(template());

        var view = new SevaDetailsTileCollectionView({
            collection: this.collection,
            member: this.options.member,
            selected: this.options.selected
        });
        this.$el.find('.seva-details').append(view.el);
        view.render();
        return this;
    },

    /**
     * Add new seva for the member
     */
    addSeva: function () {
        app.addSeva(this.options.member);
    }
});