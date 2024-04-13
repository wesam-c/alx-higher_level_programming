#!/usr/bin/node

/*num of occurences */
exports.nbOccurences = function (list, searchElement) {
    let count = 0;

    for (let i = 0; i < list.length; i++) {
        if (list[i] === searchElement) {
            count++;
        }
    }

    return count;
    /* another method : 
    return list.reduce((a, v) => (v === searchElement ? a + 1 : a), 0); */
};
