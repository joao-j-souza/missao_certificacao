"""
"""
import sqlite3
from model.Banco import Banco


class Usuario:
    def __init__(self):
        self.codigo = None
        self.cpf = None

    def setCodigo(self, codigo):
        self.codigo = codigo

    def getCodigo():
        return self.codigo

    def setCpf(self, cpf):
        self.cpf = cpf

    def getCpf():
        return self.cpf
    
    def listar(self):
        banco = Banco()
        try:
            banco.conecta_bd()
            banco.cursor.execute(
                """ SELECT codigo, cpf FROM usuarios ORDER BY codigo ASC; """)
            resposta = banco.cursor.fetchall()
            return {'success': True, 'resultado': resposta}
        except Exception as erro:
            return {'success': False, 'mensagem': f"Ocorreu um erro ao listar os usuários: {erro}"}
        finally:
            banco.desconecta_bd()    
    
    def listar_cb(self):
        banco = Banco()
        try:
            banco.conecta_bd()
            banco.cursor.execute(
                """ SELECT 
                    	codigo,
	                    cpf
                    FROM
	                    usuarios
                    ORDER BY
	                    codigo ASC; """)
            resposta = banco.cursor.fetchall()
            resultado = [(row[0], row[1]) for row in resposta]
            return {'success': True, 'resultado': resultado}
        except Exception as erro:
            return {'success': False, 'mensagem': f"Ocorreu um erro ao listar os usuários: {erro}"}
        finally:
            banco.desconecta_bd()       


