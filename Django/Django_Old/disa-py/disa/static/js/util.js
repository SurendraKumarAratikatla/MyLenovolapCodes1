/**
 * This file contains all utility javascript functions
 *
 */


/**
 * Returns Date object in the local timezone.
 *
 * @param {String} date date should be in YYYY-MM-DD format
 * @return {Date}
 */
function getDateObject(date){

    if(!date){
        // Date is null or empty
        return null;
    }

    // Date should be of the format YYYY-MM-DD
    var parts = date.match(/(\d+)/g);
    var dateObject = new Date(parts[0], parts[1] - 1, parts[2]);

    return dateObject;
}