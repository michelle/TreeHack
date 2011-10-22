  $(window).load(function() {
    $('#pushThisButton').click(function() {
      $('#semiRelevantInfo').slideToggle('slow', function() {
        $('#editor, #containsCodeEditor').css({ 'height' : '500' });
        var editor = ace.edit("editor");
        var PythonMode = require("ace/mode/python").Mode;
        editor.getSession().setMode(new PythonMode());
        $('#showForm').animate({ 'opacity' : '1' });
      });
    });
    
    $('.bigBlack').hover(function() {
      $(this).stop().animate({'background-color': '#67ad4b'});
     }, function() {
      $(this).stop().animate({'background-color' : '#000'});
    });
    
    $('#title, #eighteenAndUnderBar a').hover(function() {
      $(this).stop().animate({'color': '#67ad4b'});
     }, function() {
      $(this).stop().animate({'color' : '#000'});
    });
    
    $('.fruit').hover(function() {
      $(this).stop().animate({'background-color': '#f390a7'});
     }, function() {
      $(this).stop().animate({'background-color' : '#cb0030'});
    });
    
  });