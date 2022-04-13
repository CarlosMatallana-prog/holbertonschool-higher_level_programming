$(document).ready(function () {
  const item = $('#toggle_header');
  const header = $('header');
  item.click(function (e) {
    header.toggleClass('green red');
  });
});
