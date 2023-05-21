"""
"""
import sqlite3
from model.Banco import Banco


class Perfil:
    def __init__(self):
        self.codigo = None
        self.nome = None
        self.descricao = None

    def setCodigo(self, codigo):
        self.codigo = codigo

    def getCodigo():
        return self.codigo
            
    def setNome(self, nome):
        self.nome = nome

    def getNome():
        return self.nome
    
    def setDescricao(self, descricao):
        self.descricao = descricao

    def getDescricao():
        return self.descricao
    
    def setCodSistema(self, cod_sistema):
        self.cod_sistema = cod_sistema

    def getCodSistema():
        return self.cod_sistema
    
    def listar(self):
        banco = Banco()
        try:
            banco.conecta_bd()
            banco.cursor.execute(
                """ SELECT codigo, nome, descricao, cod_sistema FROM perfis ORDER BY codigo ASC; """)
            resposta = banco.cursor.fetchall()
            return {'success': True, 'resultado': resposta}
        except Exception as erro:
            return {'success': False, 'mensagem': f"Ocorreu um erro ao listar os perfis: {erro}"}
        finally:
            banco.desconecta_bd()    
    
    def listar_cb(self):
        banco = Banco()
        try:
            banco.conecta_bd()
            banco.cursor.execute(
                """ SELECT 
                        perfis.codigo,
                        sistemas.nome || ' - ' || perfis.nome AS "nome"
                    FROM
                        sistemas
                    INNER JOIN
                        perfis ON sistemas.codigo = perfis.cod_sistema ORDER BY perfis.codigo ASC; """)
            resposta = banco.cursor.fetchall()
            resultado = [(row[0], row[1]) for row in resposta]
            return {'success': True, 'resultado': resultado}
        except Exception as erro:
            return {'success': False, 'mensagem': f"Ocorreu um erro ao listar os perfis: {erro}"}
        finally:
            banco.desconecta_bd()
