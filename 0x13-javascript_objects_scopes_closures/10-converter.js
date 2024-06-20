#!/usr/bin/node
exports.converter = function (base) {
  return New => New.toString(base);
};
