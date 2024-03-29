"""
Permite adicionar o diretório pai do arquivo atual ao caminho de busca de módulos (sys.path).
"""
import sys
from pathlib import Path
from model.Perfil import Perfil


file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))


class PerfilController:
    def __init__(self):
        pass

    def adiciona_perfil(self, cod_sistema, nome, descricao):
        """
        Método adicionar_perfil
        """
        perfil = Perfil()
        perfil.setCodSistema(cod_sistema)
        perfil.setNome(nome)
        perfil.setDescricao(descricao)
        resultado = perfil.inserir()
        return resultado

    def altera_perfil(self, codigo, cod_sistema, nome, descricao):
        """
        Método altera_perfil
        """
        perfil = Perfil()
        perfil.setCodigo(codigo)
        perfil.setCodSistema(cod_sistema)        
        perfil.setNome(nome)
        perfil.setDescricao(descricao)
        resultado = perfil.alterar()
        return resultado
    
    def apaga_perfil(self, codigo):
        """
        Método apaga_perfil
        """
        perfil = Perfil()
        perfil.setCodigo(codigo)
        resultado = perfil.deletar()
        return resultado

    def busca_perfil(self, codigo):
        """
        Método busca_perfil
        """
        perfil = Perfil()
        perfil.setCodigo(codigo)
        resultado = perfil.listar_cb()
        return resultado

    def lista_perfis(self):
        """
        Método lista_perfis
        """
        perfil = Perfil()
        resultado = perfil.listar()
        return resultado
    
    def lista_perfis_cb(self):
        """
        Cria uma instância da classe Perfil e invoca o método listar_cb através do objeto instanciado.
        """
        perfil = Perfil()
        resultado = perfil.listar_cb()
        return resultado
