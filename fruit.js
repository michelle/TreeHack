 types[name]['el'] =  $("<div></div>").text(name).data('info', {name: name, x: _x + 15, y: _y + 15, fruit: types[name]}).addClass(div).attr('title',tit).css({left: _x, top: _y}).toggle(function(){
	 
	 var data = $(this).data('info');
	 expand(data.fruit, data.x, data.y);
     }, function(){
	 var data = $(this).data('info');
	 removeChildren(data.fruit);
     }).appendTo("#growsOnTrees");
}