/*!
 * Customize backbone.js
 */

_.extend(Backbone.Router.prototype, {
    _collections : {},
    _models : {},
    el : '#main',
    menuEl : '#menu',

    /**
     * Adds a collection to the collection pool. If the namespace already
     * exists, each model in the collection is added to the namespace.
     * Duplicate models are ignored.
     *
     * @param coll The collection
     * @param ns Namespace of the collection (e.g. "orders")
     */
    addCollection : function(coll, ns){
        if(_.isUndefined(this._collections[ns])){
            // Namespace is not yet defined
            this._collections[ns] = coll;
        } else{
            // Namespace already exists, so loop through each model in the
            // collection and add it to the namespace collection.
            coll.each(function(model){
                // Adding an existing experience throws an error, so we need a
                // try block
                try{
                    this._collections[ns].add(model);
                } catch(e){
                }
            }, this);
        }
    },

    /**
     * Upsert a model to the model pool
     *
     * @param model The model
     * @param [ns] Namespace into which the model should be added
     * @return {Object} The model that was added/updated
     */
    addModel : function(model, ns){
        if(ns == undefined){
            this._models[model.id] = model;
        } else{
            // A namespace is specified, get a collection and add model
            if(!_.isUndefined(this._collections[ns])){
                var options = {};
                var current = this._collections[ns].get(model.id);
                if(current){
                    // A model with the same ID already exists. Update this
                    // model's attributes instead of adding the new model
                    // to the collection
                    var attrs = model.toJSON();
                    current.set(attrs);
                    return current;
                } else{
                    // This is a new model to be added to the collection
                    this._collections[ns].add(model, options);
                    return model;
                }
            } else{
                // The namespace was not found, so instantiate a new
                // collection and set it to the namespace
                var coll = new Backbone.Collection();
                this._collections[ns] = coll;
                coll.add(model);
                return model;
            }
        }
    },

    /**
     * Retreives a collection from the collection pool.
     *
     * @param ns Collection namespace
     * @returns {Backbone.Collection}
     */
    findCollection : function(ns){
        return this._collections[ns] || null;
    },

    /**
     * Retrieves a model from the model or collection pool.
     *
     * If the model does not yet exist in the pool, it will be fetched from the
     * server. This happens asynchronously. Initially, the model returned will
     * be empty but once the data has been fetched, the model will get
     * populated. It is the responsibility of views rendering the returned
     * model to listen for "change" events to the model and re-render once the
     * data has been populated.
     *
     * @param id      ID of the model
     * @param ns      Namespace of the collection the model belongs to or the
     *                model's class definition (e.g: "experiences" or Experience)
     * @param [data]  GET parameters to be sent as part of the request
     * @param [force] If true, will force a fetch even if the pool already has a
     *                copy of the model (default=false)
     *
     * @returns {Backbone.Model}|null
     */
    findModel : function(id, ns, data, force){
        var model = null,
            found = false;

        // Set defaults
        data || (data = {});
        force || (force = false);

        if(ns == undefined){
            // No namespace specified, so model must not be in a collection
            return this._models[id] || null;
        } else if(typeof(ns) == 'string'){
            // A namespace is specified, so look for the model within that collection
            if(!_.isUndefined(this._collections[ns])){
                var coll = this._collections[ns];
                model = this._collections[ns].get(id);
                if(model){
                    // We have the model. Return it only if force = false
                    if(!force){
                        return model;
                    } else{
                        found = true;
                    }
                } else{
                    // We don't have the model (yet)
                    model = new this._collections[ns].model({
                        id : id
                    });
                    this.addModel(model, ns);
                }
            }
        } else{
            // The namespace is probably a model's class definition
            if(id in this._models){
                // We have the model
                return this._models[id];
            } else{
                // We don't have the model
                model = new ns({
                    id : id
                });
                this.addModel(model);
            }
        }

        if(model){
            // If we've reached here, it means one of two things:
            //   1. We did not find the model in our pool, however, we have an
            //      empty instance that we need to populate with data from the
            //      server.
            //   2. We did find the model in our pool but the "force" flag was
            //      true, so we need to force refresh the data from the server.
            var self = this;
            if(!found) model.isEmpty = true;
            model.fetch({
                data : data,
                // We need the fetch to be silent so that we can set the
                // isEmpty flag to false before the "change" event fires
                silent : true,

                success : function(model, resp){
                    model.isEmpty = false;
                    model.change();
                },

                error : function(model, resp){
                    if(resp.status == 404){
                        //not found error
                        model.notFound = true;
                        model.isEmpty = false;
                        model.trigger('change', model);
                    } else{
                        // If there was an error, remove the model from the pool
                        throw 'There was a problem fetching model with id ' + model.id;
                        //console.log('There was a problem fetching model with id ' + model.id);
                        if(typeof(ns) == 'string'){
                            self._collections[ns].remove(model);
                        } else{
                            delete self._models[model.id];
                        }
                    }

                }
            });
        }

        // The model will be more or less empty to start off with, so the view
        // who uses it is required to listen to change events so as to render
        // itself after the server responds with data.
        return model;
    },

    initLogin : function(){
        this.loginView = new LoginView();
        $('body').append(this.loginView.el);
        this.loginView.render();
    },

    login : function(options, context){
        //this.loginView.show();
        this.loginView.login(options, context);
    },

    /**
     *  renders the page not found view
     */
    resourceNotFound : function(){
        var resourceNotFoundView = new ResourceNotFoundView();
        $(this.el).empty().append($(resourceNotFoundView.el));
        resourceNotFoundView.render();
    },

    /**
     * Changes page title
     *
     * @param {string} title
     */
    setPageTitle : function(title){
        document.title = 'Boiler Plate - ' + title;
    }
});

