<!--
Antes de publicar a issue, lembre-se de clicar na aba "Preview", para visualizar se a formatação está correta =)
-->

<!-- Escreva/insira as imagens após essa linha -->
# Null e undefined

Ambos representa vazio e a diferença é que o **null** é atribuído explicitamente pelo programador, já o **undefined** vem por padrão do JavaScript.

## Undefined

Quando cria-se um variável e não atribui um valor o JS atribui o undefined. 

```js

let nftToken

console.log(nftToken, nftToken + 2022, `The NFT token is ${nftToken}`)

undefined NaN 'The NFT token is undefined'
```

Ao realizar uma operação matemática o resultado é NaN e ao ser utilizando na string é convertido para string.


## Null

Quando cria-se um variável e deseja ter um valor vazio.

```js

let nftToken = null 

console.log(nftToken, nftToken + 2022, `The NFT token is ${nftToken}`)

null 2022 'The NFT token is null'
```

Ao realizar uma operação matemática o null é considerado ZERO e quando está numa string é convertido para string.
