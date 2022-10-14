import pymysql.cursors
from contextlib import contextmanager

@contextmanager
def conecta():
    conexao = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='',
        db= 'clientes',
        charset='utf8mb4',
        cursorclass= pymysql.cursors.DictCursor
    )
    
    try:
        yield conexao
    finally:
        conexao.close()

# ######### inserir 1 de cada vez #########
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso)'\
#             'VALUES (%s, %s, %s,%s)'
#         cursor.execute(sql, ('Lorena', 'Fonseca', 3, 17.4))
#         conexao.commit()
 
 
# ######### inserir varios de cada vez #########       
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso)'\
#               'VALUES (%s, %s, %s, %s)'
            
#         dados = [
#             ('João', 'Aniceto', 62, 60.4),
#             ('Camila', 'Fonseca', 35, 62.4),
#             ('Maria', 'Bastos', 55, 44.1),
#         ]
#         cursor.executemany(sql, dados)
#         conexao.commit()

# ######### deletar dados #########
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'DELETE FROM clientes WHERE id= %s'
#         cursor.execute(sql, (5,))
#         conexao.commit()

######### atualizar dados dados #########
with conecta() as conexao:
    with conexao.cursor() as cursor:
        sql = 'UPDATE clientes '\
            'SET nome= %s, sobrenome= %s, idade= %s,  peso= %s WHERE ID= %s'
        cursor.execute(sql, ('William', 'Crystian', 30, 65.7, 1))
        conexao.commit()


######### consultar no banco de dados #########
with conecta() as conexao:
    with conexao.cursor() as cursor:
        cursor.execute('SELECT * FROM clientes')
        resultados = cursor.fetchall()
        for linha in resultados:
            print(linha)


