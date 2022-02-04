# Strict Equality and Inequality

Os operadores de comparação não estritos possuem alguns resultados inesperados quando comparamos valores.

### Exemplos

```js
const moneyInMyBankAccount = 1024000

console.log(moneyInMyBankAccount == '1024000') //It should be false, right ?
true //But the result is true 

console.log(moneyInMyBankAccount != '1024000') //It should be true, right ?
false //But the result is false, so weird...

```

#### Por que isso acontece?

- Quando é utilizado a comparação não estrita é feita algumas conversões de tipos antes da comparação. Neste caso, antes de comparar a string se transforma ela em no tipo número.

#### Como resolver ?

- Utilize a forma de comparação estrita do JavaScript, é bem simples :D

- Ao invés de utilizar dois sinais de iguais ('==') utilize três sinais de iguais ('==='). No sinal não igual, utilize dois sinais iguais ('!=='). Com isso estes sinais compararam o tipo também, mantendo da maneira esperada.


```js
const moneyInMyBankAccount = 1024000

console.log(moneyInMyBankAccount === '1024000') //It should be false
false // Now it's really working as expected !

console.log(moneyInMyBankAccount !== '1024000') //It should be true
true // Now it's really working as expected !

```

Concluindo, utilize o **'igual a, e do mesmo tipo (===)'** e **'diferente de, e do mesmo tipo (!==)'** para ter certeza do resultado da comparação.
