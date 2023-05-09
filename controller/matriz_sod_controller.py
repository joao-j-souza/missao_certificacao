"""
Permite adicionar o diretório pai do arquivo atual ao caminho de busca de módulos (sys.path).
"""
import sys
from pathlib import Path
from model.MatrizSod import MatrizSod
# from view.sistema_lista_view import SistemaListaView


file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))


class MatrizSodController:
    def __init__(self):
        pass

    def adiciona_matriz(self, perfil1, perfil2):
        """
        Método adicionar_sistema
        """
        matriz = MatrizSod()
        matriz.setCodPerfil1(perfil1)
        matriz.setCodPerfil2(perfil2)
        resultado = matriz.inserir()
        return resultado

    def altera_matriz(self, codigo, perfil1, perfil2):
        """
        Método altera_matriz
        """
        matriz = MatrizSod()
        matriz.setCodigo(codigo)
        matriz.setCodPerfil1(perfil1)
        matriz.setCodPerfil2(perfil2)
        resultado = matriz.alterar()
        return resultado
    
    def apaga_matriz(self, codigo):
        """
        Método apaga_matriz
        """
        matriz = MatrizSod()
        matriz.setCodigo(codigo)
        resultado = matriz.deletar()
        return resultado

    def busca_matriz(self, codigo):
        """
        Método busca_matriz
        """
        matriz = MatrizSod()
        matriz.setCodigo(codigo)
        resultado = matriz.buscar()
        return resultado

    def lista_matrizes(self):
        """
        Método lista_matrizes
        """
        matriz = MatrizSod()
        resultado = matriz.listar()
        return resultado
