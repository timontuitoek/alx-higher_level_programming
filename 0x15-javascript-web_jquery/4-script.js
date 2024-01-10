$(document).ready(function () {
  $('#toggle_header').click(function () {
    const headerElement = $('header');

    headerElement.toggleClass('red green');
  });
});
