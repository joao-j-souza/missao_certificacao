"""
"""
import sqlite3
from model.Banco import Banco


class UsuarioPerfil:
    def __init__(self):
        self.codigo = ""
        self.cod_usuario = ""
        self.cod_perfil = ""

    def setCodigo(self, codigo):
        self.codigo = codigo

    def getCodigo(self):
        return self.codigo

    def setCodUsuario(self, cod_usuario):
        self.cod_usuario = cod_usuario

    def getCodUsuario(self):
        return self.cod_usuario

    def setCodPerfil(self, cod_perfil):
        self.cod_perfil = cod_perfil

    def getCodPerfil(self):
        return self.cod_perfil

    def buscar(self):
        banco = Banco()
        try:
            banco.conecta_bd()
            codigo = self.codigo if self.codigo != "" else None
            cod_usuario = self.cod_usuario if self.cod_usuario != "" else None
            banco.cursor.execute(""" SELECT codigo, cod_usuario, cod_perfil FROM usuarios_perfis WHERE (codigo IS NULL or codigo = ?) OR (cod_usuario IS NULL OR cod_usuario = ?) ORDER BY codigo ASC """,(self.codigo, self.cod_usuario))
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
                """ INSERT INTO usuarios_perfis (cod_usuario, cod_perfil) VALUES (?, ?)""", (self.cod_usuario, self.cod_perfil))
            banco.conn.commit()
            return {'success': True, 'mensagem': 'Registro cadastrado com sucesso.'}
        except sqlite3.IntegrityError as erro:
            return {'success': False, 'mensagem': f"Usuário já tem esse perfil."}
        except Exception as erro:
            return {'success': False, 'mensagem': f"Ocorreu um erro ao cadastrar um perfil para um usuário: {erro}"}
        finally:
            banco.desconecta_bd()            

    def listar(self):
        banco = Banco()
        try:
            banco.conecta_bd()
            codigo = self.codigo if self.codigo != "" else "NULL"
            query = f""" SELECT 
                        up.codigo,
                        u.nome || ' - ' || u.cpf,
                        s.nome || ' - ' || p.nome AS "Sistema_Perfil"	
                    FROM
                        usuarios_perfis up
                    INNER JOIN perfis p ON
                        p.codigo = up.cod_perfil
                    INNER JOIN usuarios u ON
                        u.codigo = up.cod_usuario 
                    INNER JOIN sistemas s ON
                        s.codigo = p.cod_sistema
                    WHERE ({codigo} IS NULL OR up.codigo = {codigo}); """
            banco.cursor.execute(query)
            resposta = banco.cursor.fetchall()
            return {'success': True, 'resultado': resposta}
        except Exception as erro:
            return {'success': False, 'mensagem': f"Ocorreu o seguinte erro: {erro}"}
        finally:
            banco.desconecta_bd()

    def alterar(self):
        banco = Banco()
        try:
            banco.conecta_bd()
            if (not self.cod_usuario) or (not self.cod_perfil):
                if not self.cod_usuario:
                    raise ValueError("O campo 'Código do Usuário' é obrigatório")
                else:
                    raise ValueError("O campo 'Perfil' é obrigatório")
            banco.cursor.execute(
                """ UPDATE usuarios_perfis SET cod_usuario = ?, cod_perfil = ? WHERE codigo = ?""", (self.cod_usuario, self.cod_perfil, self.codigo))
            banco.conn.commit()
            return {'success': True, 'mensagem': 'Registro alterado com sucesso.'}
        except sqlite3.IntegrityError as erro:
            return {'success': False, 'mensagem': "Usuário já tem acesso a esse perfil."}
        except Exception as erro:
            return {'success': False, 'mensagem': f"Ocorreu um erro ao tentar alterar o registro: {erro}"}
        finally:
            banco.desconecta_bd()

    def deletar(self):
        banco = Banco()
        try:
            banco.conecta_bd()
            banco.cursor.execute(
                """ DELETE FROM usuarios_perfis WHERE codigo = ?""", (self.codigo))
            banco.conn.commit()
            return {'success': True, 'mensagem': 'Registro deletado com sucesso.'}
        except Exception as erro:
            return {'success': False, 'mensagem': f"Ocorreu um erro ao tentar deletar o registro: {erro}"}
        finally:
            banco.desconecta_bd()