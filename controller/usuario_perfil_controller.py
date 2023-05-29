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
        resposta = self.valida_matriz_sod(usuario_perfil, 'adiciona')
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
        resposta = self.valida_matriz_sod(usuario_perfil, 'altera')
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

    def valida_matriz_sod(self, u_perfil, metodo):
        """
        Método valida_matriz_sod
        """

        lst_usuario_perfis = u_perfil.buscar()
        m_sod = MatrizSod()
        lst_matrizes_sod = m_sod.listar()

        if (('resultado' in lst_matrizes_sod) and ('resultado' in lst_usuario_perfis)):

            if not((metodo == 'altera') and (len(lst_usuario_perfis['resultado'])==1)):
                matriz = None
                for lups in lst_usuario_perfis['resultado']:
                    if(lups[2] > u_perfil.getCodPerfil()):
                        matriz = f"{u_perfil.getCodPerfil()}_{lups[2]}"
                    else:
                        matriz = f"{lups[2]}_{u_perfil.getCodPerfil()}"
                    for lms in lst_matrizes_sod['resultado']:
                        if lms[3] == matriz:
                            return {'success': True, 'mensagem': "MatrizSoD detectada!!!"}

        return {'success': False}
