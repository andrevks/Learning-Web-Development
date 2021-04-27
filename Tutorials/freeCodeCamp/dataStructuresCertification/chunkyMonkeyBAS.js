/*
Chunky Monkey

Write a function that splits an array (first argument) into groups the length of size (second argument) and returns them as a two-dimensional array.

Example: 

chunkArrayInGroups(["a", "b", "c", "d"], 2) should return [["a", "b"], ["c", "d"]].

*/

function chunkArrayInGroups(arr, size) {
  let myArr = [];
  let end = size;

  for(let i=0; i < arr.length; i = end - size){
    myArr.push(arr.slice(i,end))
    end += size
  }
  return myArr;
}


