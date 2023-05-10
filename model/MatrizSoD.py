"""
"""
import sqlite3
from model.Banco import Banco


class MatrizSod:
    def setCodigo(self, codigo):
        self.codigo = codigo

    def getCodigo():
        return self.codigo

    def setCodPerfil1(self, cod_perfil1):
        self.cod_perfil1 = cod_perfil1

    def getCodPerfil1():
        return self.cod_perfil1

    def setCodPerfil2(self, cod_perfil2):
        self.cod_perfil2 = cod_perfil2

    def getCodPerfil2():
        return self.cod_perfil2

    def buscar(self):
        banco = Banco()
        try:
            banco.conecta_bd()
            codigo = self.codigo if self.codigo != "" else "NULL"
            query = """ SELECT codigo, cod_perfil1, cod_perfil2 FROM matriz_sod WHERE ({0} IS NULL OR codigo = {0}) ORDER BY codigo ASC; """.format(
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

    def inserir(self):
        banco = Banco()
        try:
            banco.conecta_bd()
            banco.cursor.execute(
                """ INSERT INTO matriz_sod (cod_perfil1, cod_perfil2) VALUES (?, ?)""", (self.cod_perfil1, self.cod_perfil2))
            banco.conn.commit()
            return {'success': True, 'mensagem': 'Registro cadastrado com sucesso.'}
        except sqlite3.IntegrityError as erro:
            return {'success': False, 'mensagem': f"Essa matriz já está cadastrada."}
        except Exception as erro:
            return {'success': False, 'mensagem': f"Ocorreu um erro ao cadastrar uma matriz: {erro}"}
        finally:
            banco.desconecta_bd()

    def listar(self):
        banco = Banco()
        try:
            banco.conecta_bd()
            banco.cursor.execute(
                """ SELECT
                        matriz_sod.codigo,
                        sistema1.nome || ' - ' || perfil1.nome AS "Sistema_Perfil1",
                        sistema2.nome || ' - ' || perfil2.nome AS "Sistema_Perfil2"
                    FROM
                        matriz_sod
                    INNER JOIN
                        perfis AS perfil1 ON matriz_sod.cod_perfil1 = perfil1.codigo
                    INNER JOIN
                        perfis AS perfil2 ON matriz_sod.cod_perfil2 = perfil2.codigo
                    INNER JOIN
                        sistemas AS sistema1 ON perfil1.cod_sistema = sistema1.codigo
                    INNER JOIN
                        sistemas AS sistema2 ON perfil2.cod_sistema = sistema2.codigo; """)
            resposta = banco.cursor.fetchall()
            return {'success': True, 'resultado': resposta}
        except Exception as erro:
            return {'success': False, 'mensagem': f"Ocorreu um erro ao listar as matrizes: {erro}"}
        finally:
            banco.desconecta_bd()

    def alterar(self):
        banco = Banco()
        try:
            banco.conecta_bd()
            if (not self.cod_perfil1) or (not self.cod_perfil2):
                if not self.cod_perfil1:
                    raise ValueError("O campo 'Perfil1' é obrigatório")
                else:
                    raise ValueError("O campo 'Perfil2' é obrigatório")
            banco.cursor.execute(
                """ UPDATE matriz_sod SET cod_perfil1 = ?, cod_perfil2 = ? WHERE codigo = ?""", (self.cod_perfil1, self.cod_perfil2, self.codigo))
            banco.conn.commit()
            return {'success': True, 'mensagem': 'Registro alterado com sucesso.'}
        except sqlite3.IntegrityError as erro:
            return {'success': False, 'mensagem': 'Essa matriz já está cadastrada.'}
        except Exception as erro:
            return {'success': False, 'mensagem': f"Ocorreu um erro ao tentar alterar o registro: {erro}"}
        finally:
            banco.desconecta_bd()

    def deletar(self):
        banco = Banco()
        try:
            banco.conecta_bd()
            banco.cursor.execute(
                """ DELETE FROM matriz_sod WHERE codigo = ?""", (self.codigo))
            banco.conn.commit()
            return {'success': True, 'mensagem': 'Registro deletado com sucesso.'}
        except Exception as erro:
            return {'success': False, 'mensagem': f"Ocorreu um erro ao tentar deletar o registro: {erro}"}
        finally:
            banco.desconecta_bd()
