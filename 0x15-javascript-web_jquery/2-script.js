const $ = window.$;
$(document).ready(function () {
  const item = $('DIV#red_header');
  item.click(function () {
    item.css('color', '#FF0000');
  });
});

// window.onload = () => {
//   const $item = document.querySelector('DIV#red_header');
//   $item.onclick = function () {
//     updateElementColor($item);
//   };
// };
//
// const updateElementColor = ($item) => {
//   $item.style.color = '#FF0000';
// };
