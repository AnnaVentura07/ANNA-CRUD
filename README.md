API de Inventário de Jogos
Esta API foi desenvolvida em Python com o framework Flask para gerenciar um catálogo de jogos. O sistema utiliza SQLite3 para armazenamento local, facilitando a execução sem necessidade de configurações complexas de banco de dados.

Estrutura do Banco de Dados
Os dados são armazenados no arquivo inventario_jogos.db. A tabela principal contém os seguintes campos:

ID: Gerado automaticamente.

Título: Nome do jogo.

Plataforma: Console ou sistema (ex: Nintendo 3DS, PC).

Ano de Lançamento: Ano em que o jogo saiu.

Preço: Valor de mercado atual.

Como Configurar e Rodar
1. Instalação das dependências
Abra o terminal e instale o Flask:

Bash
pip install flask
2. Preparação do banco de dados
Execute o script inicial para criar a tabela:

Bash
python3 init_db.py
3. Inicialização do servidor
Coloque a API no ar:

Bash
python3 app.py
O servidor estará disponível em: http://127.0.0.1:5000

Guia de Uso (Comandos cURL)
Use os comandos abaixo no terminal para interagir com a API.

Adicionar novos jogos (POST)
Exemplo: Jogo de Simulação/Moda

Bash
curl -X POST http://127.0.0.1:5000/jogos -H "Content-Type: application/json" -d '{"titulo": "Style Savvy: Styling Star", "plataforma": "Nintendo 3DS", "ano_lancamento": 2017, "preco": 149.90}'
Exemplo: Jogo de Corrida

Bash
curl -X POST http://127.0.0.1:5000/jogos -H "Content-Type: application/json" -d '{"titulo": "NFS Underground 2", "plataforma": "PC", "ano_lancamento": 2004, "preco": 45.00}'
Listar e Buscar (GET)
Ver todos os jogos cadastrados:

Bash
curl http://127.0.0.1:5000/jogos
Ver um jogo específico pelo ID (exemplo ID 2):

Bash
curl http://127.0.0.1:5000/jogos/2
Atualizar e Remover (PUT/DELETE)
Atualizar dados de um jogo (exemplo ID 3):

Bash
curl -X PUT http://127.0.0.1:5000/jogos/3 -H "Content-Type: application/json" -d '{"titulo": "Nintendogs + Cats Edição Especial", "plataforma": "Nintendo 3DS", "ano_lancamento": 2011, "preco": 95.00}'
Excluir um jogo do sistema (exemplo ID 9):

Bash
curl -X DELETE http://127.0.0.1:5000/jogos/9
Códigos de Resposta
200/201 (Sucesso): A solicitação foi atendida com sucesso e o dado foi lido ou criado.

204 (Sem Conteúdo): A atualização ou exclusão funcionou corretamente, mas não há texto para exibir.

404 (Não Encontrado): O ID informado não existe no banco de dados.
