function destroyer(arr) {

  // console.log(arguments.length)

  // for(let i = 1; i < arguments.length; i++){
  //   const index = arr.indexOf(arguments[i])
  //   console.log("index: " + index)
  //   if(index > -1) {
  //     arr.splice(index,1)
  //   }
  // }
  const args = Array.from(arguments)
  //console.log(args)
  const newArr = arr.filter(
    (elem,index) => {
      
      for(let i = 1; i < args.length; i++){
        
        if(args[i] != elem){
         return true;
        }
      }
      console.log("====")
    }
  )
  return newArr;
}

console.log(destroyer([2, 3, 2, 3], 2, 3))