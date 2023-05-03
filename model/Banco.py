"""
"""
import sqlite3

class Banco:    
    def conecta_bd(self):
        self.conn = sqlite3.connect('matriz_sod')        
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
                FOREIGN KEY(cod_sistema) REFERENCES sistemas(codigo) 
            );
        """)
        # Cria a tabela matriz_sod
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS matriz_sod (
                codigo INTEGER PRIMARY KEY,
                cod_perfil1 INTEGER NOT NULL,
                cod_perfil2 INTEGER NOT NULL,
                UNIQUE (cod_perfil1, cod_perfil2),
                FOREIGN KEY(cod_perfil1) REFERENCES perfis(codigo),
                FOREIGN KEY(cod_perfil2) REFERENCES perfis(codigo)
            );
        """)
        # Cria a tabela usuarios
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                codigo INTEGER PRIMARY KEY,
                cpf VARCHAR(11) NOT NULL,
                cod_perfil INTEGER NOT NULL,
                UNIQUE (cpf),
                UNIQUE (cpf, cod_perfil),
                FOREIGN KEY(cod_perfil) REFERENCES perfis(codigo)
            );
        """)
        self.conn.commit()
        #self.desconecta_bd()
