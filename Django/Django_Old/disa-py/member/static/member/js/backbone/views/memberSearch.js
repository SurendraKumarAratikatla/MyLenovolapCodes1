/**
 * View to show the members home page
 *
 * @param {MemberCollection} collection
 */
var MemberSearchView = Backbone.View.extend({
    template: '#memberSearchTpl',

    events: {
        'input [type="text"]': 'onKeyUpSearch',
        'click .btn-search': 'search',
        'click .add-member': 'addMember',
        'click [type="radio"]': 'handleSearchOptionChange',
        'keydown [type="text"]': 'onSubmitKeyPress',
        'click .member-create': 'onClickMemberCreate',
        'click .btn-search-reset': "onClickReset"
    },

    initialize: function () {
        _.bindAll(this);
    },

    render: function () {
        var template = _.template(
            $(this.template).html()
        );
        var data = {
            length: this.collection.length
        };
        this.$el.empty().append(template(data));
        this.renderMembers();
    },

    renderMembers: function () {
        var view = new MemberTileCollectionView({
            collection: this.collection
        });
        this.$el.find('.search-results-members').append(view.el);
        view.render();
    },

    /**
     * Called when reset button is clicked
     */
    onClickReset: function () {
        this.$el.find('input[type="text"]').val("");
    },

    /**
     * Called while search term is being entered
     * Triggers search on timeout
     */
    onKeyUpSearch: function () {
        clearTimeout(this.timer);
        var self = this;
        this.timer = setTimeout(function () {
            self.search();
        }, 500);
    },

    /**
     * Called when create member link is clicked in advance search option
     */
    onClickMemberCreate: function () {
        var attrs = this.getAttrs();
        var member = new Member();
        var errors = member.validate(attrs);
        if (!_.isEmpty(errors)) {
            this.renderErrors(errors);
            return;
        }
        member.save(attrs, {
            success: this.memberCreateSuccess,
            error: this.errorHandler
        });
    },

    /**
     * Called when create member is success. Adds model to the existing collection.
     *
     * @param {Member} model
     */
    memberCreateSuccess: function (model) {
        this.collection.add(model, {'at': 0});
        notify.success('Member created successfully');
    },

    /**
     * Get attributes from the advanced search from. They are essentially the member details by which
     * search was made.
     *
     * @returns {{}}
     */
    getAttrs: function () {
        var attrs = {};
        attrs.name = $.trim(this.$el.find('input[name="name"]').val());
        attrs.surname = $.trim(this.$el.find('input[name="surname"]').val());
        attrs.place = $.trim(this.$el.find('input[name="place"]').val());
        attrs.email = $.trim(this.$el.find('input[name="email"]').val());
        attrs.phone = $.trim(this.$el.find('input[name="phone"]').val());
        attrs.mobile = $.trim(this.$el.find('input[name="mobile"]').val());

        return attrs;
    },


    /**
     * Search member information based on search key.
     */
    search: function () {
        var searchBy = this.$el.find('input[name="searchBy"]:checked').val();
        var searchKey = null;
        var data = {};

        if (searchBy == 'advanced') {
            // Advanced search
            data['name'] = this.$el.find('input[name="name"]').val();
            data['place'] = this.$el.find('input[name="place"]').val();
            data['email'] = this.$el.find('input[name="email"]').val();
            data['surname'] = this.$el.find('input[name="surname"]').val();
            data['mobile'] = this.$el.find('input[name="mobile"]').val();
            data['phone'] = this.$el.find('input[name="phone"]').val();

        } else if (searchBy == "mid") {
            // Search by mid. Replace all leading non-digits with nothing
            searchKey = $.trim(this.$el.find('input[name="search"]').val());
            data['mid'] = searchKey.replace(/^\D+/g, '');

        } else {
            // Search by Name.
            searchKey = $.trim(this.$el.find('input[name="search"]').val());
            if (searchKey.length <= 3) {
                // If searched by name, string should be at least 2 chars to avoid large result set
                return;
            }

            data['q'] = searchKey;
        }

        this.collection.fetch({
            success: this.searchSuccess,
            data: data,
            reset: true
        });

        this.$el.find('.btn-search-wrapper').addClass('searching');

    },

    /**
     * Called when search happens successfully
     * Hides not found message and show the message with result count
     */
    searchSuccess: function () {
        this.$el.find('.search-results').removeClass('hidden');
        this.$el.find('.btn-search-wrapper').removeClass('searching');
        var len = this.collection.length;
        this.$el.find('.result-count-value').text(len);
    },

    addMember: function () {
        app.editMember()
    },

    /**
     * Providing search option based on the search type
     */
    handleSearchOptionChange: function () {
        var searchBy = this.$el.find('input[name="searchBy"]:checked').val();

        // Providing search options based on the search type
        if (searchBy == 'mid' || searchBy == 'all') {
            if (!this.$el.find('#advanced').hasClass('hidden')) {
                this.$el.find('#advanced').addClass('hidden');
            }
            if (this.$el.find('#searchBar').hasClass('hidden')) {
                this.$el.find('#searchBar').removeClass('hidden');
            }
            // To change place holder
            if (searchBy == 'mid') {
                this.$el.find('[name="search"]').attr("placeholder", "Member Id e.g. MID#001, MID#101");
            } else {
                this.$el.find('[name="search"]').attr("placeholder", "Name, Surname, Place, E-Mail, Phone");
            }
        } else {
            if (this.$el.find('#advanced').hasClass('hidden')) {
                this.$el.find('#advanced').removeClass('hidden');
            }
            if (!this.$el.find('#searchBar').hasClass('hidden')) {
                this.$el.find('#searchBar').addClass('hidden');
            }
        }
    },

    /**
     * Called when any key is pressed
     * @param e
     */
    onSubmitKeyPress: function (e) {
        if (event.which == 13 || e.keyCode == 13) {
            this.search();
        }
    }
});
