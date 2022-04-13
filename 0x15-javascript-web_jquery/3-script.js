$(document).ready(function () {
  const item = $('DIV#red_header');
  const header = $('header');
  item.click(function () {
    header.addClass('red');
  });
});
