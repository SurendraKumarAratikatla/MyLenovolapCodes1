// create this overrides variable within qq scope. Do not use var and avoid creating a variable in global scope
qq.BpFileUploader = function (o) {

    // override options
    var options = {

        listElement: null,
        uploadButtonText: 'Upload image',

        template: '<div class="qq-uploader">' +
            '<div class="qq-upload-drop-area"><span>{dragText}</span></div>' +
            '<div class="qq-upload-button btn">{uploadButtonText}</div>' +
            '<ul class="qq-upload-list"></ul>' +
            '</div>',

        // template for one item in file list
        fileTemplate: '<li>' +
            '<div>' +
            '<span class="qq-upload-spinner"></span>' +
            '<span class="qq-progress-bar"></span>' +
            '<span class="qq-upload-file"></span>' +
            '</div>' +

            '<div>' +
            '<span class="qq-upload-size"></span>' +
            '<a class="qq-upload-cancel" href="#">{cancelButtonText}</a>' +
            '<span class="qq-upload-failed-text">{failUploadtext}</span>' +
            '</div>' +
            '</li>',

        classes: {
            // used to get elements from templates
            button: 'qq-upload-button',
            drop: 'qq-upload-drop-area',
            dropActive: 'qq-upload-drop-area-active',
            dropDisabled: 'qq-upload-drop-area-disabled',
            list: 'qq-upload-list',
            progressBar: 'qq-progress-bar',
            file: 'qq-upload-file',
            spinner: 'qq-upload-spinner',
            size: 'qq-upload-size',
            cancel: 'qq-upload-cancel',

            // added to list item <li> when upload completes
            // used in css to hide progress spinner
            success: 'qq-upload-success',
            fail: 'qq-upload-fail'
        }
    };

    qq.extend(options, o);

    o = options;

    // call parent constructor
    qq.FileUploader.apply(this, arguments);
};

qq.extend(qq.BpFileUploader.prototype, qq.FileUploader.prototype);

