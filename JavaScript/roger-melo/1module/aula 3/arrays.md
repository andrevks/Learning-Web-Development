<!--
Antes de publicar a issue, lembre-se de clicar na aba "Preview", para visualizar se a formatação está correta =)
-->

<!-- Escreva/insira as imagens após essa linha -->

# Arrays 

Array é uma variável que contém um conjunto de variáveis próximas que geralmente tem relação entre si. 

Como o JavaScript é uma linguagem dinâmicamente tipada é possível ter mais de um tipo dentro da Array. Algo que não seria possível em um linguagem fortemente tipada como C.  Mesmo assim, o importante é verificar/questionar se faz sentido utilizar diversos tipos de dados dentro de uma Array.

Exemplo: 
 ```js
//Uma array de livros, aqui estou guardando um conjunto de elementos que tem relação entre si
const books = ['Think and Grow Rich', 'You Were Born Rich', 'You can\'t hurt me']

//Uma array de livros e o número de página de cada livro (Tem relação entre si, faz sentido fazer isso)
const booksAndPage = ['Think and Grow Rich', 350, 'You Were Born Rich', 260,  'You can\'t hurt me', 400]
```


## Métodos de Arrays


### Join

O método **Join** junta os elementos da array em uma **string separada por vírgula** (por padrão) ou com o **símbolo que inserir** como argumento.

 ```js

const books = ['Think and Grow Rich', 'You Were Born Rich', 'You can\'t hurt me']

const joinBooks = books.join()

console.log(joinBooks)// Think and Grow Rich,You Were Born Rich,You can't hurt me

```

### Concat

O método **Concat** concatena os elementos de outra array no final da array original.

 ```js

const books = ['Think and Grow Rich', 'You Were Born Rich', 'You can\'t hurt me']

//Array em concat será adicionada
const concatBooks = books.concat(['Rich Dad, Poor Dad', 'The Dip'])

console.log(concatBooks)// ['Think and Grow Rich', 'You Were Born Rich', "You can't hurt me", 'Rich Dad, Poor Dad', 'The Dip']

```

### Push and Pop

O método **Push** adiciona um elemento no final de uma array e o método **Pop** remove um elemento do final da array.

É importante saber que o **Push** altera a array e retorna o número de elementos que estão na array e  o **Pop** modifica a array e retorna o elemento que foi removido.

#### Push

 ```js

const books = ['Think and Grow Rich', 'You Were Born Rich', 'You can\'t hurt me']

const pushToBooks = books.push('Deep Work')

console.log(pushToBooks, books)

/* 

4 (pushToBooks)

['Think and Grow Rich', 'You Were Born Rich', "You can't hurt me", 'Deep Work'] (books)

*/

```

#### Pop

 ```js

const books = ['Think and Grow Rich', 'You Were Born Rich', "You can't hurt me", 'Deep Work'] 

const popBooks = books.pop()

console.log(popBooks, books)

/* 

Deep Work (popBooks)

 ['Think and Grow Rich', 'You Were Born Rich', "You can't hurt me"] (books)

*/

```


