const $ = window.$;
$(document).ready(function () {
  const item = $('#toggle_header');
  const header = $('header');
  item.click(function () {
    header.toggleClass('green red');
  });
});
