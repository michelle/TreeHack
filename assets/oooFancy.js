  $(window).load(function() {
    
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