/**
 * Extend the Backbone router
 */
var BpRouter = Backbone.Router.extend({
    /**
     * Overrides the parent navigate function.
     *
     * @param fragment
     * @param options
     */
    navigate : function(fragment, options){
        // Animated scroll to the top of page
        $('html,body').animate({
            scrollTop : 0
        }, 500);

        // Hide all modals
        $('.modal').modal('hide');

        // Call the parent function
        Backbone.Router.prototype.navigate.call(this, fragment, options);
    },

    /**
     * Returns an absolute symfony route.
     *
     * @param routeName
     */
    url : function(routeName, attrs){
        return location.protocol + '//' + location.hostname + this.path(routeName, attrs);
    },

    /**
     * Returns a relative symfony route.
     *
     * @param routeName
     */
    path : function(routeName, attrs){
        var urlpath = urlpaths[routeName];
        for(key in attrs){
            urlpath = urlpath.replace("%" + key + "%", attrs[key]);
        }
        urlpath = urlpath.replace(/%.+?%/g, "");
        return urlpath;
    },

    /**
     * Requests data from the server to bootstrap this app. You must implement
     * `_bootstrapSuccess` in order to use this function.
     *
     * On success, `_bootstrapSuccess(response)` is called.
     * On authentication error, `_bootstrapAuthenticate()` is called.
     */
    bootstrap : function(){
        var self = this;
        var pathname = "";
        if(window.location.pathname != '/'){
            pathname = window.location.pathname;
        }
        $.ajax({
            url : pathname + '/bootstrap',
            dataType : 'json',
            success : self._bootstrapSuccess,
            statusCode : {
                401 : self._bootstrapAuthenticate,
                403 : self._bootstrapAuthenticate
            }
        });
    },

    _bootstrapSuccess : function(){
        throw '_bootstrapSuccess not implemented';
    },

    /**
     * Called when `bootstrap()` gets an authentication or authorization
     * challenge response.
     *
     * @param xhr jQuery XHR object
     */
    _bootstrapAuthenticate : function(xhr){
        var self = this;
        this.login({
            success : self.bootstrap
        }, this);
    }
});

//
// Extend the Backbone Model
//
_.extend(Backbone.Model.prototype, {

    /**
     * Indicates whether or not the model contains data. This is set to "true"
     * when the document pool manager is in the process of fetching data for
     * the model, but the model itself is empty at that time.
     *
     * @var boolean
     */
    isEmpty : false,

    /**
     * this is set to true if requested model or data is not found
     */
    notFound : false,

    /**
     * This method is very similar to validate() in what it accepts and what it
     * returns, however, validateExtra() contains validation rules that are
     * business context specific. This method is automatically called when
     * setIfValid() is invoked.
     *
     * E.g. The arrival date must not be less than 48 hours from now. This rule
     * cannot be placed in validate() since that would invalidate all orders
     * that have already been completed.
     *
     * @param {Array} attrs Attributes that need to be validated
     */
    validateExtra : function(attrs){
    },

    validate : function(atts){
    },

    validateAll : function(attrs){
        var errors1 = this.validate(attrs) || {};
        var errors2 = this.validateExtra(attrs) || {};

        // maintain this order.
        var errors = {};
        _.extend(errors, errors2, errors1);
        if(!_.isEmpty(errors))
            return errors;
    },

    /**
     * An extension of the Model.set() functionality. This function is
     * different in that even if some attributes fail validation, those
     * that pass are set in the model.
     *
     * @param {Object} attrs Attributes that need to be validated
     * @param options An options object. silence can be set to true. default is false.
     * @return {Object} A list of field:error pairs or NULL if there are no errors
     */
    setIfValid : function(attrs, options){

        if(_.isUndefined(options)){
            options = {};
        }

        // default silent is false.
        var silent = false;
        if(options.hasOwnProperty('silent')){
            if(options.silent == true){
                silent = true;
            }
        }

        // Validate the attributes
        var errors = this.validateAll(attrs);

        // Remove the invalid attributes from the set
        if(!_.isEmpty(errors)){
            for(field in errors){
                delete attrs[field];
            }
        }

        // Sanitize the attributes
        this.sanitize(attrs);

        attrs = this.removeBlanks(attrs);

        // Set the valid attributes
        this.set(attrs, {'silent' : silent});

        // Return the error object if there are errors
        if(!_.isEmpty(errors))
            return errors;
        else
            return null;
    },

    removeBlanks : function(attrs){
        _.each(attrs, function(val, field){
            if(val == ""){
                attrs[field] = null;
            }
            else if(_.isArray(val) || _.isObject(val)){
                if(val.length <= 0){
                    attrs[field] = null;
                }
            }
        });
        return attrs;
    },

    /**
     * Sanitizes the passed attributes. It does things like trimming whitespace from strings, converting strings to
     * integers and floats, etc.
     *
     * Each model class is responsible for writing its own sanitize function, but is optional. This function is called
     * by setIfValid() before it performs a set().
     *
     * @param {Object}   attrs  The attributes to sanitize
     * @param {Boolean} [apply] If TRUE (default), the data in attrs will be updated
     *
     * @return {Object} The attributes that were sanitized
     */
    sanitize : function(attrs, apply){
        return {};
    }
});

