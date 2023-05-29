"""
"""
import sqlite3
from model.Banco import Banco


class Perfil:
    def __init__(self):
        self.codigo = ""
        self.cod_sistema = ""
        self.nome = ""
        self.descricao = ""

    def setCodigo(self, codigo):
        self.codigo = codigo

    def getCodigo(self):
        return self.codigo
            
    def setNome(self, nome):
        self.nome = nome

    def getNome(self):
        return self.nome
    
    def setDescricao(self, descricao):
        self.descricao = descricao

    def getDescricao(self):
        return self.descricao
    
    def setCodSistema(self, cod_sistema):
        self.cod_sistema = cod_sistema

    def getCodSistema(self):
        return self.cod_sistema
    
    def buscar(self):
        banco = Banco()
        try:
            banco.conecta_bd()
            codigo = self.codigo if self.codigo != "" else "NULL"
            query = """ SELECT codigo, cod_sistema, nome, descricao FROM perfis WHERE ({0} IS NULL OR codigo = {0}) ORDER BY codigo ASC; """.format(
                codigo)
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
    
    def listar(self):
        banco = Banco()
        try:
            banco.conecta_bd()
            codigo = self.codigo if self.codigo != "" else "NULL"
            query = f""" SELECT 
                        p.codigo,
                        s.nome,
                        p.nome,
                        p.descricao
                    FROM perfis p
                    INNER JOIN sistemas s
                    ON p.cod_sistema = s.codigo
                    WHERE ({codigo} IS NULL OR p.codigo = {codigo})
                    ORDER BY p.codigo ASC; """
            banco.cursor.execute(query)
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
            codigo = self.codigo if self.codigo != "" else "NULL"
            query = f""" SELECT 
                        p.codigo,
                        s.nome || " - " || p.nome,
                        p.nome,
                        p.descricao
                    FROM perfis p
                    INNER JOIN sistemas s
                    ON p.cod_sistema = s.codigo
                    WHERE ({codigo} IS NULL OR p.codigo = {codigo})
                    ORDER BY p.codigo ASC; """
            banco.cursor.execute(query)
            resposta = banco.cursor.fetchall()
            return {'success': True, 'resultado': resposta}
        except Exception as erro:
            return {'success': False, 'mensagem': f"Ocorreu um erro ao listar os perfis: {erro}"}
        finally:
            banco.desconecta_bd()

    def inserir(self):
        banco = Banco()
        try:
            banco.conecta_bd()
            banco.cursor.execute(
                """ INSERT INTO perfis (cod_sistema, nome, descricao) VALUES (?, ?, ?)""", (self.cod_sistema, self.nome, self.descricao))
            banco.conn.commit()
            return {'success': True, 'mensagem': 'Registro cadastrado com sucesso.'}
        except sqlite3.IntegrityError as erro:
            return {'success': False, 'mensagem': f"Esse perfil já está cadastrado."}
        except Exception as erro:
            return {'success': False, 'mensagem': f"Ocorreu um erro ao cadastrar um perfil: {erro}"}
        finally:
            banco.desconecta_bd()

    def alterar(self):
        banco = Banco()
        try:
            banco.conecta_bd()
            if ((not self.codigo) or (not self.cod_sistema) or (not self.nome)):
                if not self.codigo:
                    raise ValueError("O campo 'Codigo' é obrigatório")
                elif not cod_sistema:
                    raise ValueError("O campo 'Sistema' é obrigatório")
                elif not nome:
                    raise ValueError("O campo 'Nome' é obrigatório")
            banco.cursor.execute(
                """ UPDATE perfis SET cod_sistema = ?, nome = ?, descricao = ? WHERE codigo = ?""", (self.cod_sistema, self.nome, self.descricao, self.codigo))
            banco.conn.commit()
            return {'success': True, 'mensagem': 'Registro alterado com sucesso.'}
        except sqlite3.IntegrityError as erro:
            return {'success': False, 'mensagem': 'Esse perfil já está cadastrado.'}
        except Exception as erro:
            return {'success': False, 'mensagem': f"Ocorreu um erro ao tentar alterar o registro: {erro}"}
        finally:
            banco.desconecta_bd()

    def deletar(self):
        banco = Banco()
        try:
            banco.conecta_bd()
            banco.cursor.execute(
                """ DELETE FROM perfis WHERE codigo = ?""", (self.codigo))
            banco.conn.commit()
            return {'success': True, 'mensagem': 'Registro deletado com sucesso.'}
        except Exception as erro:
            return {'success': False, 'mensagem': f"Ocorreu um erro ao tentar deletar o registro: {erro}"}
        finally:
            banco.desconecta_bd()
