/**
 * List Item view
 *
 * @param {Backbone.Model} model
 */
var ItemView = Backbone.View.extend({
    tagName: 'li',

    initialize: function (options) {
        _.bindAll(this);
        this.listenTo(this.model, 'change', this.change);
    },

    render: function () {
        var template = _.template(
            $(this.template).html()
        );
        var data = this.model.toJSON();
        this.$el.empty().append(template(data));
        return this;
    },

    destroy: function () {
        this.stopListening(this.model, 'change', this.change)
        Backbone.View.prototype.destroy.call(this);
    },

    change: function () {
        this.render();
    }
});

/**
 * Item list view part of the items view.
 *
 * @param {Backbone.collection} collection
 * @param {string}              [itemViewClassName="ItemView"]
 */
var ItemCollectionView = Backbone.View.extend({
    className: 'unstyled',
    tagName: 'ul',
    itemViewClassName: "ItemView",
    rendered: false,

    initialize: function () {
        _.bindAll(this);
        if (this.options.itemViewClassName) {
            this.itemViewClassName = this.options.itemViewClassName;
        }

        this.reset();

        // bind this view to the add and remove events of the collection!
        this.listenTo(this.collection, 'add', this.add);
        this.listenTo(this.collection, 'remove', this.remove);
        this.listenTo(this.collection, 'reset', this.reset);
        this.listenTo(this.collection, 'sort', this.sort);
    },

    destroy: function () {
        this.stopListening(this.collection, 'add', this.add);
        this.stopListening(this.collection, 'remove', this.remove);
        this.stopListening(this.collection, 'reset', this.reset);

        Backbone.View.prototype.destroy.call(this);
    },

    /**
     * Handles the collection "reset" event. It will empty out all existing
     * item views and re-render the entire collection.
     */
    reset: function () {
        this.$el.empty();

        this._itemViews = [];

        // add each item to the view
        this.collection.each(this.add);
    },

    add: function (model) {
        // We create an updating item view for each item that is added.
        var options = this.options || {};

        options.model = model;

        var itemView = new window[this.itemViewClassName](options);

        // And add it to the collection so that it's easy to reuse.
        this._itemViews.push(itemView);

        // If the view has been rendered, then
        // we immediately append the rendere item.
        if (this.rendered) {
            this.renderItemView(itemView);
        }
    },

    // renders  and appends to the el
    renderItemView: function (itemView) {
        this.$el.append(itemView.el);
        itemView.render();
    },

    remove: function (model) {
        var viewToRemove = this.getView(model);
        this._itemViews = _(this._itemViews).without(viewToRemove);

        if (this.rendered && viewToRemove) {
            viewToRemove.$el.remove();
        }

    },

    /**
     * Renders all the initialized views
     */
    render: function () {
        var self = this;
        this.rendered = true;

        this.$el.empty();

        // Render each sub-view and append it to the parent view's element.
        _(this._itemViews).each(function (itemView) {
            self.renderItemView(itemView);
        });

        return this;
    },

    /**
     * Changes div positions based on the sorting string.
     */
    sort: function () {
        var self = this;
        this.collection.each(function (model) {
            var view = self.getView(model);
            self.$el.append(view.el);
        });
    },

    /**
     * Returns the view associated with a model.
     *
     * @param model
     * @return {ItemView}
     */
    getView: function (model) {
        return _(this._itemViews).select(function (cv) {
            return cv.model === model;
        })[0];
    }
});
