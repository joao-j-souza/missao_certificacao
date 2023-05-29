"""
Permite adicionar o diretório pai do arquivo atual ao caminho de busca de módulos (sys.path).
"""
import sys
from pathlib import Path
from model.Usuario import Usuario


file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))


class UsuarioController:
    def __init__(self):
        pass

    def adiciona_usuario(self, nome, cpf):
        """
        Método adiciona_usuario
        """
        usuario = Usuario()
        usuario.setNome(nome)
        usuario.setCpf(cpf)
        resultado = usuario.inserir()
        return resultado

    def altera_usuario(self, codigo, nome, cpf):
        """
        Método altera_usuario
        """
        usuario = Usuario()
        usuario.setCodigo(codigo)
        usuario.setNome(nome)
        usuario.setCpf(cpf)
        resultado = usuario.alterar()
        return resultado
    
    def apaga_usuario(self, codigo):
        """
        Método apaga_usuario
        """
        usuario = Usuario()
        usuario.setCodigo(codigo)
        resultado = usuario.deletar()
        return resultado

    def busca_usuario(self, codigo, cpf):
        """
        Método busca_usuario
        """
        usuario = Usuario()
        usuario.setCodigo(codigo)
        usuario.setCpf(cpf)
        resultado = usuario.buscar()
        return resultado

    def lista_usuarios(self):
        """
        Método lista_usuarios
        """
        usuario = Usuario()
        resultado = usuario.listar()
        return resultado
    
    def lista_usuarios_cb(self):
        """
        Método lista_usuarios_cb
        """
        usuario = Usuario()
        resultado = usuario.listar_cb()
        return resultado
