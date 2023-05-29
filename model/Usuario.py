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

    def getCodigo(self):
        return self.codigo
    
    def setNome(self, nome):
        self.nome = nome

    def getNome(self):
        return self.nome        

    def setCpf(self, cpf):
        self.cpf = cpf

    def getCpf(self):
        return self.cpf
    
    def buscar(self):
        banco = Banco()
        try:
            banco.conecta_bd()
            codigo = self.codigo if self.codigo != "" else "NULL"
            query = """ SELECT codigo, nome, cpf FROM usuarios WHERE ({0} IS NULL OR codigo = {0}) AND cpf LIKE '%{1}%' ORDER BY nome ASC; """.format(
                codigo, self.cpf)
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
            banco.cursor.execute(
                """ SELECT codigo, nome, cpf FROM usuarios ORDER BY codigo ASC; """)
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
	                    nome || ' - ' || cpf
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

    def inserir(self):
        banco = Banco()
        try:
            banco.conecta_bd()
            banco.cursor.execute(
                """ INSERT INTO usuarios (nome, cpf) VALUES (?, ?)""", (self.nome, self.cpf))
            banco.conn.commit()
            return {'success': True, 'mensagem': 'Registro cadastrado com sucesso.'}
        except sqlite3.IntegrityError as erro:
            return {'success': False, 'mensagem': f"Esse usuário já está cadastrado."}
        except Exception as erro:
            return {'success': False, 'mensagem': f"Ocorreu um erro ao cadastrar um usuário: {erro}"}
        finally:
            banco.desconecta_bd()

    def alterar(self):
        banco = Banco()
        try:
            banco.conecta_bd()
            if ((not self.codigo) or (not self.nome) or (not self.cpf)):
                if not self.codigo:
                    raise ValueError("O campo 'Codigo' é obrigatório")
                elif not nome:
                    raise ValueError("O campo 'Nome' é obrigatório")
                elif not cpf:
                    raise ValueError("O campo 'Cpf' é obrigatório")
            banco.cursor.execute(
                """ UPDATE usuarios SET nome = ?, cpf = ? WHERE codigo = ?""", (self.nome, self.cpf, self.codigo))
            banco.conn.commit()
            return {'success': True, 'mensagem': 'Registro alterado com sucesso.'}
        except sqlite3.IntegrityError as erro:
            return {'success': False, 'mensagem': 'Esse usuário já está cadastrado.'}
        except Exception as erro:
            return {'success': False, 'mensagem': f"Ocorreu um erro ao tentar alterar o registro: {erro}"}
        finally:
            banco.desconecta_bd()

    def deletar(self):
        banco = Banco()
        try:
            banco.conecta_bd()
            banco.cursor.execute(
                """ DELETE FROM usuarios WHERE codigo = ?""", (self.codigo))
            banco.conn.commit()
            return {'success': True, 'mensagem': 'Registro deletado com sucesso.'}
        except Exception as erro:
            return {'success': False, 'mensagem': f"Ocorreu um erro ao tentar deletar o registro: {erro}"}
        finally:
            banco.desconecta_bd()