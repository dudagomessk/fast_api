# Tutores e Pets

API em FastAPI com banco MySQL e front-end em Vue 3.

## Requisitos

- Python 3
- Node.js
- MySQL Server e MySQL Workbench

## 1. Banco de dados

1. Abra o MySQL Workbench e conecte no seu servidor.
2. Abra o arquivo `backend/banco.sql` (File > Open SQL Script).
3. Execute o script (botao do raio), uma vez so.

O script cria o banco `petshop`, as tabelas `tutores` e `pets` (o pet
tem `tutor_id`, chave estrangeira para o tutor) e alguns dados de exemplo.

## 2. Configurar o .env

Copie o modelo e coloque a senha do seu MySQL em `DB_PASSWORD`:

    Copy-Item backend\.env.example backend\.env

## 3. Rodar a API

    cd backend
    py -m pip install -r requirements.txt
    py -m uvicorn main:app --reload

A documentacao (Swagger) fica em http://127.0.0.1:8000/docs

## 4. Rodar o Vue

Em outro terminal, na pasta raiz do projeto:

    npm install
    npm run dev

Abra http://localhost:5173

## Endpoints

| Metodo | Rota             | Descricao                |
|--------|------------------|--------------------------|
| GET    | /tutores         | Lista todos os tutores   |
| GET    | /tutores/{id}    | Consulta um tutor por id |
| GET    | /pets            | Lista todos os pets      |
| GET    | /pets/{id}       | Consulta um pet por id   |

Se o id nao existir, a API retorna erro 404.

## Estrutura

    backend/
      main.py          rotas da API
      database.py      conexao com o MySQL (executar_sql)
      banco.sql        script para criar o banco
      requirements.txt
      .env.example     modelo das configuracoes
    src/
      views/           paginas (Tutores e Pets)
      components/      menu
      router/          rotas do Vue
      assets/          estilos