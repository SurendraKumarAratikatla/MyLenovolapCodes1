
/**
 * Modal to hold nakshatram data
 */
var Nakshatram = Backbone.Model.extend({});

/**
 * Modal to hold maasam data
 */
var Maasam = Backbone.Model.extend({});

/**
 * Modal to hold paksham data
 */
var Paksham = Backbone.Model.extend({});

/**
 * Modal to hold tithi data
 */
var Tithi = Backbone.Model.extend({});

/**
 * Collection to hold nakshatram models
 */
var NakshatramCollection = Backbone.Collection.extend({
    model: Nakshatram
});

/**
 * Collection to hold maasam models
 */
var MaasamCollection = Backbone.Collection.extend({
    model: Maasam
});

/**
 * Collection to hold paksham models
 */
var PakshamCollection = Backbone.Collection.extend({
    model: Paksham
});

/**
 * Collection to hold tithi models
 */
var TithiCollection = Backbone.Collection.extend({
    model: Tithi
});

