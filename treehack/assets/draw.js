$( document ).ready(function() {
        countVars = function( things ) {
            var ret = 0;
            for( var kind in things ) {
                if ( kind != 'vars' && kind != 'methods' && kind != 'classes' ) continue;
                for( var name in things[ kind ] ) { 
                    ret++;
                }
            }
            return ret;
        }

        draw = function( things, base, length, first ) {
            count = countVars( things );
            var increment = 2 * Math.PI / count;
            var angle = Math.random()*2 * Math.PI;
            for( var kind in things ) {
                if ( kind != 'vars' && kind != 'methods' && kind != 'classes' ) continue;
                for( var name in things[ kind ] ) { var item = things[ kind ][ name ];
                    if( count == 1 && first) {
                        var X = base.x;
                        var Y = base.y;
                        var f = 1;
                    }
                    else {
                        var X = base.x + length * Math.cos( angle );
                        var Y = base.y + length * Math.sin( angle );
                        var f = .4
                    }
                    var tit = 'nothing';
                    //if ( item.doc ) { tit = item.doc }
                    item.el =
                        $("<div></div>").text( name ).data('info', { base : { x: X, y: Y }, length : length * f ,fruit : item }).
                        addClass( kind + 'Fruit' ).attr('title', tit ).css({left: X, top: Y}).toggle( function(event){
                                var data = $(this).data('info');
                                if ( data.fruit ) {
                                    draw( data.fruit, data.base, data.length, false );
                                }
                            }, function(event){
                                var data = $(this).data('info');
                                if ( data.fruit ) {
                                    removeChildren( data.fruit );
                                }
                            }).appendTo("#growsOnTrees");
                    angle += increment;
                }

            $('#growsOnTrees div').hover(function() {
                    $('#growsOnTrees div').stop().animate({'opacity': '.2'});
                    $(this).stop().animate({'opacity': '1'});
                }, function() {
                    $('#growsOnTrees div').stop().animate({'opacity': '.6'});
                });
            }
        }

        removeChildren = function( things ) {
            for( var kind in things ) {
                if ( kind != 'vars' && kind != 'methods' && kind != 'classes' ) continue; 
                for( var name in things[ kind ] ) { var item = things[ kind ][ name ];
                    removeChildren( item );
                    if( item && item.el ) {
                        item.el.remove();
                    }
                }
            }
        }

        $('#pushThisButton').click(function() {
                $('#semiRelevantInfo').slideToggle('slow', function() {
                        $('#editor, #containsCodeEditor').css({ 'height' : '500px' });
                        editor = ace.edit("editor");
                        var PythonMode = require("ace/mode/python").Mode;
                        editor.getSession().setMode(new PythonMode());
                        $('#showForm').animate({ 'opacity' : '1' });
                    });
            });

        loadNextThings = function() {
            var base = { x : 521/2, y : 658/ 2 };
            var length = base.x / 2;

            draw( all, base, length, true );

            $('#showFrom').animate({ 'opacity' : '0' });
            $('#editor, #containsCodeEditor').css({ 'height' : '0px' });
            
            $('#contentButNotHappy').fadeToggle('slow');
            $('#contentAndNotSad').fadeToggle('slow');
            
            snippet = ace.edit("snippet");
            var PythonMode = require("ace/mode/python").Mode;
            snippet.getSession().setMode(new PythonMode());
            snippet.getSession().setValue(editor.getSession().getValue());
            
            $('#share').append('Share your code:<br><textarea>'+window.location.href+id+'</textarea>');
            
        };

        $('#smallify').click(function(e) {
                e.preventDefault;
                $.post('/transferCode/', {'code': editor.getSession().getValue()}, function(dic) {
                        all = dic['parsed'];
                        id = dic['ID'];
                        if ( all instanceof Object ) {
                            loadNextThings();
                        } else {
                            $(".parseError").html( all );
                        }
                    });
            });

        $('#updateThisCrap').click(function() {
                $.post('/transferCode/', {'code': snippet.getSession().getValue()}, function(dic) {
                        all = dic['parsed'];
                        id = dic['ID'];
                        $('#growsOnTrees').empty();
                        $('#share').empty();
                        var base = { x : 521/2, y : 658/ 2 };
                        var length = base.x / 2;

                        draw( all, base, length, true );
                        $('#share').append('Share your code:<br><textarea>'+window.location.href+id+'</textarea>');
                    });
            });

    });