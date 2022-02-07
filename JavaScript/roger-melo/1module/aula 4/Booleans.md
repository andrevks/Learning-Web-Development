# Boolean e Comparações

O boolean possui valores de **True** ou **False** que são usado em comparações booleanas. Com isso pode ser feito algumas decisões dependendo do valor que foi atribuído e do contexto da aplicação.

## Exemplo

Suponha-se que um certo usuário não pagou por um ingresso em um show. O valor que permite o usuário entrar seria falso, assim pode-se exibir a mensagem referente a isso. 


```js
const userAllowToEnterTheShow = false 

console.log(userAllowToEnterTheShow)
//since it's false
console.log('The user haven\'t paid for the ticket!') 
```

### Comparações 

As comparações resultam em um valor booleano. Elas podem ser iguais, maiores, menores e muitas outras comparações.

```js
const ticketPrice = 300

console.log(ticketPrice > 300)//Maior
false

console.log(ticketPrice < 300)//Menor
false

console.log(ticketPrice == 300)//Igual
true

console.log(ticketPrice <= 300) //Menor ou Igual
true

console.log(ticketPrice >= 300) //Maior ou Igual
true
```

```js
const userName = 'Linus Torvalds'

console.log(userName == ' ')
false

console.log(userName == 'linus torvalds')
false

console.log(userName == 'Linus Torvalds')
true
```