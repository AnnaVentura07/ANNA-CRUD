Como você já testou os comandos e eles funcionaram perfeitamente, o seu README.md deve refletir exatamente essa estrutura. Vou gerar uma versão limpa, técnica e sem decorações, ideal para documentar o que você acabou de fazer no terminal.

Documentação do Projeto: Inventário de Jogos API
Esta é uma API REST desenvolvida em Python com Flask para o gerenciamento de um catálogo de jogos, utilizando SQLite3 como persistência de dados.

Estrutura do Banco de Dados
O arquivo de banco de dados é o inventario_jogos.db. A tabela jogos contém:

id: Chave primária (automática).

titulo: Nome do jogo.

plataforma: Console ou sistema.

ano_lancamento: Ano de saída do título.

Como Instalar e Rodar
Instale o Flask:
pip install flask

Execute o servidor:
python app.py
O servidor iniciará em http://127.0.0.1:5000.

Exemplos de Uso (Comandos cURL)
Abaixo estão os comandos para testar cada funcionalidade do CRUD diretamente no CMD ou Terminal.

1. Inserir Jogos (POST)
Estes comandos foram validados e inserem os registros no banco:

Jogo de Carro:

DOS
curl -X POST http://127.0.0.1:5000/jogos -H "Content-Type: application/json" -d "{\"titulo\": \"Forza Horizon 5\", \"plataforma\": \"Xbox\", \"ano_lancamento\": 2021}"
Jogo de Médico:

DOS
curl -X POST http://127.0.0.1:5000/jogos -H "Content-Type: application/json" -d "{\"titulo\": \"Two Point Hospital\", \"plataforma\": \"PC\", \"ano_lancamento\": 2018}"
Jogo de Vestir:

DOS
curl -X POST http://127.0.0.1:5000/jogos -H "Content-Type: application/json" -d "{\"titulo\": \"Barbie Fashion Closet\", \"plataforma\": \"Mobile\", \"ano_lancamento\": 2020}"
2. Listar Todos os Jogos (GET)
Retorna um JSON com todos os itens cadastrados:

DOS
curl http://127.0.0.1:5000/jogos
3. Buscar por ID (GET)
Retorna apenas o jogo correspondente ao ID informado:

DOS
curl http://127.0.0.1:5000/jogos/1
4. Atualizar Jogo (PUT)
Altera os dados de um jogo existente (Status 204 - No Content):

DOS
curl -X PUT http://127.0.0.1:5000/jogos/1 -H "Content-Type: application/json" -d "{\"titulo\": \"Forza Horizon 5 Premium\", \"plataforma\": \"PC/Xbox\", \"ano_lancamento\": 2021}"
5. Remover Jogo (DELETE)
Exclui um registro permanentemente:

DOS
curl -X DELETE http://127.0.0.1:5000/jogos/1
Respostas do Sistema
200 OK: Operação de leitura ou remoção concluída.

201 Created: Registro inserido com sucesso.

204 No Content: Atualização realizada com sucesso.

404 Not Found: Registro não encontrado no banco de dados.
