/*
 * Customize backbone.js
 */


//
// Extend the Backbone Model
//
var __sync = Backbone.Model.prototype.sync;
_.extend(Backbone.Model.prototype, {
    // This field is set to true while data is being synced
    syncing: false,

    /**
     * Override the Backbone Model sync method
     */
    sync: function (method, model, options) {

        //from django docs
        function getCookie(name) {
            var cookieValue = null;
            if (document.cookie && document.cookie != '') {
                var cookies = document.cookie.split(';');
                for (var i = 0; i < cookies.length; i++) {
                    var cookie = jQuery.trim(cookies[i]);
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) == (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }

        /* only need a token for non-get requests */
        if (method == 'create' || method == 'update' || method == 'delete' || method == 'patch') {
            // CSRF token value is in an embedded meta tag
            var csrfToken = getCookie('csrftoken');

            if (csrfToken) {
                options.beforeSend = function (xhr) {
                    xhr.setRequestHeader('X-CSRFToken', csrfToken);
                };
            }
        }

        // Override the success callback so that we can reset syncing flags on sync
        var success = options.success,
            error = options.error;

        options.success = function () {
            // Mark the model as not empty
            model.syncing = false;

            // Call the original success callback
            if (success) success.apply(this, arguments);
        };

        options.error = function (resp) {
            model.syncing = false;

            // Call the original error callback
            if (error) error.apply(this, arguments);
        };

        // set syncing true indicating the start of sync process
        model.syncing = true;

        // Call the original Backbone.sync
        __sync.apply(this, arguments);
    }
});


//
// Extend the Backbone View
//
_.extend(Backbone.View.prototype, {

    /**
     * Common error handler which concats the errors and notifies it using humane notifier.
     * @param errors
     */
    renderErrors: function (errors) {
        var errorStr = "";
        _.each(errors, function (error, key) {
            errorStr += key + " : " + error + "<br/>";
        }, this);
        if (!_.isEmpty(errorStr)) {
            notify.error(errorStr);
        }
    }
});