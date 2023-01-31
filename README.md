# Sobre o Projeto

Esse projeto visa carregar um arquivo .txt de Balançoes financeiros de pequenos comércios e mostrar seu saldo atual.

Dockerização em andamento...

### Feito Com

Abaixo segue o que foi utilizado na criação deste projeto:

#### Front End
 - React - Framework Utilizado para desenvolver interfaces web.
 - Vite - Agiliza nosso processo de desenvolvimento, com instalacoes e build de pacotes/modulos javascript feitas rapidamente.
 - typescript - Linguagem totalmente tipada baseada no javascript, para fortalecer o seu desenvolvimento em equipe,rendendo mais e fazendo voce perder menos tempo procurando propriedades ou metodos escondidos no objeto.
 - Axios - Biblioteca Utilizada para trabalhar com requisicoes.
 - styled-components - Biblioteca de estilizacao utilizada em conjunto com o react

#### Back End
 - Flask - Framework python para a construção de APIS
 - Flask-SQLAlchemy - ORM utilizada em conjuto com o flask
 - Flask-Migrate - Criar migrações em sua aplicação flask.
 - SQLAlchemy-serializer - Serializar saída no formato JSON. 
<!-- GETTING STARTED -->

## Começando

Para conseguir utilizar o projeto localmente,siga os passos abaixo.
### Pré-requisitos

 - Necessário uma IDE,de preferência uma com terminal integrado em sua interface,(para facilitar a execucão dos comandos).

 - Necessário Python3

 - Necessário NPM

 - Necessário postgreSQL

 - Você precisará estar com dois terminais abertos para e execução de ambas as aplicações em paralelo, pois ela se comunicarão entre si via localhost.
### Instalação Back-end

1. Para inicializar a aplicação é bem simples, bastar clonar o repositóriorio e entrar nas respectivas pastas: back-end e front-end.
2. Crie um venv para isolar as dependências:
```sh
  python -m venv venv #Tenha certeza de estar utilizando o Python 3
```
3. Utilize o venv:
```sh
  source venv/bin/activate #A ativacao difere do sistema operacional.
```
4.Dentro do ambiente instale as dependências:
```sh
  pip install -r requirements.txt
```
5. Você irá precisar do banco de dados postgreSQL rodando na porta 5432.
6. Você terá que criar um usuário e um banco de dados(caso ja tenha ótimo).
7. A aplicação irá Utilizar da variável de ambiente .env para acessar o banco de dados.
8. Siga o .env.example para a construção dos dados necessários.
9. Com a conexão feita rode as migrações:
```sh
  flask db upgrade
```
10. Com as migrações feitas Execute a aplicação back end:

```sh
  flask run
```
11. Você verá algo semelhante no terminal:
```sh
  * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 567-901-471
```
 - Projeto Back End rodando perfeitamente!

### Instalação Front End
1. entre na pasta front-end e rode o seguinte comando para instalar as dependências:
```sh
  yarn
```
2. Execute o projeto:
```sh
  yarn dev
```
3.Você verá algo semelhante:
```sh
    VITE v4.0.4  ready in 808 ms

  ➜  Local:   http://localhost:3000/
  ➜  Network: use --host to expose
  ➜  press h to show help
```
 - Projeto Front End Rodando perfeitamente!

### Utilzando o projeto

 1. A Utilização é simples, copie o conteúdo deste arquivo <a href="https://github.com/Kenzie-Academy-Brasil-Developers/desafio-backend-m6/blob/main/CNAB.txt">CNAB</a> e crie um .txt 
 2. Com a aplicação rodando, você verá um botão para upload
 3. Clique no botão e fação o upload do arquivo .txt
 4. Envie
 5. Mostrará na sua tela:
   - O Tipo da transação, nome da loja que a fez e o saldo atual.