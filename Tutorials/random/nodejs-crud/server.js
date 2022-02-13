const express = require('express')


const PORT = 5000
const app = express()

app.use(express.json())

const coins = [
    {'id':0,'coin':'Bitcoin'}, 
    {'id':1,'coin':'Ethereum'},
    {'id':2,'coin':'Solana'},
    ]
app.get('/', (req, res) => {
  res.json({message: 'Welcome to the server. Try to use the resource coins'})

} )

const coinsPath = '/api/coins'
app.get(coinsPath, (req, res) => {
  res.json(coins)
})


app.post(coinsPath, (req, res) => {
  const { coin } = req.body

  let count = 0
  let lastPosition = coins.length - 1
  const lastCoin = coins[lastPosition]
  const newCoin = {
                    id: lastCoin.id + 1,
                    coin
                  }

  coins.push(newCoin)
  lastPosition = coins.length - 1
  console.log(coins)
  res.status(201).json(coins[lastPosition])
})


app.put(`${coinsPath}/:id`, (req, res) => {
  const id = +(req.params.id)
  const {coin} = req.body 
  let isIdOnArray = false
  const updatedCoin = {
                    id,
                    coin
                  }

  console.log('Before>> ',coins)
  console.log('\n')
  coins.forEach( (coinElem, index )=> {
    if(coinElem.id === id){
      coins[index] = updatedCoin
      isIdOnArray = true
      res.json({message : 'Updated successfully'})
      return
    }
  })
  console.log('\n')
  console.log(coins)
  if(!isIdOnArray){
    res.status(404).send({'message':'Id doesn\'t exist'})
  }

})

app.delete(`${coinsPath}/:id`, (req, res) => {
  const id = +(req.params.id)

  let isIdOnArray = false
  console.log('Before>> ',coins)
  coins.forEach( (coinElem, index )=> {
    if(coinElem.id === id){
      console.log(coins.splice(index, 1))
      console.log(coins)
      isIdOnArray = true
      res.status(204).send()
    }
  })

  if(!isIdOnArray){
    res.status(404).send({'message':'Id doesn\'t exist'})
  }

})



app.listen(PORT, () => console.log(`Server Listening to port ${PORT}`))