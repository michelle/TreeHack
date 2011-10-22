  $(window).load(function() {
    $('#pushThisButton').click(function() {
      $('#semiRelevantInfo').slideToggle('slow', function() {
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
  });