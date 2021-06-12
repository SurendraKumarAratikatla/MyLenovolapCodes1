var AddressTileView = ItemView.extend({
    template : '#addressTileTpl',
    className: 'address-tile col-xs-12',
    tagName: 'div',

    events:{
        'click .edit-address' : 'editAddress'
    },

    render: function(){
        var template= _.template(
           $(this.template).html()
        );

        var data=this.model.toJSON();
        this.$el.empty().append(template(data));
    },

    editAddress : function(){
        app.editMemberAddress(this.options.member,this.model.id)
    }
});

/**
 * View to add/edit addresses details of specified member
 *
 * @param {Member}   member  Member model
 * @param {AddressCollection}  Collection  Address collection
 */
var AddressTileCollectionView = ItemCollectionView.extend({
    itemViewClassName: 'AddressTileView',
    className: 'address-tile-collection row',
    tagName: 'div'
});