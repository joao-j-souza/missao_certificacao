"""
Permite adicionar o diretório pai do arquivo atual ao caminho de busca de módulos (sys.path).
"""
import sys
from pathlib import Path
from model.Sistema import Sistema
# from view.sistema_lista_view import SistemaListaView


file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))


class SistemaController:
    def __init__(self):
        pass

    def adiciona_sistema(self, nome):
        """
        Método adicionar_sistema
        """
        sistema = Sistema()
        sistema.setNome(nome)
        resultado = sistema.inserir()
        return resultado

    def altera_sistema(self, codigo, nome):
        """
        Método altera_sistema
        """
        sistema = Sistema()
        sistema.setCodigo(codigo)
        sistema.setNome(nome)
        resultado = sistema.alterar()
        return resultado
    
    def apaga_sistema(self, codigo):
        """
        Método apaga_sistema
        """
        sistema = Sistema()
        sistema.setCodigo(codigo)
        resultado = sistema.deletar()
        return resultado

    def busca_sistema(self, codigo, nome):
        """
        Método busca_sistema
        """
        sistema = Sistema()
        sistema.setCodigo(codigo)
        sistema.setNome(nome)
        resultado = sistema.buscar()
        return resultado

    def lista_sistemas(self):
        """
        Método lista_sistemas
        """
        sistema = Sistema()
        resultado = sistema.listar()
        return resultado
    