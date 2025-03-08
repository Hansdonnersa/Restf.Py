Tecnologias Utilizadas

Python 3.12.0

Django==4.2

Django REST Framework (DRF)
djangorestframework==3.14.0

Swagger para documentação interativa

Endpoints

Soma

POST /api/sum/

Exemplo de requisição:

{
    "numbers": [1, 2, 3, 4, 5]
}

Exemplo de resposta:

{
    "sum": 15
}

Média

POST /api/average/

Exemplo de requisição:

{
    "numbers": [10, 20, 30, 40, 50]
}

Exemplo de resposta:

{
    "average": 30.0
}

Testando a API

Usando o Swagger UI

Acesse a documentação interativa da API pelo navegador:
Swagger UI http://127.0.0.1:8000/swagger/

Usando o Postman

Abra o Postman.

Crie uma nova requisição POST.

Defina a URL como:

http://127.0.0.1:8000/api/sum/ ou http://127.0.0.1:8000/api/average/.

No corpo da requisição, selecione raw e JSON.

Insira os dados no formato JSON:

{
    "numbers": [1, 2, 3, 4, 5]
}

Clique em Send para enviar a requisição.

Instalação e Configuração

Clonando o Repositório

git clone https://github.com/seu-usuario/Restf.Py.git
cd Restf.Py

Criando e ativando o ambiente virtual

python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate

Instalando dependências

pip install -r requirements.txt

Executando migrações

python manage.py migrate

Iniciando o servidor

python manage.py runserver

Acesse a API em: http://127.0.0.1:8000/api/sum/