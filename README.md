# Exemplo de microserviços

Este exemplo consiste em um conjunto de microserviços que
fornecem um sistema de cadastro de livros, usuários, e também
de recomendações de livros para usuários. A ideia é que cada microserviço seja responsável por uma das funcionalidades.

Por questões de simplificação, todos os microserviços compartilham acesso há um mesmo
servidor de banco de dados (mongodb).

## Serviço de Acervo

O serviço de acervo é responsável por permitir o cadastro e a listagem dos livros
cadastrados. Ele é implementado em python utilizando XMLRPC. O serviço expõe três funções:
1. cadastrar_livro: que recebe os dados (json) do livro por parâmetro e armazena no banco de dados. O retorno é uma mensagem "done".
2. listar_livros: faz uma consulta no banco de dados e retorna uma lista de todos os livros cadastrados.
3. listar_livros_categoria: recebe como parâmetro o nome de uma categoria, realiza uma consulta no banco de dados filtrando os livros pela categoria informada. Retorna a lista de livros daquela categoria.

## Serviço de Usuários

Responsável por permitir o cadastro e a listagem dos usuários. É implementado em Python utilizando XMLRPC. O serviço expõe duas funções:
1. adicionar_usuarios: recebe os dados (json) de um usuário e armazena no banco de dados. O retorno é um mensagem "done"
2. listar_usuarios: faz um consulta no banco de dados e retorna uma lista de todos os usuários cadastrados.

## Serviço de Recomendações

Responsável por receber os dados do usuário e fazer uma recomendação de livros. Implementado em Python utilizando o microframework Flask. Expõe uma rota:
1. /recomendar: recebe como parâmetro da requisição o idUsuario, faz uma consulta no acervo para obter os livros, e sorteia 3 livros aleatórios.

## Serviço de Frontend

Responsável por permitir que os clientes acessem os outros serviços. Implementado em Python utilizando o microframework Flask.
