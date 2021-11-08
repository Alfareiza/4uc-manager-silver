<h1 align="center" >
    <img src="#">
</h1>
<h2 align="center" >
    Aplicação em Django - 4UC Manager Silver <br>
    <img alt="GitHub stars" src="https://img.shields.io/github/stars/Alfareiza/4uc-manager-silver?style=social">
    <img alt="GitHub followers" src="https://img.shields.io/github/followers/Alfareiza?label=Follow%20me%20%3A%29&style=social">
</h2>

<h2>⚈ Acerca de '4UC Manager Silver'</h2>

Aplicação wev desenvolvida no framework python Django que permite a comunicação com várias contas de 4yousee manager. 


<h2>⚈ Configurar Projeto para execução local</h2>

Para este projeto usei Django 3.2.2 e Python 3.9. 

1. Isolando o Ambiente

    Para isolar o ambiente e usar o projeto você deve seguir os seguintes passos:

    * Isolar ambiente: Executar comando `python -m venv .venv` dentro da pasta do projeto clonado.
    * Isolar ambiente [Windows]: `.venv\Scripts\activate` 
    * Isolar ambiente [Linux]: `source .venv/bin/activate`
    * Instalar dependências: `pip install -r requirements.txt`

2. Variáveis de Ambiente

    Crie um arquivo `.env` na raiz do projeto baseado no arquivo [`env-sample`](https://github.com/Alfareiza/4uc-manager-silver/blob/main/contrib/.env-sample).

    #### Como gerar o SECRET_KEY ?
    Para gerar o SECRET_KEY, após ter criado o .env. Enseguida, execute  `python manage.py shell` e digite o seguinte:
    ```
    >>> from django.core.management.utils import get_random_secret_key
    >>> get_random_secret_key()
    908ads123%$#@!+78uyt5>:u7*(i83er
    ```
    
    Copie e cole o valor na variável de SECRET_KEY no arquivo .env.
    
    #### DATABASE_URL
    
    Você precisa ter um banco de dados para rodar o projeto. Na variável `DATABASE_URL` deve estabelecer a endereço no formato URI, como é mostrado no seguinte exemplo:
    
    ```
    DATABASE_URL = mysql://username:password@host:100/nome_do_banco
    ```
    
    Se a variável é deixada em branco, a aplicação vai procurar o arquivo `db.sqlite3` na pasta raíz do projeto.
    
3. Migrações ao Banco

    Com o ambiente virtual ativo, e o banco existente, execute o seguinte comando: `python manage.py migrate`
    
4. Criando super usuário

    Com o ambiente virtual ativo, execute o seguinte comando: `python manage.py createsuper` e preenche os campos.

<h4 align="center"> 
	🚧  Aplicação Web sempre em construção...  🚧
</h4>
