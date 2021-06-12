/**
 * View to show the seva details in sevas home page
 *
 * @param {Seva}
 */
var SevaTileView = ItemView.extend({
    template: '#sevaTileTpl',
    className: 'seva-tile',
    tagName: 'tr',
    events: {
        'click': 'onClick',
        'change [name="print-subscription"]': 'selectForPrint',
        'click .details': 'details',
        'click .member-details': 'memberDetails',
        'click .edit': 'editSevaDetails'
    },

    render: function () {
        var template = _.template(
            $(this.template).html()
        );
        var data = this.model.toJSON();

        try {
            data.member = data["member"].toJSON();
            data.member.addresses = data.member["addresses"].toJSON();
        } catch (error) {
            data.member = data["member"];
            data.member.addresses = data.member["addresses"];
        }

        data.member.mid = this.model.get('member').getMid();
        data.member.photo=this.model.get('member').getPhoto();

        var sevaDate = this.model.get('sevaDate');
        sevaDate = getDateObject(sevaDate);
        data.sevaDate = sevaDate.format('j M');
        this.$el.empty().append(template({data: data}));

        // Highlight the current view if already in print list
        if (_.indexOf(app.printDetails.list, this.model.id) >= 0) {
            this.$el.addClass('highlight');
        }

        // This view got rendered. Stop listening to changes on the model.
        this.stopListening(this.model);
        return this;
    },

    /**
     * Called when seva tile is clicked
     */
    onClick: function () {
        // Seva tile was clicked

        if (!this.$el.hasClass('highlight')) {
            // This seva is checked for print. Add id to the print list
            app.printDetails.list.push(this.model.id);
            this.$el.addClass('highlight');
        }
        else {
            // This seva is unchecked for print. Remove it from the print list
            app.printDetails.list = _.without(app.printDetails.list, [this.model.id]);
            this.$el.removeClass('highlight');
        }
    },

    // To show seva details
    details: function () {
        app.sevaDetails(this.model.id);
    },

    // To edit seva details
    editSevaDetails: function () {
        app.editSeva(this.model.id);
    },

    /**
     * Go to member details page
     */
    memberDetails: function () {
        app.memberDetails(this.model.get('member'));
    }

});

/**
 * Collection view for seva tiles shown in sevas home page
 *
 * @param {SevaCollection}
 */
var SevaTileCollectionView = ItemCollectionView.extend({
    itemViewClassName: 'SevaTileView',
    className: 'seva-tile-collection',
    tagName: 'tbody'
});