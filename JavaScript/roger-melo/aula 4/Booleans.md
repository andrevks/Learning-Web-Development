
# Boolean e Comparações

O boolean possui valores de **True** e **False** que é usado em comparações booleanas. Com isso pode ser feito algumas decisões dependendo do valor que foi atribuído e do contexto da aplicação.

## Exemplo

Suponha-se que um certo usuário não pagou por um ingresso em um show. O valor que permite o usuário entrar seria falso, assim pode-se exibir a mensagem referente a isso. 

(Não quis entrar no conceito de condicionais aqui, já que não faz parte do escopo da aula)

```js
const userAllowToEnterTheShow = false 

console.log(userAllowToEnterTheShow)
//since it's false
console.log('The user haven\'t paid for the ticket!') 
```