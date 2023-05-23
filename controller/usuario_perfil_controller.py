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
        usuario_perfil = UsuarioPerfil()
        usuario_perfil.setCodUsuario(cod_usuario)
        usuario_perfil.setCodPerfil(cod_perfil)
        resposta = self.valida_matriz_sod(usuario_perfil)
        if resposta['success']:
            return resposta
        resposta = usuario_perfil.inserir()
        return resposta

    def altera_usuario_perfil(self, codigo, cod_usuario, cod_perfil):
        """
        Método altera_usuario_perfil
        """
        usuario_perfil = UsuarioPerfil()
        usuario_perfil.setCodigo(codigo)
        usuario_perfil.setCodUsuario(cod_usuario)
        usuario_perfil.setCodPerfil(cod_perfil)
        resposta = self.valida_matriz_sod(usuario_perfil)
        if resposta['success']:
            return resposta
        resposta = usuario_perfil.alterar()
        return resposta

    def apaga_usuario_perfil(self, codigo):
        """
        Método apaga_usuario_perfil
        """
        usuario_perfil = UsuarioPerfil()
        usuario_perfil.setCodigo(codigo)
        resultado = usuario_perfil.deletar()
        return resultado

    def busca_usuario_perfil(self, codigo):
        """
        Método busca_usuario_perfil
        """
        usuario_perfil = UsuarioPerfil()
        usuario_perfil.setCodigo(codigo)
        resposta = usuario_perfil.listar()
        return resposta

    def lista_usuarios_perfis(self):
        """
        Método lista_usuario_perfil
        """   
        usuario_perfil = UsuarioPerfil()
        resultado = usuario_perfil.listar()
        return resultado
    
    def valida_matriz_sod(self, u_perfil):
        """
        Método valida_matriz_sod
        """
        m_sod = MatrizSod()
        lst_usuario_perfis = u_perfil.buscar()
        lst_matrizes_sod = m_sod.listar()
        u_perfis = []
        if 'resultado' in lst_usuario_perfis:
            for lups in lst_usuario_perfis['resultado']:
                if(lups[2] > u_perfil.getCodPerfil()):
                    u_perfis.append(f"{u_perfil.getCodPerfil}_{lups[2]}")
                else:
                    u_perfis.append(f"{lups[2]}_{u_perfil.getCodPerfil()}")
        if 'resultado' in lst_matrizes_sod:
            for ups in u_perfis:
                for lms in lst_matrizes_sod['resultado']:
                    if lms[3] == ups:
                        return {'success': True, 'mensagem': f"MatrizSoD detectada!!! {lms[3]}"}
        return {'success': False}
    