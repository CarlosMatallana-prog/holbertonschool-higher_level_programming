#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let occurrences = 0;
  list.forEach(function (currentValue) {
    if (currentValue === searchElement) {
      occurrences++;
    }
  });
  return occurrences;
};
