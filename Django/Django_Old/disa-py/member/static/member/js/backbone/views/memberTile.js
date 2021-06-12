/**
 * @param {Member} model
 *
 */
var MemberTileView = ItemView.extend({
    template: '#memberTileTpl',
    className: 'col-xs-12 col-sm-6 col-md-4',
    tagName: 'div',

    events: {
        'click .view-member': 'viewDetails',
        'click .edit-member': 'editMemberDetails'
    },

    render: function () {
//        Call the parent's render
//        ItemView.prototype.render.apply(this, arguments);

        var template = _.template(
            $(this.template).html()
        );
        var data = this.model.toJSON();
        data.mid = this.model.getMid();
        data.photo = this.model.getPhoto();

        this.$el.empty().append(template(data));
        return this;
    },

    /**
     * View member information
     */
    viewDetails: function () {
        app.memberDetails(this.model.id);
    },

    /**
     * Edit member data
     */
    editMemberDetails: function () {
        app.editMember(this.model.id);
    }

});

/**
 * @param {MemberCollection} collection
 */
var MemberTileCollectionView = ItemCollectionView.extend({
    itemViewClassName: 'MemberTileView',
    className: 'member-tile-collection section row',
    tagName: 'div'
});