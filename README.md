# Instruções para rodar a aplicação

Acesse a pasta do projeto e siga a ordem dos comandos abaixo para criar o
ambiente virtual (virtualenv) e instalar as dependências do projeto:

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt


Faça as migrações dos modelos para o banco sqlite com os comandos:


python manage.py makemigrations

python manage.py migrate


Agora inicie o projeto com o comando:


python3 manage.py runserver



Abra no seu browser o seguinte endereço:

http://localhost:5000/



Nesta tela ja havera o seguinte link:

"products": "http://localhost:5000/products/"

Acessando este link você ja podera fazer testes em todos os endpoints
da api utilizando a interface web que o Django Rest Framework provem.


## Testes

Tambem escrevi alguns testes para testar os endpoints do backend, para executa-los
basta rodar o comando (dentro da pasta backend): python manage.py test


## Endpoints

Por fim segue abaixo os endpoints da api:

Verbo: GET
Endereço: http://localhost:5000/products/
Descrição: Retorna uma lista da todos os produtos cadastrados.

Verbo: POST
Endereço: http://localhost:5000/products/
Descrição: Insere um produto na api, o Json do envio precisa conter
um name, price e opcionalmente um image file.

Verbo: PUT
Endereço: http://localhost:5000/products/idDoProduct/
Descrição: Permite a edição de um product existente na api

Verbo: DELETE
Endereço: http://localhost:5000/products/idDoProduct/
Descrição: Permite a deleção de um product na api.
