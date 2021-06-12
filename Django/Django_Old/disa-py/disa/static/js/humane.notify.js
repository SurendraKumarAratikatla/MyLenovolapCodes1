/**
 * Wrapper over humane js so that we have standard notify functions for success, error, info, log scenarios
 *
 */
var notify = {
    log: function (text, options) {
        humane.log(text, options);
    },

    success: function (text, options) {
        options || (options = {});
        options['addnCls'] = 'humane-jackedup-success';
        humane.log(text, options);
    },

    error: function (text, options) {
        options || (options = {});
        options['addnCls'] = 'humane-jackedup-error';
        options['timeout'] = 5000;
        humane.log(text, options);
    },

    info: function (text, options) {
        options || (options = {});
        options['addnCls'] = 'humane-jackedup-info';
        options['waitForMove'] = true;
        humane.log(text, options);
    }
}