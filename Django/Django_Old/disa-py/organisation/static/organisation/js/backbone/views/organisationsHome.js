var OrganisationsHomeView = Backbone.View.extend({
    template: '#organisationsHomeTpl',

    events:{
        'click .add' : 'add'
    },
    render: function () {
        var template = _.template(
            $(this.template).html()
        );
        this.$el.empty().append(template());

        var view = new OrganisationCollectionView({
            collection: this.collection
        });
        this.$el.find('.organisations').append(view.el);
        view.render();
        return this;
    },

    add: function(){
        app.editOrganisation();
    }
});