"""
Permite adicionar o diretório pai do arquivo atual ao caminho de busca de módulos (sys.path).
"""
import sys
from pathlib import Path
import tkinter as tk
from tkinter import ttk
from tkinter.font import Font
from tkinter import messagebox
from controller.sistema_controller import SistemaController

file = Path(__file__).resolve()
parent, master = file.parent, file.parents[1]
sys.path.append(str(master))


class Funcs():
    """
    Classe com as fuções relativas a view de sistemas.
    """

    def __init__(self):
        self.codigo_entry = None
        self.nome_entry = None

    def limpa_tela(self):
        """
        Limpa o conteúdo das entrys do formulário.
        """
        self.codigo_entry.delete(0, tk.END)
        self.nome_entry.delete(0, tk.END)
        self.lista_sistemas()

    def duplo_clique(self, event):
        """
        Preenche o formulário ao dar um duplo clique no registro da lista.
        :param event: Evento que captura o duplo clique. 
        """
        self.codigo_entry.delete(0, tk.END)
        self.nome_entry.delete(0, tk.END)        
        self.listaSistemas.selection()
        for n in self.listaSistemas.selection():
            col1, col2 = self.listaSistemas.item(n, 'values')
            self.codigo_entry.insert(tk.END, col1)
            self.nome_entry.insert(tk.END, col2)

    def exibir_mensagem(self, sistema):
        if sistema['success']:
           if "mensagem" in sistema:
                messagebox.showinfo("Informação", sistema['mensagem'])
        else:
            messagebox.showerror("Erro", sistema['mensagem'])

    def cria_sistema(self):
        """
        Função para cadastrar um sistema.
        """
        nome = self.nome_entry.get()
        if not nome:
            messagebox.showerror("Alerta!", "O Campo Nome é obrigatório!")
        else:
            controller = SistemaController()
            sistema = controller.adiciona_sistema(nome)
            self.exibir_mensagem(sistema)
            self.limpa_tela()
            self.lista_sistemas()

    def altera_sistema(self):
        """
        Função para alterar um sistema.
        """
        codigo = self.codigo_entry.get()
        nome = self.nome_entry.get()
        if not codigo:
            messagebox.showerror("Alerta!", "O Campo Código é obrigatório!")
        else:
            controller = SistemaController()
            sistema = controller.altera_sistema(codigo, nome)
            self.exibir_mensagem(sistema)
            self.lista_sistemas()

    def apaga_sistema(self):
        """
        Função para apagar um sistema.
        """
        codigo = self.codigo_entry.get()
        if not codigo:
            messagebox.showerror("Alerta!", "O Campo Código é obrigatório!")
        else:
            controller = SistemaController()
            sistema = controller.apaga_sistema(codigo)
            self.exibir_mensagem(sistema)
            self.limpa_tela()
            self.lista_sistemas()            

    def busca_sistema(self):
        """
        Método busca_sistema
        """
        codigo = self.codigo_entry.get()
        nome = self.nome_entry.get()
        controller = SistemaController()
        if (codigo or nome):
            sistema = controller.busca_sistema(codigo, nome)
            if "resultado" in sistema:                
                self.listaSistemas.delete(*self.listaSistemas.get_children())
                for s in sistema['resultado']:
                    self.listaSistemas.insert("", tk.END, values=s)
            self.exibir_mensagem(sistema)
        else:
            messagebox.showinfo("Informação", "Digite o código ou o nome.")

    def lista_sistemas(self):
        """
        Método lista_sistemas
        """
        self.listaSistemas.delete(*self.listaSistemas.get_children())
        controller = SistemaController()
        sistemas = controller.lista_sistemas()
        if sistemas['success']:
            for sistema in sistemas['resultado']:
                self.listaSistemas.insert("", tk.END, values=sistema)
        #else:
        self.exibir_mensagem(sistemas)

