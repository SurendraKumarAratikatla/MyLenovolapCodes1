/**
 * View to show the details of the specified seva
 *
 * @param {SevaCategory} model
 */
var SevaCategoryTileView = ItemView.extend({
    template: '#sevaCategoryTileTpl',
    className: 'seva-category-tile',
    tagName: 'tr',

    events:{
        'click .edit' : 'edit'
    },

    edit:function(){
        app.editSevaCategory(this.model.id);
    }
});

/**
 * @param {SevaCategoryCollection} collection
 */
var SevaCategoryCollectionTileView = ItemCollectionView.extend({
    itemViewClassName: 'SevaCategoryTileView',
    className: 'seva-tile-collection',
    tagName: 'tbody'
});