const $ = window.$;
window.onload = () => {
  const listItems = $('.my_list');
  const addItem = $('#add_item');
  addItem.click(function () {
    const newItem = '<li>Item</li>';
    listItems.append(newItem);
  });
};
