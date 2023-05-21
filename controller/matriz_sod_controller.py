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

    def adiciona_matriz(self, p1, p2):
        """
        Método adicionar_matriz
        """
        perfil1 = None
        perfil2 = None
        if p1 == p2:
            return {'success': False, 'mensagem': "Os perfis não podem ser os mesmos."}
        else:
            if p1 < p2:
                perfil1 = p1
                perfil2 = p2
            else:
                perfil1 = p2
                perfil2 = p1
        matriz = MatrizSod()
        matriz.setCodPerfil1(perfil1)
        matriz.setCodPerfil2(perfil2)
        matriz.setConcat(f"{perfil1}_{perfil2}")
        resultado = matriz.inserir()
        return resultado

    def altera_matriz(self, codigo, p1, p2):
        """
        Método altera_matriz
        """
        if p1 == p2:
            return {'success': False, 'mensagem': "Os perfis não podem ser os mesmos."}
        else:
            if p1 < p2:
                perfil1 = p1
                perfil2 = p2
            else:
                perfil1 = p2
                perfil2 = p1
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
        resultado = matriz.listar_cb()
        return resultado
