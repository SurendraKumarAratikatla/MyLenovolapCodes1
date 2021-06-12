/**
 * View to show the details of the specified organisation
 *
 * @param {Organisation} model
 */
var OrganisationTileView = ItemView.extend({
    template: '#organisationTileTpl',
    className: 'organisation-tile',
    tagName: 'tr',

    events:{
        'click .edit' : 'edit'
    },

    edit:function(){
        app.editOrganisation(this.model.id);
    }
});

/**
 * @param {OrganisationCollection} collection
 */
var OrganisationCollectionView = ItemCollectionView.extend({
    itemViewClassName: 'OrganisationTileView',
    className: 'organisation-tile-collection',
    tagName: 'tbody'
});