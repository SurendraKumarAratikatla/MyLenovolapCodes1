var MemberDetailsView = Backbone.View.extend({
    template: '#memberDetailsTpl',
    rendered: false,

    initialize: function (options) {
        _.bindAll(this);
    },

    events: {
        'click .see-more': 'seeMore',
        'click .edit-member': 'editMember',
        'click .add-address': 'addAddress'
    },

    render: function () {
        var template = _.template(
            $(this.template).html()
        );

        // Populate the data object with the model's data if available
        var data = this.model ? this.model.toJSON() : {};

        // Include this view's ID so that we can create unique element IDs
        data.cid = this.cid;

        if (!data.nakshatram) {
            data.nakshatram = null;
        }

        data.mid = this.model.getMid();
        data.photo = this.model.getPhoto();
        data.id = this.model.id;

        this.$el.empty().append(template(data));

        if (!this.rendered) {
            this.rendered = true;
            this.listenTo(this.model, 'change', this.render);
        }
        this.renderMemberAddresses();
        this.renderUploader();
        return this;
    },

    renderUploader: function () {

        var self = this;
        var uploader = new qq.BpFileUploader({
            // pass the dom node (ex. $(selector)[0] for jQuery users)
            element: document.getElementById('file-uploader-' + this.cid),
            // path to server-side upload script
            action: this.model.url() + '/photo',
            onComplete: self.uploadComplete,

            hoverClass: 'btn',
            multiple: false

        });
    },

    uploadComplete: function (id, filename, response) {
        if (response.success) {
            var curTime = new Date().getTime();
            this.model.set('photo', response.success + '?' + curTime);
        }
    },

    seeMore: function () {
        this.$el.find('.see-more-content').toggle();
    },

    editMember: function () {
        app.editMember(this.model);
    },

    /**
     * render member addresses
     */
    renderMemberAddresses: function () {
        var addressCollection = this.model.get('addresses');
        if (!addressCollection) {
            addressCollection = new AddressCollection();
            this.model.set('addresses', addressCollection);
        }
        var view = new AddressTileCollectionView({
            collection: addressCollection,
            member: this.model
        });
        this.$el.find('.member-addresses').append(view.el);
        view.render();
    },

    /**
     * For add new address for an existing member
     */
    addAddress: function () {
        app.editMemberAddress(this.model, 'new');
    }
});