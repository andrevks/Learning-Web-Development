/* 
Diff Two Arrays

Compare two arrays and return a new array with any items only found in one of the two given arrays, but not both. In other words, return the symmetric difference of the two arrays.

Note: You can return the array with its elements in any order.


*/

function diffArray(arr1, arr2) {
  var newArr = [];

  function compareArr(arr1, arr2){
     for(let i = 0; i < arr2.length; i++){
         if(!arr1.includes(arr2[i])){
           console.log("Right here: ", arr2[i] , "is not isn't included")
           newArr.push(arr2[i])
         } 
      }
  }

    compareArr(arr1,arr2);
    compareArr(arr2,arr1);

  return newArr;
}

console.log("Result:")
console.log(diffArray([], ["snuffleupagus", "cookie monster", "elmo"]))