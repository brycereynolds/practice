'use strict'

let n = 5
let d = 4

function shiftLeft(arr, moves){
    var newArr = [];
    for(let i = moves; i < arr.length; i++){
        newArr.push(arr[i])
    }
    for(let i = 0; i < moves; i++){
        newArr.push(arr[i])
    }
    return newArr;
}

let arr = [];
for(let i = 1; i <= n; i++){
    arr.push(i);
}

// console.log(arr);

console.log(shiftLeft(arr, d));
