var AwardTileView = ItemView.extend({
    template : '#awardTile',
    className: 'award-tile',
    tagName: 'li',

    events:{
        'click .edit-award' : 'editAward'
    },

    render: function(){
        var template= _.template(
            $(this.template).html()
        );

        var data=this.model.toJSON();
        this.$el.empty().append(template(data));
    },

    editAward : function(){
        app.editAward(this.options.member,this.model.id)
    }
});

/**
 * View to add/edit awards details of specified member
 *
 * @param {Member}   member  Member model
 * @param {AwardCollection}  Collection  Award collection
 */
var AwardTileCollectionView = ItemCollectionView.extend({
    itemViewClassName: 'AwardTileView',
    className: 'award-tile-collection'
});