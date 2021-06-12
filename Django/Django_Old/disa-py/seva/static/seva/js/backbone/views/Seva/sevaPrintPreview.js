/**
 * View to show print preview of seva in the template that is passed as option
 *
 * @param {Seva} model
 * @param {string}}      templateId  Id of the template chosen for printing
 */
var SevaPrintPreviewView = ItemView.extend({
    template: '#sevaPrintPreviewTpl',
    className: 'seva-tile-print-preview',
    tagName: 'div',
    events: {
        'click .icon-remove': 'remove'
    },

    initialize: function () {
        // update the template for this view based on the template Id passed in options
        this.template = this.template + '_' + this.options.templateId;
    },

    render: function () {

        var template = _.template(
            $(this.template).html()
        );
        var data = this.model.toJSON();
        data.member=this.model.get('member').toJSON();
        data.member.addresses=this.model.get('member').get('addresses').toJSON();
        var validPrimaryAddress = this.model.get('member').getValidPrimaryAddress();
        if(validPrimaryAddress){
            data.member.validPrimaryAddress = validPrimaryAddress.toJSON();
        }

        data.member.mid=this.model.get('member').getMid();

        // To display seva date as 'date month' formate
        var sevaDate = this.model.get('sevaDate');
        sevaDate = getDateObject(sevaDate);
        data.sevaDate = sevaDate.format('j M');

        this.$el.empty().append(template(data));

//        ItemView.prototype.render.apply(this, arguments);

        this.$el.addClass(this.options.templateId);

        return this;
    },


    /**
     * Called when a document is remove from print preview
     */
    remove: function () {
        // First slide up the preview
        this.$el.slideUp("normal", function () {
            // after slide up is done. remove the element
            $(this).remove();
        });
    }

});

/**
 * @param {SevaCollection}  collection
 * @param {string}}                 templateId  Id of the template chosen for printing
 */
var SubscriptionPrintPreviewCollectionView = ItemCollectionView.extend({
    itemViewClassName: 'SevaPrintPreviewView',
    className: 'seva-tile-collection-print-preview',
    tagName: 'div',

    render: function () {
        ItemCollectionView.prototype.render.apply(this, arguments);

        this.$el.addClass(this.options.templateId);

        return this;
    }
});