"""
Permite adicionar o diretório pai do arquivo atual ao caminho de busca de módulos (sys.path).
"""
import sys
from pathlib import Path
from model.Sistema import Sistema
from model.MatrizSod import MatrizSod
from view.sistema_view import SistemaView
from view.matriz_sod_view import MatrizSodView

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
        Chama o método listar de SistemaDAO e passa o resultado
        como parâmetro para a classe SistemaListaView
        :param root: recebe o master 
        """
        sistema = Sistema()
        resultado = sistema.listar()
        SistemaView(self.root, resultado)

    def lista_matrizes_sod(self):
        """
        Chama o método listar de MatrizSoD e passa o resultado
        como parâmetro para a classe MatrizSoDView
        :param root: recebe o master
        """
        matriz = MatrizSod()
        resultado = matriz.listar()
        MatrizSodView(self.root, resultado)
