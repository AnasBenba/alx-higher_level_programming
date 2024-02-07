const item = $('<li>').text('Item');
$('#add_item').on('click', function (event) {
  $('Ul.my_list').append(item);
});
