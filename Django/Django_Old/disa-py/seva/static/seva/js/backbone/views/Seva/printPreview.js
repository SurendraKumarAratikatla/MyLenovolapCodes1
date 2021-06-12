/**
 * View to show the print preview for the selected print template
 *
 * @param {SevaCollection} collection
 * @param {string}                 templateId   Id of the template that is selected for print
 */
var PrintPreviewView = Backbone.View.extend({
    template: '#printPreviewTpl',
    events: {
        'click [name="print"]': 'print',
        'click [name="back"]': 'back'
    },

    render: function () {
        var template = _.template(
            $(this.template).html()
        );

        var data = {
            templateId: this.options.templateId
        };

        this.$el.empty().append(template(data));

        var view = new SubscriptionPrintPreviewCollectionView({
            collection: this.collection,
            templateId: this.options.templateId
        });

        this.$el.append(view.el);
        view.render();
    },

    /**
     * Called when print button is clicked
     */
    print: function () {
        window.print();
        //todo: use routes
        var currentUrl=window.location.href;
        document.location.href = currentUrl;
    },

    back: function () {
        app.sevasHome();
    }


});