"""
Permite adicionar o diretório pai do arquivo atual ao caminho de busca de módulos (sys.path).
"""
import sys
from pathlib import Path
from model.Sistema import Sistema
from model.Perfil import Perfil
from model.MatrizSod import MatrizSod
from model.Usuario import Usuario
from model.UsuarioPerfil import UsuarioPerfil
from view.sistema_view import SistemaView
from view.perfil_view import PerfilView
from view.matriz_sod_view import MatrizSodView
from view.usuario_view import UsuarioView
from view.usuario_perfil_view import UsuarioPerfilView

file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

class MainController:
    """
    Classe MainController
    """
    def __init__(self, master):
        """
        Método init
        """
        self.root = master

    def lista_sistemas(self):
        """
        Chama o método listar de Sistema e passa o resultado
        como parâmetro para a classe SistemaListaView
        :param root: recebe o master 
        """
        sistema = Sistema()
        resultado = sistema.listar()
        SistemaView(self.root, resultado)

    def lista_perfis(self):
        """
        Chama o método listar de Perfil e passa o resultado
        como parâmetro para a classe PerfilListaView
        :param root: recebe o master 
        """
        perfil = Perfil()
        resultado = perfil.listar()
        PerfilView(self.root, resultado)

    def lista_matrizes_sod(self):
        """
        Chama o método listar de MatrizSoD e passa o resultado
        como parâmetro para a classe MatrizSoDView
        :param root: recebe o master
        """
        matriz = MatrizSod()
        resultado = matriz.listar_cb()
        MatrizSodView(self.root, resultado)

    def lista_usuarios(self):
        """
        Chama o método listar de Usuario e passa o resultado
        como parâmetro para a classe UsuarioView
        :param root: recebe o master
        """
        usuario = Usuario()
        resultado = usuario.listar()
        UsuarioView(self.root, resultado)

    def lista_usuarios_perfis(self):
        """
        Chama o método listar de UsuariosPerfis e passa o resultado
        como parâmetro para a classe MatrizSoDView
        :param root: recebe o master
        """
        usuario_perfil = UsuarioPerfil()
        resultado = usuario_perfil.listar()
        UsuarioPerfilView(self.root, resultado)
