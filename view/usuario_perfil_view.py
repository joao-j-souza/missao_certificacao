"""
Permite adicionar o diretório pai do arquivo atual ao caminho de busca de módulos (sys.path).
"""
import sys
from pathlib import Path
import tkinter as tk
from tkinter import ttk
from tkinter.font import Font
from tkinter import messagebox
from tkinter import StringVar
from view.uteis import CustomCombobox
from controller.usuario_perfil_controller import UsuarioPerfilController
from controller.usuario_controller import UsuarioController    
from controller.perfil_controller import PerfilController

file = Path(__file__).resolve()
parent, master = file.parent, file.parents[1]
sys.path.append(str(master))


class Funcs():
    """
    Classe com as fuções relativas a view da matrizSod.
    """

    def __init__(self):
        self.codigo_entry = None
        self.codigo_usuario_cb = None
        self.codigo_perfil_cb = None

    def limpa_tela(self):
        """
        Limpa o conteúdo das entrys do formulário.
        """
        self.codigo_entry.delete(0, tk.END)
        self.codigo_usuario_cb.delete(0, tk.END)
        self.codigo_perfil_cb.delete(0, tk.END)
        self.lista_usuarios_perfis()

    def duplo_clique(self, event):
        """
        Preenche o formulário ao dar um duplo clique no registro da lista.
        :param event: Evento que captura o duplo clique. 
        """
        self.codigo_entry.delete(0, tk.END)
        self.codigo_usuario_cb.delete(0, tk.END)
        self.codigo_perfil_cb.delete(0, tk.END)

        self.listaUsuariosPerfis.selection()
        for n in self.listaUsuariosPerfis.selection():
            col1, col2, col3 = self.listaUsuariosPerfis.item(n, 'values')
        self.codigo_entry.insert(tk.END, col1)
        self.codigo_usuario_cb.insert(tk.END, col2)
        self.codigo_perfil_cb.insert(tk.END, col3)

    def exibir_mensagem(self, usuario_perfil):
        if usuario_perfil['success']:
            if "mensagem" in usuario_perfil:
                messagebox.showinfo("Informação", usuario_perfil['mensagem'])
        else:
            messagebox.showerror("Erro", usuario_perfil['mensagem'])

    def cria_usuario_perfil(self):
        """
        Função para cadastrar um usuario_perfil.
        """
        # Obtendo o código correspondente aos valores selecionados
        cod_usuario = self.codigo_usuario_cb["values_id"][self.codigo_usuario_cb.current(
        )]
        cod_perfil = self.codigo_perfil_cb["values_id"][self.codigo_perfil_cb.current(
        )]

        if (not cod_usuario) or (not cod_perfil):
            if not cod_usuario:
                messagebox.showerror(
                    "Alerta!", "O Campo Usuário é obrigatório!")
            else:
                messagebox.showerror(
                    "Alerta!", "O Campo Perfil é obrigatório!")
        else:
            controller = UsuarioPerfilController()
            usuario_perfil = controller.adiciona_usuario_perfil(cod_usuario, cod_perfil)
            self.exibir_mensagem(usuario_perfil)
            self.limpa_tela()
            self.lista_usuarios_perfis()

    def altera_usuario_perfil(self):
        """
        Função para alterar um usuario_perfil.
        """
        codigo = self.codigo_entry.get()
        cod_usuario = self.codigo_usuario_cb.get()
        cod_perfil = self.codigo_perfil_cb.get()
        if (not cod_usuario) or (not cod_perfil):
            if not cod_usuario:
                messagebox.showerror(
                    "Alerta!", "O Campo Usuario é obrigatório!")
            else:
                messagebox.showerror(
                    "Alerta", "O Campo Perfil é obrigatório!")
        else:
            controller = UsuarioPerfilController()
            usuario_perfil = controller.altera_usuario_perfil(codigo, cod_usuario, cod_perfil)
            self.exibir_mensagem(usuario_perfil)
            self.lista_usuarios_perfis()

    def apaga_usuario_perfil(self):
        """
        Função para apagar um usuario_perfil.
        """
        codigo = self.codigo_entry.get()
        if not codigo:
            messagebox.showerror("Alerta!", "O Campo Código é obrigatório!")
        else:
            controller = UsuarioPerfilController()
            usuario_perfil = controller.apaga_usuario_perfil(codigo)
            self.exibir_mensagem(usuario_perfil)
            self.limpa_tela()
            self.lista_usuarios_perfis()

    def busca_usuario_perfil(self):
        """
        Método busca_usuario_perfi
        """
        codigo = self.codigo_entry.get()
        # nome = self.nome_entry.get()
        controller = UsuarioPerfilController()
        # if (codigo or nome):
        if codigo:
            usuario_perfil = controller.busca_usuario_perfil(codigo)
            if "resultado" in usuario_perfil:
                self.listaUsuarioPerfis.delete(*self.listaUsuarioPerfis.get_children())
                for s in usuario_perfil['resultado']:
                    self.listaUsuarioPerfis.insert("", tk.END, values=s)
            self.exibir_mensagem(usuario_perfil)
        else:
            # messagebox.showinfo("Informação", "Digite o código ou o nome.")
            messagebox.showinfo("Informação", "Digite o código.")

    def lista_usuarios_perfis(self):
        """
        Método lista_usuarios_perfis
        """
        self.listaUsuariosPerfis.delete(*self.listaUsuariosPerfis.get_children())
        controller = UsuarioPerfilController()
        usuarios_perfis = controller.lista_usuarios_perfis()
        if usuarios_perfis['success']:
            for usuario_perfil in usuarios_perfis['resultado']:
                self.listaUsuariosPerfis.insert("", tk.END, values=usuario_perfil)
        self.exibir_mensagem(usuarios_perfis)

    def popula_combos(self):
        controller = PerfilController()
        # Buscando os perfis no banco de dados
        perfis = controller.lista_perfis_cb()

        # Criando uma lista de valores para o combobox, contendo o nome do perfil
        values = [value[1] for value in perfis["resultado"]]

        # Criando uma lista de valores para o combobox, contendo o código do perfil
        codigos = [value[0] for value in perfis["resultado"]]

        # Configurando as opções do combobox para exibir o nome do perfil e retornar o código correspondente
        self.codigo_perfil_cb["values"] = values
        self.codigo_perfil_cb["values_id"] = codigos

        controller = UsuarioController()
        # Buscando os usuários no banco de dados
        usuarios = controller.lista_usuarios_cb()

        # Criando uma lista de valores para o combobox, contendo o nome do usuário
        values = [value[1] for value in usuarios["resultado"]]

        # Criando uma lista de valores para o combobox, contendo o código do usuário
        codigos = [value[0] for value in usuarios["resultado"]]

        # Configurando as opções do combobox para exibir o nome do usuário e retornar o código correspondente
        self.codigo_usuario_cb["values"] = values
        self.codigo_usuario_cb["values_id"] = codigos


