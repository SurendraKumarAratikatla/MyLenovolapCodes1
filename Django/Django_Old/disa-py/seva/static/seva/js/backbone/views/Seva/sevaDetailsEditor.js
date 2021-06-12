/**
 * View to add/edit seva details of specified member
 *
 * @param {Member}        member  Member model for which the seva is to be added / edited
 * @param {Seva}  model   Seva model that is to be added / edited
 */
var SevaDetailsEditorView = FormView.extend({
    template: '#sevaDetailsEditorTpl',

    events: {
        'change [name=organisation]': 'handleOrganisationChange',
        'click [name=inTheNameOf]': 'type',
        'click [type="submit"]': 'save',
        'click .cancel': 'cancel',
        'change [name=sevaCategory]': 'handleSevaCategoryChange',
        'change [name=sevaCategory]': 'handleSevaSummary',
        'click [name=transactionType]': 'handleTransactionTypeChange',
        'blur [name=amountPay]': 'calculateDauAmount',
        'click #sponsor-item-option': 'handleSponsorItem',
        'change [name=startDateInput]' : 'handleSevaSummary'
    },

    render: function () {
        if (this.model.syncing) {
            this.listenToOnce(this.model, 'sync', this.render);
            return;
        }

        if (this.options.member) {
            if (this.options.member.syncing) {
                this.listenToOnce(this.options.member, 'sync', this.render);
                return;
            }
        }
        else if (this.model.get('member')) {
            this.options.member = this.model.get('member');
        }

        var template = _.template(
            $(this.template).html()
        );

        data = this.model.toJSON();

        // Get nakshatram value. Check the type of the nakshatram weather it is a string or an object.
        // If it is an object then convert that object into string format and set it to the data object
        if (data['nakshatram']) {
            if ($.type(data['nakshatram']) == 'object') {
                // Convert javascript object to json
                var nakshatram = JSON.stringify(data['nakshatram']);
                var parsedJSON = eval('(' + nakshatram + ')');
                // Getting nakshatram string and set it to data object
                data.nakshatram = parsedJSON.nakshatram;
            }
        }

        data.member = this.options.member.toJSON();
        data.sevaCategoryColl = app.sevaCategoryCollection.toJSON();
        data.nakshatramColl = app.nakshatramCollection.toJSON();
        data.organisationColl = app.organisationCollection.toJSON();

        // pass the data in a another data wrapper
        this.$el.empty().append(template({data: data}));
        this.initDatePicker();
        this.memberSummary(this.options.member);
        // If seva day is available then set seva date in text field
        if (data.id) {
            var date = data['sevaDay'];
            this.setDate(date);

            var startDate = this.model.get('startDate');
//            var endDate = this.model.get('endDate');
            if(startDate){
                this.setStartDate(startDate);
            }
//            if(endDate){
//                this.setEndDate(endDate);
//            }
        }
        // If id is available then call the function to add class 'hide' to sevaAddress block
        if (!this.model.id) {
            this.sevaAddressHandler();
        }

        return this;
    },

    initDatePicker: function () {
        // initialise date picker for seva date
        this.$el.find("input[name='sevaDateInput']").datepicker({
            dateFormat: "d MM, yy",
            altFormat: "yy-mm-dd",
            changeMonth: true,
            changeYear: true,
            altField: "input[name='sevaDate']"
        });

        this.$el.find("input[name='startDateInput']").datepicker({
            dateFormat: "d MM, yy",
            altFormat: "yy-mm-dd",
            changeMonth: true,
            changeYear: true,
            altField: "input[name='startDate']"
        });

        // pre-select date
        this.$el.find("input[name='sevaDateInput']").datepicker("setDate", new Date());
        this.$el.find("input[name='startDateInput']").datepicker("setDate", new Date());

        // Calculating next date( end date ). adding days to start date
        Date.prototype.addDays = function(days,dateObj) {
            dateObj.setDate(this.getDate() + days);
            return dateObj;
        };
    },

    /**
     * Called while rendering the seva editor template
     * If seva inTheNameOf is donor then add class 'hide' to sevaAddress block
     */
    sevaAddressHandler: function () {
        var type = this.$el.find("input:radio[name='inTheNameOf']:checked").val();
        if (type == 'donor') {
            this.$el.find(".seva-address").addClass("hide");
        }
    },

    /**
     * @param date  Passing date string to change format
     */
    setDate: function (date) {
        var day = date.substr(2, 2);
        var month = date.substr(0, 2);
        var dateObj = new Date();
        var year = dateObj.getFullYear();
        var formattedDate = year + '-' + month + '-' + day;
        this.$el.find("input[name='sevaDateInput']").datepicker("setDate", getDateObject(formattedDate));
    },

    setStartDate : function (startDate) {
        startDate = startDate.date;
        startDate = new Date(startDate);
        var day = startDate.getDate();
        var month = startDate.getMonth()+1;
        var year = startDate.getFullYear();
        var formattedDate = year + '-' + month + '-' + day;
        this.$el.find("input[name='startDateInput']").datepicker("setDate", getDateObject(formattedDate));
    },

//    setEndDate : function (endDate) {
//        endDate = endDate.date;
//        endDate = new Date(endDate);
//        this.$el.find("input[name='endDateInput']").val('').val(endDate.format('d M, Y'));
//        this.$el.find("input[name='endDate']").val('').val(endDate.format('Y-m-d'));
//    },

    /**
     * @param {Member} model    Member model for display member summary information
     */
    memberSummary: function (model) {
        var view = new MemberSummaryTileView({
            model: model
        });
        $('.member-summary').empty().append(view.el);
        view.render();
    },

    /**
     * If Donor then disable Name & gotram but enable gotram if it is null
     * If Other then enable Name & gotram by clearing both the fields
     */
    type: function () {
        var type = this.$el.find("input:radio[name='inTheNameOf']:checked").val();

        if (type == 'donor') {
            this.inTheNameOfOtherData = {
                name: this.$el.find("input[name='name']").val(),
                gotram: this.$el.find("input[name='gotram']").val(),
                nakshatram: this.$el.find('select[name="nakshatram"]').val()
            };

            this.$el.find("input[name='name']").val(this.options.member.get("name"));
            this.$el.find("input[name='gotram']").val(this.options.member.get("gotram"));
            this.$el.find("select[name='nakshatram']").val(this.options.member.get("nakshatram"));

            this.$el.find("input[name='name']").prop('disabled', true);
            this.$el.find("input[name='gotram']").prop('disabled', true);
            this.$el.find("select[name='nakshatram']").prop('disabled', true);

            // If seva in the name of is other then hide the seva address block
            this.$el.find(".seva-address").addClass("hide");

        } else {
            // If inTheNameOf is other then show the seva address block
            this.$el.find(".seva-address").removeClass("hide");

            var sevaName = this.inTheNameOfOtherData.name || "";
            var sevaGotram = this.inTheNameOfOtherData.gotram || "";
            var sevaNakshatram = this.inTheNameOfOtherData.nakshatram || "";
            this.inTheNameOfOtherData = {};

            this.$el.find("input[name='name']").val(sevaName);
            this.$el.find("input[name='gotram']").val(sevaGotram);
            this.$el.find("select[name='nakshatram']").val(sevaNakshatram);

            this.$el.find("input[name='name']").prop('disabled', false);
            this.$el.find("input[name='gotram']").prop('disabled', false);
            this.$el.find("select[name='nakshatram']").prop('disabled', false);

            this.$el.find("input[name='name']").focus();
        }
    },

    /**
     * Called when organisation value gets changed.
     * Populate available seva categories along with locations list in seva vategories drop down for the selected organisation.
     */
    handleOrganisationChange: function () {
        var sevaCategories = app.sevaCategoryCollection.toJSON();

        var orgId = $.trim(this.$el.find('select[name="organisation"]').val());

        var options = this.$el.find('select[name="sevaCategory"]');
        options.empty();
        options.append($("<option />").val("").text("--Select--"));
        $.each(sevaCategories, function (i) {
            if (sevaCategories[i].oid == orgId) {
                options.append($("<option />").val(sevaCategories[i].id).text(sevaCategories[i].location + " --> " + sevaCategories[i].name));
            }
        });
    },

    handleSevaCategoryChange: function () {
        var sevacategoryId = $.trim(this.$el.find('select[name="sevaCategory"]').val());
        var sevaCategory = app.sevaCategoryCollection.get(sevacategoryId);
        sevaCategory = sevaCategory.toJSON();
        var amount = sevaCategory.amount;

        this.$el.find('input[name="totalAmount"]').val(amount);

        // Populating sponsor item type
        var sponsorItemType = sevaCategory.sponsorItemType;
        if(sponsorItemType){
            this.$el.find('input[name="itemType"]').val('').val(sponsorItemType);
        }
    },

    handleTransactionTypeChange: function () {
        var transactionType = this.$el.find('input:radio[name="transactionType"]:checked').val();
        if (transactionType == "check") {
            if (this.$el.find(".check-number").hasClass("hide")) {
                this.$el.find(".check-number").removeClass("hide");
            }
        } else {
            if (!this.$el.find(".check-number").hasClass("hide")) {
                this.$el.find(".check-number").addClass("hide");
            }
        }
    },

    /**
     * To get all form field attributes
     */
    getAttrs: function () {
        var attrs = {};
        attrs.member = this.options.member.id;
        attrs.organisation = this.$el.find('select[name="organisation"]').val();
        attrs.sevaCategory = this.$el.find('select[name="sevaCategory"]').val();
        attrs.sevaDate = $.trim(this.$el.find('input[name="sevaDate"]').val());
        attrs.occasion = $.trim(this.$el.find('input[name="occasion"]').val());

        attrs.gotram = $.trim(this.$el.find('input[name="gotram"]').val());
        attrs.nakshatram = this.$el.find('select[name="nakshatram"]').val();

        attrs.startDate = $.trim(this.$el.find('input[name="startDate"]').val());
//        attrs.endDate = this.$el.find('input[name="endDate"]').val();
//        attrs.frequency = this.$el.find('select[name="frequency"]').val();
//        attrs.frequencyValue = this.$el.find('input[name="frequencyValue"]').val();

        var type = this.$el.find('input:radio[name=inTheNameOf]:checked').val();
        var name = $.trim(this.$el.find('input[name="name"]').val());
        if (type == 'donor') {
            attrs.inTheNameOf = type;
        } else if (type == 'other') {
            attrs.inTheNameOf = name;

            attrs.address = {};
            attrs.address.address = $.trim(this.$el.find('textarea[name="address"]').val());
            attrs.address.city = $.trim(this.$el.find('input[name="city"]').val());
            attrs.address.district = $.trim(this.$el.find('input[name="district"]').val());
            attrs.address.state = $.trim(this.$el.find('input[name="state"]').val());
            attrs.address.country = $.trim(this.$el.find('input[name="country"]').val());
            attrs.address.pin = $.trim(this.$el.find('input[name="pin"]').val());
            attrs.address.phone = $.trim(this.$el.find('input[name="phone"]').val());
            var isValid = this.$el.find('input:checkbox[name=valid]:checked').val();
            if(isValid){
                attrs.address.isValid = true;
            }else{
                attrs.address.isValid = false;
            }
        }

        // Sponsor item properties
        var sponsorItemOption = (this.$el.find('input[name="sponsorItemOption"]')) ?
            this.$el.find('input[name="sponsorItemOption"]').val() : false;
        attrs.sponsorItemOption = false;
        if(sponsorItemOption){
            attrs.sponsorItemOption = true;
            attrs.sponsorItem = {};
            attrs.sponsorItem.name = $.trim(this.$el.find('input[name="itemName"]').val());
            attrs.sponsorItem.code = $.trim(this.$el.find('input[name="itemCode"]').val());
            attrs.sponsorItem.type = $.trim(this.$el.find('input[name="itemType"]').val());
            attrs.sponsorItem.amount = $.trim(this.$el.find('input[name="itemAmount"]').val());
            attrs.sponsorItem.description = $.trim(this.$el.find('input[name="itemDescription"]').val());
        }

        return attrs;
    },

    save: function () {
        var attrs = this.getAttrs();
        this.model.save(attrs, {
            success: this.success,
            error: this.errorHandler,
            patch: true
        });
    },

    success: function () {
        notify.success('Seva details saved successfully');
        if (this.options.success) {
            // success callback is specified. Call the callback function
            this.options.success.apply(this, arguments);
        }
        else {
            // no callback specified
            app.sevaDetails(this.model);
        }
    },

    cancel: function () {
        if (this.options.cancel) {
            // cancel callback is specified. Call the callback function
            this.options.cancel();
        }
        else {
            // no callback specified. Take to the seva details page
            app.sevaDetails(this.model);
        }
    },

    calculateDauAmount: function () {
        var totalAmount = this.$el.find('input[name="totalAmount"]').val();
        var amountPay = this.$el.find('input[name="amountPay"]').val();
        if (isNaN(amountPay)) {
            alert("It accept only numbers");
        } else {
            if (totalAmount != "" && totalAmount > 0) {
                if (amountPay != null && amountPay >= 0) {
                    var dauAmount = totalAmount - amountPay;
                    this.$el.find('input[name="amountDau"]').val(dauAmount);
                }
            }
        }
    },

    /**
     * Handle sponsor item properties.
     * Adding values to hidden property and displaying sponsor item block based on the condition
     */
    handleSponsorItem: function() {
        if(this.$el.find(".sponsor-item-properties").hasClass('hide')){
            this.$el.find(".sponsor-item-properties").removeClass('hide');
            this.$el.find(".sponsor-item-properties").addClass('show');
            this.$el.find('input[name="sponsorItemOption"]').val('').val(true);
        }else{
            this.$el.find(".sponsor-item-properties").removeClass('show');
            this.$el.find(".sponsor-item-properties").addClass('hide');
            this.$el.find('input[name="sponsorItemOption"]').val('').val(false);
        }
    },

    /**
     * Displaying seva summary
     */
    handleSevaSummary : function (){
        var sevaCategoryId = this.$el.find('select[name="sevaCategory"]').val();
        var summary = 'please select seva category for seva summary';
        if(sevaCategoryId){
            var startDate = this.$el.find('input[name="startDate"]').val();
            var sevaCategory = app.sevaCategoryCollection.get(sevaCategoryId);
            sevaCategory = sevaCategory.toJSON();
            var recurrence = sevaCategory.recurrence;
            var endDate = this.model.calculateEndDate(new Date(startDate), sevaCategory.durationType, sevaCategory.duration);
            summary = this.model.sevaSummary(new Date(startDate), endDate, recurrence);
        }

        this.$el.find('#seva_date_summary').html('').html(summary);
    }

});