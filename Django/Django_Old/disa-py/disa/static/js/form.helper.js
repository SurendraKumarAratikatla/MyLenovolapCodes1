/*

 Copyright (c) 2009 Stefano J. Attardi, http://attardi.org/

 Permission is hereby granted, free of charge, to any person obtaining
 a copy of this software and associated documentation files (the
 "Software"), to deal in the Software without restriction, including
 without limitation the rights to use, copy, modify, merge, publish,
 distribute, sublicense, and/or sell copies of the Software, and to
 permit persons to whom the Software is furnished to do so, subject to
 the following conditions:

 The above copyright notice and this permission notice shall be
 included in all copies or substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
 EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
 MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
 NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
 LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
 OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
 WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

 */
(function($) {

    function toggleLabel() {
        var input = $(this);
        var def = input.val();
        var label = input.prev('label').attr('for');
        var label_class = input.prev('label').attr('class');
        /*
         alert(label+': '+label_class);
         //*/
        if(checkLabel.call(this) == true) {
            setTimeout(function() {
                if(!input.val()) {
                    input.prev('label').css('visibility', '');
                } else {
                    input.prev('label').css('visibility', 'hidden');
                }
            }, 0);
        } else {
        }
    }

    function checkLabel() {
        var input = $(this);
        var def = input.val();
        var label = input.prev('label').attr('for');
        var label_class = input.prev('label').attr('class');
        /*
         alert(label+': '+label_class);
         //*/
        if(input.prev('label').hasClass('inside')) {
            return true;
        } else {
            return false;
        }
    }

    $('input, textarea').on('keydown', toggleLabel);
    $('input, textarea').on('paste', toggleLabel);
    $('select').on('change', toggleLabel);

    $('input, textarea').on('focusin', function() {
        if(checkLabel.call(this) == true) {
            $(this).prev('label').css('color', '#ccc');
        }
    });

    $('input, textarea').on('focusout', function() {
        if(checkLabel.call(this) == true) {
            $(this).prev('label').css('color', '#999');
        }
    });

    //*
    $(function() {
        $('input, textarea').each(function() {
            toggleLabel.call(this);
        });
    });
    //*/

})(jQuery);