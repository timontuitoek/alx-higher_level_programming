$(document).ready(function () {
  $('#add_item').click(function () {
    const myList = $('ul.my_list');

    const newItem = $('<li>Item</li>');

    myList.append(newItem);
  });
});
