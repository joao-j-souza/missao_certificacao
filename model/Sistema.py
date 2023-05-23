"""
"""
import sqlite3
from model.Banco import Banco


class Sistema:
    def __init__(self):
        self.codigo = None
        self.nome = None

    def setCodigo(self, codigo):
        self.codigo = codigo

    def getCodigo(self):
        return self.codigo

    def setNome(self, nome):
        self.nome = nome

    def getNome(self):
        return self.nome

    def buscar(self):
        banco = Banco()
        try:
            banco.conecta_bd()
            codigo = self.codigo if self.codigo != "" else "NULL"
            query = """ SELECT codigo, nome FROM sistemas WHERE ({0} IS NULL OR codigo = {0}) AND nome LIKE '%{1}%' ORDER BY nome ASC; """.format(
                codigo, self.nome)
            banco.cursor.execute(query)
            resposta = banco.cursor.fetchall()
            if not resposta:
                return {'success': True, 'mensagem': 'Registro não encontrado.'}
            else:
                return {'success': True, 'resultado': resposta}
        except Exception as erro:
                return {'success': False, 'mensagem': f"Ocorreu um erro na busca: {erro}"}
        finally:
            banco.desconecta_bd()

    def inserir(self):
        banco = Banco()
        try:
            banco.conecta_bd()
            banco.cursor.execute(
                """ INSERT INTO sistemas (nome) VALUES (?)""", (self.nome,))
            banco.conn.commit()
            return {'success': True, 'mensagem': 'Registro cadastrado com sucesso.'}
        except sqlite3.IntegrityError as erro:
            return {'success': False, 'mensagem': f"Esse sistema já está cadastrado."}
        except Exception as erro:
            return {'success': False, 'mensagem': f"Ocorreu um erro ao cadastrar um sistema: {erro}"}
        finally:
            banco.desconecta_bd()

    def listar(self):
        banco = Banco()
        try:
            banco.conecta_bd()
            banco.cursor.execute(
                """ SELECT codigo, nome FROM sistemas ORDER BY codigo ASC; """)
            resposta = banco.cursor.fetchall()
            return {'success': True, 'resultado': resposta}
        except Exception as erro:
            return {'success': False, 'mensagem': f"Ocorreu um erro ao listar os sistemas: {erro}"}
        finally:
            banco.desconecta_bd()

    def alterar(self):
        banco = Banco()
        try:
            banco.conecta_bd()
            if not self.nome:
                raise ValueError("O campo 'nome' é obrigatório")
            banco.cursor.execute(
                """ UPDATE sistemas SET nome = ? WHERE codigo = ?""", (self.nome, self.codigo))
            banco.conn.commit()
            return {'success': True, 'mensagem': 'Registro alterado com sucesso.'}
        except sqlite3.IntegrityError as erro:
            return {'success': False, 'mensagem': 'Já existe um sistema com esse nome.'}
        except Exception as erro:
            return {'success': False, 'mensagem': f"Ocorreu um erro ao tentar alterar o registro: {erro}"}
        finally:
            banco.desconecta_bd()

    def deletar(self):
        banco = Banco()
        try:
            banco.conecta_bd()
            banco.cursor.execute(
                """ DELETE FROM sistemas WHERE codigo = ?""", (self.codigo))
            banco.conn.commit()
            return {'success': True, 'mensagem': 'Registro deletado com sucesso.'}
        except Exception as erro:
            return {'success': False, 'mensagem': f"Ocorreu um erro ao tentar deletar o registro: {erro}"}
        finally:
            banco.desconecta_bd()
