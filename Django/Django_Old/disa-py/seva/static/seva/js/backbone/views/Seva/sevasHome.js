/**
 * Main view to show the sevas home page
 *
 * @param {SevaCollection} collection
 */
var SevasHomeView = Backbone.View.extend({
    template: '#sevasHomeTpl',

    events: {
        'click [name="print"]': 'print',
        'click [name="print-seva-all"]': 'selectAllForPrint',
        'click [name="dateRange"]': 'filter',
        'change [name="orderedBy"]': 'orderedBy',
        'click .place-sort': 'sortByPlace',
        'click .name-sort': 'sortByName'
    },

    render: function () {
        var template = _.template(
            $(this.template).html()
        );

        var data = {
            length: this.collection.length,
            all: app.printDetails.all,
            templateId: app.printDetails.templateId,
            sevaCategoriesColl: app.sevaCategoryCollection.toJSON(),
            sevaCategoryId: app.sevaCategoryId
        };

        this.$el.empty().append(template(data));

        var view = new SevaTileCollectionView({
            collection: this.collection
        });

        this.$el.find('.sevas thead').after(view.el);

        view.render();
        this.initDatePicker();
    },

    initDatePicker: function () {
        // initialise date picker for registration date
        this.$el.find("input[name='fromDate-input']").datepicker({
            dateFormat: "d MM, yy",
            altFormat: "yy-mm-dd",
            altField: "input[name='fromDate']",
            onClose: function (selectedDate) {
                $('input[name="toDate-input"]').datepicker("option", "minDate", selectedDate);
            }
        });

        var self = this;
        // open calendar on click of icon
        this.$el.find('input[name="fromDate-input"] + span').on('click', function () {
            self.$el.find("input[name='fromDate-input']").datepicker('show');
        });

        this.$el.find("input[name='toDate-input']").datepicker({
            dateFormat: "d MM, yy",
            altFormat: "yy-mm-dd",
            altField: "input[name='toDate']",
            onClose: function (selectedDate) {
                $('input[name="fromDate-input"]').datepicker("option", "maxDate", selectedDate);
            }
        });

        // open calendar on click of icon
        this.$el.find('input[name="toDate-input"] + span').on('click', function () {
            self.$el.find("input[name='toDate-input']").datepicker('show');
        });

        // pre-select from and to seva dates
        var sevaDates = app.sevaDate.split(",");
        if (sevaDates.length == 1) {
            sevaDates[1] = sevaDates[0];
        }


        // pre-select from date
        this.$el.find("input[name='fromDate-input']").datepicker("setDate", getDateObject(sevaDates[0]));
        this.$el.find("input[name='toDate-input']").datepicker("setDate", getDateObject(sevaDates[1]));
    },


    /**
     * Called when print button is clicked
     */
    print: function () {
        var templateId = this.$el.find('[name="print-template-list"]').val()
        if (!templateId) {
            notify.error('Choose template for printing');
            return;
        }
        if (app.printDetails.list.length == 0) {
            // No seva was selected for print
            notify.error('Select sevas for printing');
            return;
        }
        app.printDetails.templateId = templateId;
        app.print();

    },

    /**
     * Method to select all the sevas in the page for printing
     */
    selectAllForPrint: function () {
        if (this.$el.find('[name="print-seva-all"]').is(':checked')) {
            // Print all is checked. Add all sevas to it. Empty the list so as to avoid duplicates
            app.printDetails.all = true;
            app.printDetails.list = [];
            this.collection.each(function (seva) {
                app.printDetails.list.push(seva.id);
            });

            // add highlight class to all the sevas
            this.$el.find('tr').addClass('highlight');
        }
        else {
            // Print all is unchecked, empty the list
            app.printDetails.all = false;
            app.printDetails.list = [];
            // remove highlight for all sevas
            this.$el.find('tr').removeClass('highlight');
        }
    },

    /**
     * Method to post date range to get sevas based on filtered criteria
     */
    filter: function () {
        var fromDate = $('input[name=fromDate]').val();
        var toDate = $('input[name=toDate]').val();
        var scId = $('select[name=sevaCategory]').val();
        //todo: use routes instead of hard coding url
        if(scId!=""){
            window.location.href = "/admin/sevas?scId="+scId+"&sevaDate=" + fromDate + ',' + toDate;
        }else{
            window.location.href = "/admin/sevas?sevaDate=" + fromDate + ',' + toDate;
        }
    },

    orderedBy: function (e) {
        var sortVal = $(e.currentTarget).val();
        var collections = this.collection;

        switch (sortVal) {
            case "nameAtoZ" :
                // sub1 indicates seva modal one and sub2 indicates seva modal 2
                collections.comparator = function (sub1, sub2) {
                    if (sub1.get("member").get("name") < sub2.get("member").get("name")) {
                        return -1;
                    } else if (sub1.get("member").get("name") > sub2.get("member").get("name")) {
                        return 1;
                    } else {
                        return 0;
                    }
                };
                break;
            case "nameZtoA" :
                // sub1 indicates seva modal one and sub2 indicates seva modal 2
                collections.comparator = function (sub1, sub2) {
                    if (sub1.get("member").get("name") < sub2.get("member").get("name")) {
                        return 1;
                    } else if (sub1.get("member").get("name") > sub2.get("member").get("name")) {
                        return -1;
                    } else {
                        return 0;
                    }
                };
                break;
            case "placeAtoZ" :
                // sub1 indicates seva modal one and sub2 indicates seva modal 2
                collections.comparator = function (sub1, sub2) {
                    if (sub1.get("member").get("place") < sub2.get("member").get("place")) {
                        return -1;
                    } else if (sub1.get("member").get("place") > sub2.get("member").get("place")) {
                        return 1;
                    } else {
                        return 0;
                    }
                }
                break;
            case "placeZtoA" :
                // sub1 indicates seva modal one and sub2 indicates seva modal 2
                collections.comparator = function (sub1, sub2) {
                    if (sub1.get("member").get("place") < sub2.get("member").get("place")) {
                        return 1;
                    } else if (sub1.get("member").get("place") > sub2.get("member").get("place")) {
                        return -1;
                    } else {
                        return 0;
                    }
                }
                break;
//            case "nakshatramAtoZ" :
//                // sub1 indicates seva modal one and sub2 indicates seva modal 2
//                collections.comparator = function (sub1, sub2) {
//                    if (!sub1.has("nakshatram")) {
//                        return -1;
//                    } else if (!sub2.has("nakshatram")) {
//                        return 1
//                    } else if (sub1.has("nakshatram") && sub2.has("nakshatram")) {
//                        var ret = sub1.get("nakshatram").nakshatram < sub2.get("nakshatram").nakshatram ? -1 : sub1.get("nakshatram").nakshatram > sub2.get("nakshatram").nakshatram ? 1 : 0;
//                        return ret;
//                    }
//                }
//                break;
//            case "nakshatramZtoA" :
//                // sub1 indicates seva modal one and sub2 indicates seva modal 2
//                collections.comparator = function (sub1, sub2) {
//                    if (!sub1.has("nakshatram")) {
//                        return 1;
//                    } else if (!sub2.has("nakshatram")) {
//                        return -1
//                    } else if (sub1.has("nakshatram") && sub2.has("nakshatram")) {
//                        var ret = sub1.get("nakshatram").nakshatram < sub2.get("nakshatram").nakshatram ? 1 : sub1.get("nakshatram").nakshatram > sub2.get("nakshatram").nakshatram ? -1 : 0;
//                        return ret;
//                    }
//                }
//                break;
        }

        collections.sort();

//        console.log(collections);
    },

    /**
     * To sort the records on place
     * @param e
     */
    sortByPlace: function(e){
        this.$el.find('.name-sort').html('Donor');
        // Check weather element have value attribute or not
        if($(e.currentTarget).attr("value")){
            // Get the value of set sort
            var sortStringVal=$(e.currentTarget).attr("value");
            if(sortStringVal==="placeAtoZ"){
                $(e.currentTarget).attr("value","placeZtoA");
                $(e.currentTarget).html('Place <i class="icon-arrow-up"></i>');
            }else if(sortStringVal==="placeZtoA"){
                $(e.currentTarget).attr("value","placeAtoZ");
                $(e.currentTarget).html('Place <i class="icon-arrow-down"></i>');
            }
        }else{
            $(e.currentTarget).attr("value","placeAtoZ");
            $(e.currentTarget).html('Place <i class="icon-arrow-down"></i>');
        }

        var sortVal = $(e.currentTarget).attr("value");
        var collections = this.collection;

        switch (sortVal) {
            case "placeAtoZ" :
                // sub1 indicates seva modal one and sub2 indicates seva modal 2
                collections.comparator = function (sub1, sub2) {
                    if (sub1.get("member").get("place") < sub2.get("member").get("place")) {
                        return -1;
                    } else if (sub1.get("member").get("place") > sub2.get("member").get("place")) {
                        return 1;
                    } else {
                        return 0;
                    }
                }
                break;
            case "placeZtoA" :
                // sub1 indicates seva modal one and sub2 indicates seva modal 2
                collections.comparator = function (sub1, sub2) {
                    if (sub1.get("member").get("place") < sub2.get("member").get("place")) {
                        return 1;
                    } else if (sub1.get("member").get("place") > sub2.get("member").get("place")) {
                        return -1;
                    } else {
                        return 0;
                    }
                }
                break;
        }
        collections.sort();
    },

    sortByName: function(e){
        this.$el.find('.place-sort').html('Place');
        // Check weather element have value attribute or not
        if($(e.currentTarget).attr("value")){
            // Get the value of set sort
            var sortStringVal=$(e.currentTarget).attr("value");
            if(sortStringVal==="nameAtoZ"){
                $(e.currentTarget).attr("value","nameZtoA");
                $(e.currentTarget).html('Donor <i class="icon-arrow-up"></i>');
            }else if(sortStringVal==="nameZtoA"){
                $(e.currentTarget).attr("value","nameAtoZ");
                $(e.currentTarget).html('Donor <i class="icon-arrow-down"></i>');
            }
        }else{
            $(e.currentTarget).attr("value","nameAtoZ");
            $(e.currentTarget).html('Donor <i class="icon-arrow-down"></i>');
        }

        var sortVal = $(e.currentTarget).attr("value");
        var collections = this.collection;

        switch (sortVal) {
            case "nameAtoZ" :
                // sub1 indicates seva modal one and sub2 indicates seva modal 2
                collections.comparator = function (sub1, sub2) {
                    if (sub1.get("member").get("name") < sub2.get("member").get("name")) {
                        return -1;
                    } else if (sub1.get("member").get("name") > sub2.get("member").get("name")) {
                        return 1;
                    } else {
                        return 0;
                    }
                };
                break;
            case "nameZtoA" :
                // sub1 indicates seva modal one and sub2 indicates seva modal 2
                collections.comparator = function (sub1, sub2) {
                    if (sub1.get("member").get("name") < sub2.get("member").get("name")) {
                        return 1;
                    } else if (sub1.get("member").get("name") > sub2.get("member").get("name")) {
                        return -1;
                    } else {
                        return 0;
                    }
                };
                break;
        }

        collections.sort();
    }
});