var SevaCategoriesHomeView = Backbone.View.extend({
    template: '#sevaCategoriesHomeTpl',

    events:{
      'click .add': 'add'
    },
    render:function(){
        var template = _.template(
            $(this.template).html()
        );

        var data = {
            length: this.collection.length
        };

        this.$el.empty().append(template(data));

        var view = new SevaCategoryCollectionTileView({
            collection: this.collection
        });

        this.$el.find('.sevaCategories thead').after(view.el);
        view.render();
    },
    add:function(){
        app.editSevaCategory();
    }
});