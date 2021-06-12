/**
 * View to render details of seva in MemberDetails page or sevaDetails page
 *
 * @param {Seva}    model       Seva that is to be rendered, whose details are to be shown
 * @param {Member}  member      Member model to which these sevas belong
 * @param {Seva}    [selected]  Optionally, a selected seva can be passed. If passed, this view highlights the seva,
 *                              if the current seva being rendered matches with the selected seva
 */
var SevaDetailsTileView = ItemView.extend({
    template: '#sevaDetailsTileTpl',
    className: 'seva-details-tile col-xs-12',
    tagName: 'div',

    events: {
        'click .edit-seva': 'editSeva'
    },

    render: function () {
        var template = _.template(
            $(this.template).html()
        );
        var data = this.model.toJSON();
        data.memberName = this.options.member.getFullName();
        if (data.startDate) {
            // If start Date is valid
            var sevaStartDate = new Date(data.startDate);
            var endDate;
            if (data.endDate) {
                // if end date is valid
                endDate = new Date(data.endDate);
            }
            data.startDate = sevaStartDate.toString('MMMM d, yyyy');

            var recurrence = data.sevaCategory.recurrence;

            data.sevaDateSummary = this.model.sevaSummary(sevaStartDate, endDate, recurrence);
        }
        this.$el.empty().append(template(data));

        if (this.options.selected) {
            if (this.model.id == this.options.selected.id) {
                // Current seva model is the one that was selected
                // Add a class that highlights this seva
                this.$el.find('.seva-tile').addClass('bg-info');
                // Move this element to the top of the list.
                this.$el.prependTo(this.$el.parent());
            }
        }

        return this;
    },

    /**
     * Edit seva
     */
    editSeva: function () {
        app.editSeva(this.model);
    }

//    /**
//     * Set the seva date formate like (d MonthName (20 September))
//     *
//     * @param sevaDate
//     * @returns {string}
//     */
//    sevaDateFormate: function (sevaDate) {
//        var sevaDate = new Date(sevaDate);
//
//        var month = new Array();
//        month[0] = "January";
//        month[1] = "February";
//        month[2] = "March";
//        month[3] = "April";
//        month[4] = "May";
//        month[5] = "June";
//        month[6] = "July";
//        month[7] = "August";
//        month[8] = "September";
//        month[9] = "October";
//        month[10] = "November";
//        month[11] = "December";
//
//        var monthName = month[sevaDate.getMonth()];
//        return sevaDate = new Date(sevaDate).format('d') + ' ' + monthName;
//    }
});

/**
 * View to show collection of seva details in MemberDetails page
 *
 * @param {SevaCollection}  collection  List of sevas that needs to shown
 * @param {Member}          model       Member to which the sevas belong
 * @param {Seva}            selected    Selected seva that needs to be highlighted
 */
var SevaDetailsTileCollectionView = ItemCollectionView.extend({
    itemViewClassName: 'SevaDetailsTileView',
    className: 'seva-collection row',
    tagName: 'div'
});