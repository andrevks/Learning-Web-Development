/* 
Diff Two Arrays

Compare two arrays and return a new array with any items only found in one of the two given arrays, but not both. In other words, return the symmetric difference of the two arrays.

Note: You can return the array with its elements in any order.


*/

function diffArray(arr1, arr2) {
  var newArr = [];


  
  let arr3 = arr1.concat(arr2)

  console.log(arr3)
  // .filter((elem) => {

    for(let i = 0; i < arr3.length; i++){

      if(typeof(arr1[i]) !== 'undefined' && (arr2[i]) !== 'undefined'){
         console.log(".")
         if(!arr3.includes(arr2[i])){
            console.log("arr2: ", arr2[i],arr3.includes(arr2[i]))
         }

         if(!arr3.includes(arr1[i])){
          console.log("arr1: ", arr1[i],arr3.includes(arr1[i]))
         } 
      }

     

   
       
    }
   
  // })
  

  return newArr;
}

console.log("Result:")
console.log(diffArray([1, 2, 3, 5], [1, 2, 3, 4, 5]))
