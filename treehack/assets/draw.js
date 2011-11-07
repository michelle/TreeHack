depthVars = function( things, d ) {
    return Math.max.apply( Math, things.map( function(e) { return depthVars( e, d + 1 ) } ));
}

countVars = function( things ) {
    var ret = 0;
    for( var kind in things ) {
        if ( kind != 'vars' && kind != 'methods' && kind != 'classes' ) continue;
        for( var name in things[ kind ] ) { 
            ret++;
        }
    }
    return ret;
};

draw = function( things, base, length, first ) {
    var dx = 10;
    var dy = 10;
    count = countVars( things );
    var increment = 2 * Math.PI / count;
    var angle = Math.random()*2 * Math.PI;
    for( var kind in things ) {
        if ( kind != 'vars' && kind != 'methods' && kind != 'classes' ) continue;
        for( var name in things[ kind ] ) { var item = things[ kind ][ name ];
            if( count == 1 ) {
                var X = base.x - dx ;
                var Y = base.y - dy ;
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
};

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
};

drawInit = function( all ) {    
    var base = { x : 521/2, y : 658/ 2 };
    var length = base.x / 2;
    
    draw( all, base, length, true );
};
