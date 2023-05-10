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
from controller.matriz_sod_controller import MatrizSodController
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
        self.codigo_perfil1_cb = None
        self.codigo_perfil2_cb = None

    def limpa_tela(self):
        """
        Limpa o conteúdo das entrys do formulário.
        """
        self.codigo_entry.delete(0, tk.END)
        self.codigo_perfil1_cb.delete(0, tk.END)
        self.codigo_perfil2_cb.delete(0, tk.END)
        self.lista_matrizes()

    def duplo_clique(self, event):
        """
        Preenche o formulário ao dar um duplo clique no registro da lista.
        :param event: Evento que captura o duplo clique. 
        """
        self.codigo_entry.delete(0, tk.END)
        self.codigo_perfil1_cb.delete(0, tk.END)
        self.codigo_perfil2_cb.delete(0, tk.END)

        self.listaMatrizes.selection()
        for n in self.listaMatrizes.selection():
            col1, col2, col3 = self.listaMatrizes.item(n, 'values')
        self.codigo_entry.insert(tk.END, col1)
        self.codigo_perfil1_cb.insert(tk.END, col2)
        self.codigo_perfil2_cb.insert(tk.END, col3)

    def exibir_mensagem(self, matriz):
        if matriz['success']:
            if "mensagem" in matriz:
                messagebox.showinfo("Informação", matriz['mensagem'])
        else:
            messagebox.showerror("Erro", matriz['mensagem'])

    def cria_matriz(self):
        """
        Função para cadastrar uma matriz.
        """
        # Obtendo o código correspondente aos valores selecionados
        perfil1_codigo = self.codigo_perfil1_cb["values_id"][self.codigo_perfil1_cb.current(
        )]
        perfil2_codigo = self.codigo_perfil2_cb["values_id"][self.codigo_perfil2_cb.current(
        )]

        print(perfil1_codigo, perfil2_codigo)

        if (not perfil1_codigo) or (not perfil2_codigo):
            if not perfil1_codigo:
                messagebox.showerror(
                    "Alerta!", "O Campo Perfil1 é obrigatório!")
            else:
                messagebox.showerror(
                    "Alerta!", "O Campo Perfil2 é obrigatório!")
        else:
            controller = MatrizSodController()
            matriz = controller.adiciona_matriz(perfil1_codigo, perfil2_codigo)
            self.exibir_mensagem(matriz)
            self.limpa_tela()
            self.lista_matrizes()

    def altera_matriz(self):
        """
        Função para alterar uma matriz.
        """
        codigo = self.codigo_entry.get()
        perfil1 = self.codigo_perfil1_cb.get()
        perfil2 = self.codigo_perfil2_cb.get()
        if (not perfil1) or (not perfil2):
            if not perfil1:
                messagebox.showerror(
                    "Alerta!", "O Campo Perfil1 é obrigatório!")
            else:
                messagebox.showerror(
                    "Alerta", "O Campo Perfil2 é obrigatório!")
        else:
            controller = MatrizSodController()
            matriz = controller.altera_matriz(codigo, perfil1, perfil2)
            self.exibir_mensagem(matriz)
            self.lista_matrizes()

    def apaga_matriz(self):
        """
        Função para apagar uma matriz.
        """
        codigo = self.codigo_entry.get()
        if not codigo:
            messagebox.showerror("Alerta!", "O Campo Código é obrigatório!")
        else:
            controller = MatrizSodController()
            matriz = controller.apaga_matriz(codigo)
            self.exibir_mensagem(matriz)
            self.limpa_tela()
            self.lista_matrizes()

    def busca_matriz(self):
        """
        Método busca_matriz
        """
        codigo = self.codigo_entry.get()
        # nome = self.nome_entry.get()
        controller = MatrizSodController()
        # if (codigo or nome):
        if codigo:
            matriz = controller.busca_matriz(codigo)
            if "resultado" in matriz:
                self.listaMatrizes.delete(*self.listaMatrizes.get_children())
                for s in matriz['resultado']:
                    self.listaMatrizes.insert("", tk.END, values=s)
            self.exibir_mensagem(matriz)
        else:
            # messagebox.showinfo("Informação", "Digite o código ou o nome.")
            messagebox.showinfo("Informação", "Digite o código.")

    def lista_matrizes(self):
        """
        Método lista_matrizes
        """
        self.listaMatrizes.delete(*self.listaMatrizes.get_children())
        controller = MatrizSodController()
        matrizes = controller.lista_matrizes()
        if matrizes['success']:
            for matriz in matrizes['resultado']:
                self.listaMatrizes.insert("", tk.END, values=matriz)
        self.exibir_mensagem(matrizes)

    def popula_combos(self):
        controller = PerfilController()
        # Buscando os perfis no banco de dados
        perfis = controller.lista_perfis_cb()

        # Criando uma lista de valores para o combobox, contendo o nome do perfil
        values = [value[1] for value in perfis["resultado"]]

        # Criando uma lista de valores para o combobox, contendo o código do perfil
        codigos = [value[0] for value in perfis["resultado"]]

        # Configurando as opções do combobox para exibir o nome do perfil e retornar o código correspondente
        self.codigo_perfil1_cb["values"] = values
        self.codigo_perfil1_cb["values_id"] = codigos

        # Configurando as opções do combobox para exibir o nome do perfil e retornar o código correspondente
        self.codigo_perfil2_cb["values"] = values
        self.codigo_perfil2_cb["values_id"] = codigos


