(function ($) {
    /**
     * Overrides jQuery.cleanData so that a "destroy" event is triggered
     * whenever a node is removed from the DOM.
     */
    var oldClean = jQuery.cleanData;
    $.cleanData = function (elems) {
        for (var i = 0, elem;
             (elem = elems[i]) !== undefined; i++) {
            $(elem).triggerHandler("destroy");
        }
        oldClean(elems);
    };

})(jQuery);

/**
 * Get a paramter value from the querystring
 *
 * @see http://stackoverflow.com/questions/901115/get-query-string-values-in-javascript#4439076
 *
 * @param {string} name
 * @return string|null The param's value or NULL if the param was not found
 */
$.urlParam = function (name) {
    var results = new RegExp('[\\?&]' + name + '=([^&#]*)').exec(window.location.href);
    if (!results) {
        return null;
    }
    return decodeURIComponent(results[1].replace(/\+/g, " ")) || null;
};

/**
 * Converts a 24-hour time to a 12-hour time
 *
 * @param {int} time
 */
$.prettyTime = function (time) {
    var hour, min, suffix;
    min = time % 100;
    hour = (time - min) / 100;
    if (time < 100) hour += 12;
    else if (time >= 1300) hour -= 12;
    suffix = time >= 1200 ? 'pm' : 'am';
    return hour + ':' + (min < 10 ? '0' + min : min) + suffix;
};

/**
 * Pads a string with the specified padding string
 *
 * @param {string}  str     String to be padded
 * @param {int}     length
 * @param {string}  pad_str
 * @param {string}  [pad_type=left]
 *
 * @return string
 */
$.strPad = function (str, length, pad_str, pad_type) {
    pad_type = pad_type || 'left';

    while (str.length < length) {
        str = pad_type == "left" ? "" + pad_str + str : "" + str + pad_str;
    }
    return str;
};
