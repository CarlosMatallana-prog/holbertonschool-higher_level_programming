#!/usr/bin/node
exports.esrever = function (list) {
  const newList = [];
  list.forEach(function (currentValue, index) {
    newList.push(list[list.length - index - 1]);
  });
  return newList;
};
