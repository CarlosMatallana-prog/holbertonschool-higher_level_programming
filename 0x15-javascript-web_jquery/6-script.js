$(document).ready(function () {
  const item = $('DIV#update_header');
  const newHeader = 'New Header!!!';
  const header = $('header');
  item.click(function () {
    header.html(newHeader);
  });
});
