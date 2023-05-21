"""
Permite adicionar o diretório pai do arquivo atual ao caminho de busca de módulos (sys.path).
"""
import sys
from pathlib import Path
from model.UsuarioPerfil import UsuarioPerfil
from model.MatrizSod import MatrizSod

file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))


class UsuarioPerfilController:
    def __init__(self):
        pass

    def adiciona_usuario_perfil(self, cod_usuario, cod_perfil):
        """
        Método adiciona_usuario_perfil
        """
        u_perfil = UsuarioPerfil()
        u_perfil.setCodUsuario(cod_usuario)
        u_perfil.setCodPerfil(cod_perfil)

        lst_usuario_perfis = u_perfil.buscar()
        u_perfis = []

        if 'resultado' in lst_usuario_perfis:
            m_sod = MatrizSod()
            lst_matrizes_sod = m_sod.listar()
            for lup in lst_usuario_perfis['resultado']:
                u_perfis.append(f"{lup[2]}_{cod_perfil}")
            u_perfis = sorted(u_perfis)

            if 'resultado' in lst_matrizes_sod:
                for up in u_perfis:
                    for lms in lst_matrizes_sod['resultado']:
                        if lms[3] == up:
                            resultado = {'success': True, 'mensagem': f"MatrizSoD detectada!!! {lms[3]}"}
                            return resultado
        resultado = u_perfil.inserir()
        return resultado

    def altera_usuario_perfil(self, codigo, cod_usuario, cod_perfil):
        """
        Método altera_usuario_perfil
        """
        usuario_perfil = UsuarioPerfil()
        usuario_perfil.setCodigo(codigo)
        usuario_perfil.setCodUsuario(cod_usuario)
        usuario_perfil.setCodPerfil(cod_perfil)
        resultado = usuario_perfil.alterar()
        return resultado

    def apaga_usuario_perfil(self, codigo):
        """
        Método apaga_usuario_perfil
        """
        usuario_perfil = UsuarioPerfil()
        usuario_perfil.setCodigo(codigo)
        resultado = usuario_perfil.deletar()
        return resultado

    def busca_usuario_perfil(self):
        """
        Método busca_usuario_perfil
        """

    def lista_usuarios_perfis(self):
        """
        Método lista_usuario_perfil
        """   
        usuario_perfil = UsuarioPerfil()
        resultado = usuario_perfil.listar()
        return resultado