class UsuarioPerfilView(Funcs):
    """
    Classe UsuarioPerfilView
    """

    def __init__(self, root=None, resultado=None):
        """
        Método init
        """
        self.root = root
        self.resultado = resultado
        self.frame()  # Chama o método que define o frame para o form.
        self.lista_frame()  # Chama o método que define o frame para a lista.
        # Chama o método que configura os componentes no frame.
        self.componentes()
        self.lista_componentes()
        self.lista_usuarios_perfis()
        self.popula_combos()

    def frame(self):
        """
        Método usuario_perfis_frame
        """
        # Cria o Frame para o Form de Cadastro
        self.form = tk.Frame(self.root, bg='#dfe3ee', bd=4,
                             highlightbackground='#759fe6', highlightthickness=3)
        self.form.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.66)

    def lista_frame(self):
        """
        Método lista_frame
        """
        # Cria o Frame para a Listagem de UsuarioPerfis
        self.lista = tk.Frame(self.root, bg='#dfe3ee', bd=4,
                              highlightbackground='#759fe6', highlightthickness=3)
        self.lista.place(relx=0.02, rely=0.69, relwidth=0.96, relheight=0.29)

    def componentes(self):
        """
        Método usuario_perfis_componentes
        """
        bt_font = Font(family="verdana", size=8, weight="bold")
        # Criação do Botão Limpar
        bt_limpar = tk.Button(self.form, text="Limpar", bd=2, bg="#107db2",
                              fg="white", font=bt_font, command=self.limpa_tela)
        bt_limpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.1)
        # Criação do Botão Buscar
        bt_buscar = tk.Button(self.form, text="Buscar", bd=2, bg="#107db2",
                              fg="white", font=bt_font, command=self.busca_usuario_perfil)
        bt_buscar.place(relx=0.305, rely=0.1, relwidth=0.1, relheight=0.1)
        # Criação do Botão Novo
        bt_novo = tk.Button(self.form, text="Novo", bd=2, bg="#107db2",
                            fg="white", font=bt_font, command=self.cria_usuario_perfil)
        bt_novo.place(relx=0.55, rely=0.1, relwidth=0.1, relheight=0.1)
        # Criação do Botão Alterar
        bt_alterar = tk.Button(self.form, text="Alterar", bd=2, bg="#107db2",
                               fg="white", font=bt_font, command=self.altera_usuario_perfil)
        bt_alterar.place(relx=0.655, rely=0.1, relwidth=0.1, relheight=0.1)
        # Criação do Botão Apagar
        bt_apagar = tk.Button(self.form, text="Apagar",
                              bd=2, bg="#107db2", fg="white", font=bt_font, command=self.apaga_usuario_perfil)
        bt_apagar.place(relx=0.76, rely=0.1, relwidth=0.1, relheight=0.1)
        # Criação da Label de Entrada do Código
        lb_codigo = tk.Label(self.form, text="Código:",
                             bg="#dfe3ee", fg="#107db2")
        lb_codigo.place(relx=0.05, rely=0.05)
        self.codigo_entry = tk.Entry(self.form)
        self.codigo_entry.place(relx=0.05, rely=0.12, relwidth=0.08)

        # Criação da Label e Entrada do usuario
        lb_usuario = tk.Label(self.form, text="Usuário*:",
                              bg="#dfe3ee", fg="#107db2")
        lb_usuario.place(relx=0.05, rely=0.4)

        cod_usuario = StringVar()

        self.codigo_usuario_cb = CustomCombobox(
            self.form, textvariable=cod_usuario)
        self.codigo_usuario_cb.place(relx=0.22, rely=0.4, relwidth=0.72)

        # Criação da Label e Entrada do perfil
        lb_perfil = tk.Label(self.form, text="Sistema - Perfil*:",
                              bg="#dfe3ee", fg="#107db2")
        lb_perfil.place(relx=0.05, rely=0.6)

        cod_perfil = StringVar()

        self.codigo_perfil_cb = CustomCombobox(
            self.form, textvariable=cod_perfil)
        self.codigo_perfil_cb.place(relx=0.22, rely=0.6, relwidth=0.72)

    def lista_componentes(self):
        """
        Método lista_componentes
        """
        self.listaUsuariosPerfis = ttk.Treeview(
            self.lista, height=3, columns=("col1", "col2", "col3"))
        self.listaUsuariosPerfis.heading("#0", text="")
        self.listaUsuariosPerfis.heading("#1", text="Código")
        self.listaUsuariosPerfis.heading("#2", text="Usuário")
        self.listaUsuariosPerfis.heading("#3", text="Perfil")
        self.listaUsuariosPerfis.column("#0", width=10)
        self.listaUsuariosPerfis.column("#1", width=40)
        self.listaUsuariosPerfis.column("#2", width=175)
        self.listaUsuariosPerfis.column("#3", width=175)
        self.listaUsuariosPerfis.place(relx=0.01, rely=0.02,
                                 relwidth=0.95, relheight=0.95)
        scrool_lista = tk.Scrollbar(self.lista, orient="vertical")
        self.listaUsuariosPerfis.configure(yscroll=scrool_lista.set)
        scrool_lista.place(relx=0.96, rely=0.02, relwidth=0.03, relheight=0.95)
        self.listaUsuariosPerfis.bind("<Double-1>", self.duplo_clique)
