var MemberSummaryTileView = Backbone.View.extend({
    template: "#memberSummaryTileTpl",

    events: {
        'click .view-member': 'viewMember'
    },

    render: function () {
        var template = _.template(
            $(this.template).html()
        );

        var data = this.model.toJSON();

        data.mid = this.model.getMid();
        data.photo = this.model.getPhoto();

        this.$el.empty().append(template(data));
        return this;
    },

    viewMember: function () {
        app.memberDetails(this.model);
    }
});