class SistemaView(Funcs):
    """
    Classe SistemaView
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
        self.lista_sistemas()

    def frame(self):
        """
        Método sistemas_frame
        """
        # Cria o Frame para o Form de Cadastro
        self.form = tk.Frame(self.root, bg='#dfe3ee', bd=4,
                             highlightbackground='#759fe6', highlightthickness=3)
        self.form.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.66)

    def lista_frame(self):
        """
        Método lista_frame
        """
        # Cria o Frame para a Listagem de Sistemas
        self.lista = tk.Frame(self.root, bg='#dfe3ee', bd=4,
                              highlightbackground='#759fe6', highlightthickness=3)
        self.lista.place(relx=0.02, rely=0.69, relwidth=0.96, relheight=0.29)

    def componentes(self):
        """
        Método sistemas_componentes
        """
        bt_font = Font(family="verdana", size=8, weight="bold")
        # Criação do Botão Limpar
        bt_limpar = tk.Button(self.form, text="Limpar", bd=2, bg="#107db2",
                              fg="white", font=bt_font, command=self.limpa_tela)
        bt_limpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.1)
        # Criação do Botão Buscar
        bt_buscar = tk.Button(self.form, text="Buscar", bd=2, bg="#107db2",
                              fg="white", font=bt_font, command=self.busca_sistema)
        bt_buscar.place(relx=0.305, rely=0.1, relwidth=0.1, relheight=0.1)
        # Criação do Botão Novo
        bt_novo = tk.Button(self.form, text="Novo", bd=2, bg="#107db2",
                            fg="white", font=bt_font, command=self.cria_sistema)
        bt_novo.place(relx=0.55, rely=0.1, relwidth=0.1, relheight=0.1)
        # Criação do Botão Alterar
        bt_alterar = tk.Button(self.form, text="Alterar", bd=2, bg="#107db2",
                               fg="white", font=bt_font, command=self.altera_sistema)
        bt_alterar.place(relx=0.655, rely=0.1, relwidth=0.1, relheight=0.1)
        # Criação do Botão Apagar
        bt_apagar = tk.Button(self.form, text="Apagar",
                              bd=2, bg="#107db2", fg="white", font=bt_font, command=self.apaga_sistema)
        bt_apagar.place(relx=0.76, rely=0.1, relwidth=0.1, relheight=0.1)
        # Criação da Label de Entrada do Código
        lb_codigo = tk.Label(self.form, text="Código:",
                             bg="#dfe3ee", fg="#107db2")
        lb_codigo.place(relx=0.05, rely=0.05)
        self.codigo_entry = tk.Entry(self.form)
        self.codigo_entry.place(relx=0.05, rely=0.12, relwidth=0.08)
        # Criação da Label e Entrada do nome
        lb_nome = tk.Label(self.form, text="Nome*:",
                           bg="#dfe3ee", fg="#107db2")
        lb_nome.place(relx=0.05, rely=0.3)
        self.nome_entry = tk.Entry(self.form)
        self.nome_entry.place(relx=0.14, rely=0.3, relwidth=0.78)

    def lista_componentes(self):
        """
        Método lista_componentes
        """
        self.listaSistemas = ttk.Treeview(
            self.lista, height=3, columns=("col1", "col2"))
        self.listaSistemas.heading("#0", text="")
        self.listaSistemas.heading("#1", text="Código")
        self.listaSistemas.heading("#2", text="Nome")
        self.listaSistemas.column("#0", width=10)
        self.listaSistemas.column("#1", width=40)
        self.listaSistemas.column("#2", width=350)
        self.listaSistemas.place(relx=0.01, rely=0.02,
                                 relwidth=0.95, relheight=0.95)
        scrool_lista = tk.Scrollbar(self.lista, orient="vertical")
        self.listaSistemas.configure(yscroll=scrool_lista.set)
        scrool_lista.place(relx=0.96, rely=0.02, relwidth=0.03, relheight=0.95)
        self.listaSistemas.bind("<Double-1>", self.duplo_clique)