class MatrizSodView(Funcs):
    """
    Classe MatrizSodView
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
        self.lista_matrizes()
        self.popula_combos()

    def frame(self):
        """
        Método matrizes_frame
        """
        # Cria o Frame para o Form de Cadastro
        self.form = tk.Frame(self.root, bg='#dfe3ee', bd=4,
                             highlightbackground='#759fe6', highlightthickness=3)
        self.form.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.66)

    def lista_frame(self):
        """
        Método lista_frame
        """
        # Cria o Frame para a Listagem de Matrizes
        self.lista = tk.Frame(self.root, bg='#dfe3ee', bd=4,
                              highlightbackground='#759fe6', highlightthickness=3)
        self.lista.place(relx=0.02, rely=0.69, relwidth=0.96, relheight=0.29)

    def componentes(self):
        """
        Método matrizes_componentes
        """
        bt_font = Font(family="verdana", size=8, weight="bold")
        # Criação do Botão Limpar
        bt_limpar = tk.Button(self.form, text="Limpar", bd=2, bg="#107db2",
                              fg="white", font=bt_font, command=self.limpa_tela)
        bt_limpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.1)
        # Criação do Botão Buscar
        bt_buscar = tk.Button(self.form, text="Buscar", bd=2, bg="#107db2",
                              fg="white", font=bt_font, command=self.busca_matriz)
        bt_buscar.place(relx=0.305, rely=0.1, relwidth=0.1, relheight=0.1)
        # Criação do Botão Novo
        bt_novo = tk.Button(self.form, text="Novo", bd=2, bg="#107db2",
                            fg="white", font=bt_font, command=self.cria_matriz)
        bt_novo.place(relx=0.55, rely=0.1, relwidth=0.1, relheight=0.1)
        # Criação do Botão Alterar
        bt_alterar = tk.Button(self.form, text="Alterar", bd=2, bg="#107db2",
                               fg="white", font=bt_font, command=self.altera_matriz)
        bt_alterar.place(relx=0.655, rely=0.1, relwidth=0.1, relheight=0.1)
        # Criação do Botão Apagar
        bt_apagar = tk.Button(self.form, text="Apagar",
                              bd=2, bg="#107db2", fg="white", font=bt_font, command=self.apaga_matriz)
        bt_apagar.place(relx=0.76, rely=0.1, relwidth=0.1, relheight=0.1)
        # Criação da Label de Entrada do Código
        lb_codigo = tk.Label(self.form, text="Código:",
                             bg="#dfe3ee", fg="#107db2")
        lb_codigo.place(relx=0.05, rely=0.05)
        self.codigo_entry = tk.Entry(self.form)
        self.codigo_entry.place(relx=0.05, rely=0.12, relwidth=0.08)

        # Criação da Label e Entrada do perfil1
        lb_perfil1 = tk.Label(self.form, text="Sistema - Perfil*:",
                              bg="#dfe3ee", fg="#107db2")
        lb_perfil1.place(relx=0.05, rely=0.4)

        cod_perfil1 = StringVar()

        self.codigo_perfil1_cb = CustomCombobox(
            self.form, textvariable=cod_perfil1)
        self.codigo_perfil1_cb.place(relx=0.22, rely=0.4, relwidth=0.72)

        # Criação da Label e Entrada do perfil2
        lb_perfil2 = tk.Label(self.form, text="Sistema - Perfil*:",
                              bg="#dfe3ee", fg="#107db2")
        lb_perfil2.place(relx=0.05, rely=0.6)

        cod_perfil2 = StringVar()

        self.codigo_perfil2_cb = CustomCombobox(
            self.form, textvariable=cod_perfil2)
        self.codigo_perfil2_cb.place(relx=0.22, rely=0.6, relwidth=0.72)

    def lista_componentes(self):
        """
        Método lista_componentes
        """
        self.listaMatrizes = ttk.Treeview(
            self.lista, height=3, columns=("col1", "col2", "col3"))
        self.listaMatrizes.heading("#0", text="")
        self.listaMatrizes.heading("#1", text="Código")
        self.listaMatrizes.heading("#2", text="Sistema - Perfil")
        self.listaMatrizes.heading("#3", text="Sistema - Perfil")
        self.listaMatrizes.column("#0", width=10)
        self.listaMatrizes.column("#1", width=40)
        self.listaMatrizes.column("#2", width=175)
        self.listaMatrizes.column("#3", width=175)
        self.listaMatrizes.place(relx=0.01, rely=0.02,
                                 relwidth=0.95, relheight=0.95)
        scrool_lista = tk.Scrollbar(self.lista, orient="vertical")
        self.listaMatrizes.configure(yscroll=scrool_lista.set)
        scrool_lista.place(relx=0.96, rely=0.02, relwidth=0.03, relheight=0.95)
        self.listaMatrizes.bind("<Double-1>", self.duplo_clique)