//
// Extend the Backbone View
//
_.extend(Backbone.View.prototype, {

    // Ensure that we bind the "this" object to all our functions
    initialize : function(options){
        _.bindAll(this);

        // Listen to DOM "destroy" event so that we can clean up
        this.$el.on('destroy', this.destroy);

        this.init(options);
    },

    _events : [],

    /**
     * A wrapper function that does a bind but also registers the bind in the
     * view's event manager.
     *
     * @param obj The object to bind to (usually a model)
     * @param event
     * @param callback
     * @param [context]
     */
    _on : function(obj, event, callback, context){
        // If there is no callback, no point in doing anything
        if(!obj || !callback) return this;

        // Perform the bind
        obj.on(event, callback, context);

        // Queue up the arguments in our events manager
        this._events.push([obj, event, callback, context]);
    },

    /**
     * Unbinds all events in the event manager.
     */
    _off : function(){
        _.each(this._events, function(args){
            args[0].off(args[1], args[2], args[3]);
        });
    },

    /**
     * Called right before this view is destroyed
     *
     * @param e
     */
    destroy : function(e){
        this._off();
    },

    render : function(){
        var data = {};
        if(this.model){
            data = this.model.toJSON();
        }
        this.$el.empty().append($(this.template).tmpl(data));
        return this;
    },

    init : function(options){
    },

    // An error handler helper to be used in save operations
    errorHandler : function(model, resp, options){
        switch(resp.status){
            case 400:
                // Validation error
                // Convert the error response text to a JSON object and render
                var errors = $.parseJSON(resp.responseText);

                if(errors.hasOwnProperty('field')){
                    // Field level errors exist
                    this.renderErrors(errors.field);
                }

                if(errors.hasOwnProperty('global')){
                    // Global errors exist
                    var errTxt = "";
                    for(var err in errors.global){
                        errTxt += errors.global[err] + "<br/>";
                    }
                    // error message is not removed by itself because its a message
                    // not specific to one field but user must read it and take necessary actions
                    flash.error(errTxt);
                } else{
                    // No global errors, so display a default error message
                    flash.error("There were some errors in your form");
                }

                break;

            case 401:
                // Authentication required
                this.handleError401(model, resp, options);
                break;

            case 403:
            case 500:
            default:
                // Internal server error
                flash.error("We have encountered an unexpected error, please try again");
                break;
        }
    },

    handleError401 : function(model, resp, options){
        app.login({
            model : model,
            callbacks : options
        });
    },

    renderErrors : function(field){
    },

    /**
     * replaces '\n' with <br> tag
     * @param {string} text
     */
    nl2br : function(text){
        return this.nl2p(text);
    },

    /**
     * Wraps text separated by newlines within <p> tags
     *
     * @param str
     * @return {String}
     */
    nl2p : function(str){
        var out = '',
            arr = str.split('\n');
        _.each(arr, function(p, i){
            if($.trim(p).length > 0){
                out += '<p>' + $.trim(p) + '</p>';
            }
        });

        return out;
    }
});

//
// Extend the Backbone Collection
//
_.extend(Backbone.Collection.prototype, {
    /**
     * This will update the collection with the new list of models. If the model already exists in the collection
     * it updates with new data else adds a new model to the collection.
     *
     * @param models
     * @param options
     */
    update : function(models, options){
        var i, length, model;
        models || (models = []);
        options || (options = {});
        models = _.isArray(models) ? models.slice() : [models];

        // check if the model already exists in the collection
        // if yes set to the model or add to the collection
        for(i = 0, length = models.length ; i < length ; i++){
            var modelData = models[i];
            model = this.get(modelData.id);
            if(model){
                model.set(modelData, options);
            }
            else{
                this.add(modelData, options);
            }
        }
        if(!options.silent) this.trigger('update', this, options);
        return this;
    }
});
