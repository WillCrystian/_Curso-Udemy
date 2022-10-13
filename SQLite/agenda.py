import sqlite3

class AgendaDB:
    def __init__(self, banco_dados) -> None:
        self.conn = sqlite3.connect(banco_dados)
        self.cursor = self.conn
        
        
    def inserir(self, nome, telefone):
        comando = 'INSERT OR IGNORE INTO agenda (nome, telefone) VALUES (?, ?)'
        self.cursor.execute(comando, (nome, telefone))
        self.conn.commit()

    
    def editar(self, nome, telefone, id):
        comando = 'UPDATE OR IGNORE agenda SET nome= ?, telefone= ? WHERE ID= ?'
        self.cursor.execute(comando, (nome, telefone, id))
        self.conn.commit()
    
    def excluir(self, id):
        comando = 'DELETE FROM agenda WHERE id=?'
        self.cursor.execute(comando, (id,))
        self.conn.commit()
    
    def listar(self):
        res = self.cursor.execute('SELECT * FROM agenda')
        # interagir sobre a busca na tabela
        
        for linha in res.fetchall():
            print(linha)
    
    def buscar(self, valor):
        comando = 'SELECT * FROM agenda WHERE nome LIKE ?'
        res = self.cursor.execute(comando, (f'%{valor}%',))
        # interagir sobre a busca na tabela
        
        for linha in res.fetchall():
            print(linha)
        
    def fechar(self):
        self.cursor.close()
        self.conn.close()
    
if __name__ == '__main__':
    agenda = AgendaDB('agenda.db')
    agenda.buscar('ian') 
    
    
    #agenda.listar()
    agenda.fechar()