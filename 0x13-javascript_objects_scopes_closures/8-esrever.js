#!/usr/bin/node

exports.esrever = function (list) {
    const newList = [];
    let item;

    for (item of list) {
	newList.unshift(item);
    }

    return newList;
};
