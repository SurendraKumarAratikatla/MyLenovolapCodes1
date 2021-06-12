var ResourceNotFoundView = Backbone.View.extend({
	template: "#resourceNotFoundTpl",

	render: function() {
        $(this.el).append($(this.template).tmpl());
		return this;
	}
});
