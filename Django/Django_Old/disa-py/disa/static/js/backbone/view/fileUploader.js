var FileUploaderView = Backbone.View.extend({
    fileUploaderEl : "#fileUploaderTpl",

    init : function(){
        if(this.options.hasOwnProperty('action')){
            this.action = this.options.action;
        }
    },

    render : function(){
        var uploader = new qq.FileUploader({
            // pass the dom node (ex. $(selector)[0] for jQuery users)
            element : this.$el[0],
            // path to server-side upload script
            action : this.action,

            template : $(this.fileUploaderEl).tmpl().html()
        });
        return this;
    }
});