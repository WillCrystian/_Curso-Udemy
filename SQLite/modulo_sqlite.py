import sqlite3

conexao = sqlite3.connect('basededados.db')
cursor = conexao.cursor()

# Criar tabela de dados
cursor.execute('CREATE TABLE IF NOT EXISTS clientes ('
               'id INTEGER PRIMARY KEY AUTOINCREMENT,'
               'nome TEXT,'
               'peso REAL'
               ')')

# ############### Inserir dados na tabela criada #####################
# cursor.execute('INSERT INTO clientes (nome, peso) VALUES ("William", 65.2)')
# cursor.execute('INSERT INTO clientes (nome, peso) VALUES (?, ?)', ('Camila', 62.6))
# cursor.execute('INSERT INTO clientes (nome, peso) VALUES (:nome, :peso)', 
#                {'nome': 'Lorena', 'peso': 17}
#                )
# cursor.execute('INSERT INTO clientes VALUES (:id, :nome, :peso)', 
#                {'id': None, 'nome': 'Joãozinho', 'peso': 23.9}
#                )
# # executar a inserção na tabela
# conexao.commit()

# ########## atualizar dados na tabela #############
# cursor.execute('UPDATE clientes '
#                'SET nome= ? WHERE ID= ?', ('Pedro', 4))
# conexao.commit()

# ############## deletar dados na tabela ##################
# cursor.execute('DELETE FROM clientes WHERE id=?', (2,))
# conexao.commit()

########## buscar dados na tabela de dados  ###################
cursor.execute('SELECT * FROM clientes')
# interagir sobre a busca na tabela 
for linha in cursor.fetchall():
    id_, nome, peso = linha
    print(id_, nome, peso)

print()
########## buscar dados na tabela de dados  ###################
cursor.execute('SELECT nome, peso FROM clientes WHERE peso > ?', (20,))
# interagir sobre a busca na tabela 
for linha in cursor.fetchall():
    nome, peso = linha
    print(nome, peso)
    
cursor.close()
conexao.close()