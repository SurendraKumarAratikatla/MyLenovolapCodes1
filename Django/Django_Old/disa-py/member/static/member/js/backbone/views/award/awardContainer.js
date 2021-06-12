/**
 * View to add/edit awards details of specified member
 *
 * @param {Member}   member  Member model for which the awards is to be added / edited
 * @param {Award}  model   Award model that is to be added / edited
 */
var AwardContainerView = Backbone.View.extend({
    template: "#awardContainer",

    render: function () {
        if (this.options.member.syncing) {
            // member model is still syncing i.e. Fetch request has been made. So do not continue with render. View is already
            // listening for the model
            this.listenToOnce(this.options.member, 'sync', this.render);
            return;
        }
        if (!this.model.isNew() && this.model.syncing) {
            // Get the current award model from member. This is needed because some times, a dummy award
            // model may be sent while instantiating the view for the cases where member model is still fetching.
            this.listenToOnce(this.model, 'sync', this.render);
            return;
        }

        var template = _.template(
            $(this.template).html()
        );

        this.$el.empty().append(template());
        this.awardEditor();
        this.awardesDetails();
        return this;
    },

    /**
     * add/edit awardes details of specified member
     */
    awardEditor: function () {
        var self = this;
        var view = new AwardEditorView({
            model: this.model,
            member: this.options.member
        });
        $('.award-editor').empty().append(view.el);
        view.render();
    },

    /**
     * To display all available awardes for a specific member.
     * Called this function when award container template is rendered
     *
     * Passing member model
     */
    awardesDetails: function () {
        var data = this.options.member.get('awardes');
        var view = new AwardTileCollectionView({
            collection: data,
            member: this.options.member
        });
        this.$el.find('.award-details').append(view.el);
        view.render();

    }
});