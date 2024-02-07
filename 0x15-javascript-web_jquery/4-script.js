const element = $('header');
$('#toggle_header').on('click', function (event) {
  if (element.hasClass('green')) {
    element.removeClass('green');
    element.addClass('red');
  } else {
    element.removeClass('red');
    element.addClass('green');
  }
});
