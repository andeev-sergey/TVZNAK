$(".menu").click (function(){
  $(this).toggleClass('open');
  $('#navigation').toggleClass('open');
  $('body, html').toggleClass('fixed');
});
