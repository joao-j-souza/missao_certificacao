"""
"""
import sqlite3

class Banco:    
    def conecta_bd(self):
        self.conn = sqlite3.connect('matriz_sod')
        # Ativar as restrições de chave estrangeira
        self.conn.execute("PRAGMA foreign_keys = ON")
        self.cursor = self.conn.cursor()
        self.monta_tabelas()
        print("Conectando ao banco de dados")

    def desconecta_bd(self):
        self.conn.close() 
        print("Desconectando ao banco de dados")

    def monta_tabelas(self):
        ### Cria as tabelas
        # Cria a tabela sistemas
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS sistemas (
                codigo INTEGER PRIMARY KEY,
                nome VARCHAR(40) NOT NULL COLLATE NOCASE,
                UNIQUE (nome)
            );
        """)
        # Cria a tabela perfis
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS perfis (
                codigo INTEGER PRIMARY KEY,
                nome VARCHAR(40) NOT NULL,
                descricao VARCHAR(100),
                cod_sistema INTEGER NOT NULL,
                UNIQUE (cod_sistema, nome),
                FOREIGN KEY(cod_sistema) REFERENCES sistemas(codigo) ON DELETE CASCADE
            );
        """)
        # Cria a tabela matriz_sod
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS matriz_sod (
                codigo INTEGER PRIMARY KEY,
                cod_perfil1 INTEGER NOT NULL,
                cod_perfil2 INTEGER NOT NULL,
                concat INTEGER NOT NULL,
                UNIQUE (concat),
                FOREIGN KEY(cod_perfil1) REFERENCES perfis(codigo) ON DELETE CASCADE,
                FOREIGN KEY(cod_perfil2) REFERENCES perfis(codigo) ON DELETE CASCADE
            );
        """)
        # Cria a tabela usuarios
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                codigo INTEGER PRIMARY KEY,
                nome VARCHAR(40) NOT NULL,
                cpf VARCHAR(11) NOT NULL,
                UNIQUE (cpf)
            );
        """)
        # Cria a tabela usuarios_perfis
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios_perfis (
                codigo INTEGER PRIMARY KEY,
                cod_usuario INTEGER NOT NULL,
                cod_perfil INTEGER NOT NULL,
                UNIQUE (cod_usuario, cod_perfil),
                FOREIGN KEY(cod_usuario) REFERENCES usuarios(codigo) ON DELETE CASCADE,
                FOREIGN KEY(cod_perfil) REFERENCES perfis(codigo) ON DELETE CASCADE
            );
        """)        
        self.conn.commit()
        #self.desconecta_bd()
