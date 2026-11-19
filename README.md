# Tutores e Pets

Trabalho de Desenvolvimento Web II. É uma API feita com FastAPI e um banco MySQL, e um site em Vue que mostra os dados.

## Como rodar

1. No MySQL Workbench, abrir o arquivo `backend/banco.sql` e executar.
2. Copiar o arquivo `backend/.env.example` para `backend/.env` e colocar a senha do MySQL.
3. Rodar a API:

        cd backend
        pip install -r requirements.txt
        uvicorn main:app --reload

4. Em outro terminal, rodar o Vue (na pasta principal):

        npm install
        npm run dev

O site abre em http://localhost:5173 e a documentação da API em http://127.0.0.1:8000/docs

## Endpoints

- GET /tutores
- GET /tutores/{id}
- GET /pets
- GET /pets/{id}