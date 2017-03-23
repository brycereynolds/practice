'use strict'

let a = 'asdfsl'
let b = 'jjsdfl'

function strSortIntoNumeric(str){
    return str.split("").sort().map((el) => el.charCodeAt(0));
}

function intersection(arr1, arr2){
    let i = 0, j = 0;

    let same = [];
    let count = 0;
    while(i < arr1.length && j < arr2.length){
        // console.log("arr1", i, arr1[i]);
        // console.log("arr2", j, arr2[j]);
        if(arr1[i] < arr2[j]){
            i++;
            // console.log("NEW i: " + i);
        }else if (arr2[j] < arr1[i]){
            j++;
            // console.log("NEW j: " + j);
        }else{
            same.push(arr1[i]);
            i++;
            j++;
        }
        count++;
    }

    return same;
}

function findAnagrams(a, b){
    let aSort = strSortIntoNumeric(a);
    let bSort = strSortIntoNumeric(b);

    // console.log("aSort", aSort);
    // console.log("bSort", bSort);

    let common = intersection(aSort, bSort);
    let removeCount = (aSort.length - common.length) + (bSort.length - common.length);
    return removeCount;
}

console.log(findAnagrams(a, b))