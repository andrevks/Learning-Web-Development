function destroyer(arr) {

  // console.log(arguments.length)

  // for(let i = 1; i < arguments.length; i++){
  //   const index = arr.indexOf(arguments[i])
  //   console.log("index: " + index)
  //   if(index > -1) {
  //     arr.splice(index,1)
  //   }
  // }
  var newArr = []
  const args = Array.from(arguments).slice(1)

  for(let i = 0; i < args.length; i++){ 
     arr.filter(
      (elem) => {
        console.log("elem: ",elem)
        console.log(args[i])
        if(arg[i])
      }
     
    )
     console.log(newArr)
     console.log("---")
  }
 
  return newArr;
}

console.log(destroyer([2, 3, 2, 3], 2, 3))