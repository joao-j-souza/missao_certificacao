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
from controller.sistema_controller import SistemaController
from controller.perfil_controller import PerfilController

file = Path(__file__).resolve()
parent, master = file.parent, file.parents[1]
sys.path.append(str(master))


class Funcs():
    """
    Classe com as fuções relativas a view da perfil.
    """

    def __init__(self):
        self.codigo_entry = None
        self.codigo_sistema_cb = None
        self.nome_entry = None
        self.descricao_text = None

    def limpa_tela(self):
        """
        Limpa o conteúdo das entrys do formulário.
        """
        self.codigo_entry.delete(0, tk.END)
        self.codigo_sistema_cb.delete(0, tk.END)
        self.nome_entry.delete(0, tk.END)
        self.descricao_text.delete("1.0", "end")
        self.lista_perfis()

    def duplo_clique(self, event):
        """
        Preenche o formulário ao dar um duplo clique no registro da lista.
        :param event: Evento que captura o duplo clique. 
        """
        self.codigo_entry.delete(0, tk.END)
        self.codigo_sistema_cb.delete(0, tk.END)
        self.nome_entry.delete(0, tk.END)
        self.descricao_text.delete("1.0", "end")

        self.listaPerfis.selection()
        for n in self.listaPerfis.selection():
            col1, col2, col3, col4 = self.listaPerfis.item(n, 'values')
        self.codigo_entry.insert(tk.END, col1)
        self.codigo_sistema_cb.insert(tk.END, col2)
        self.nome_entry.insert(tk.END, col3)
        self.descricao_text.insert(tk.END, col4)

    def exibir_mensagem(self, perfil):
        if perfil['success']:
            if "mensagem" in perfil:
                messagebox.showinfo("Informação", perfil['mensagem'])
        else:
            messagebox.showerror("Erro", perfil['mensagem'])

    def cria_perfil(self):
        """
        Função para cadastrar um perfil.
        """
        # Obtendo o código correspondente aos valores selecionados
        cod_sistema = self.codigo_sistema_cb["values_id"][self.codigo_sistema_cb.current(
        )]
        nome = self.nome_entry.get()
        descricao = self.descricao_text.get("1.0", "end-1c")

        if not cod_sistema:
            messagebox.showerror(
                "Alerta!", "O Campo Sistema é obrigatório!")
        else:
            controller = PerfilController()
            perfil = controller.adiciona_perfil(cod_sistema, nome, descricao)
            self.exibir_mensagem(perfil)
            self.limpa_tela()
            self.lista_perfis()

    def altera_perfil(self):
        """
        Função para alterar um perfil.
        """
        codigo = self.codigo_entry.get()
        cod_sistema = self.codigo_sistema_cb.get()
        nome = self.nome_entry.get()
        descricao = self.descricao_text.get("1.0", "end-1c")

        if ((not codigo) or (not cod_sistema) or (not nome)):
            if not codigo:
                messagebox.showerror(
                    "Alerta", "O Campo Código é obrigatório!")
            elif not cod_sistema:
                messagebox.showerror(
                    "Alerta", "O Campo Sistema é obrigatório!")
            elif not nome:
                messagebox.showerror(
                    "Alerta", "O Campo Nome é obrigatório!")           
        else:
            controller = PerfilController()            
            perfil = controller.altera_perfil(codigo, cod_sistema, nome, descricao)
            self.exibir_mensagem(perfil)
            self.limpa_tela()
            self.lista_perfis()

    def apaga_perfil(self):
        """
        Função para apagar um perfil.
        """
        codigo = self.codigo_entry.get()
        if not codigo:
            messagebox.showerror("Alerta!", "O Campo Código é obrigatório!")
        else:
            controller = PerfilController()
            perfil = controller.apaga_perfil(codigo)
            self.exibir_mensagem(perfil)
            self.limpa_tela()
            self.lista_perfis()

    def busca_perfil(self):
        """
        Método busca_perifl
        """
        codigo = self.codigo_entry.get()
        controller = PerfilController()
        if codigo:
            perfil = controller.busca_perfil(codigo)
            if 'resultado' in perfil:
                self.listaPerfis.delete(*self.listaPerfis.get_children())
                for s in perfil['resultado']:
                    self.listaPerfis.insert("", tk.END, values=s)
            self.exibir_mensagem(perfil)
        else:
            messagebox.showinfo("Informação", "Digite o código.")

    def lista_perfis(self):
        """
        Método lista_perfis
        """
        self.listaPerfis.delete(*self.listaPerfis.get_children())
        controller = PerfilController()
        perfis = controller.lista_perfis()
        if perfis['success']:
            for perfil in perfis['resultado']:
                self.listaPerfis.insert("", tk.END, values=perfil)
        self.exibir_mensagem(perfis)

    def popula_combos(self):
        controller = SistemaController()
        # Buscando os sistemas no banco de dados
        sistemas = controller.lista_sistemas()

        # Criando uma lista de valores para o combobox, contendo o código do sistema
        codigos = [c_sistemas[0] for c_sistemas in sistemas["resultado"]]

        # Criando uma lista de valores para o combobox, contendo o nome do sistema
        nomes = [p_nomes[1] for p_nomes in sistemas["resultado"]]

        # Configurando as opções do combobox para exibir o nome do sistema e retornar o código correspondente
        self.codigo_sistema_cb["values_id"] = codigos
        self.codigo_sistema_cb["values"] = nomes


class PerfilView(Funcs):
    """
    Classe PerfilView
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
        self.lista_perfis()
        self.popula_combos()

    def frame(self):
        """
        Método perfis_frame
        """
        # Cria o Frame para o Form de Cadastro
        self.form = tk.Frame(self.root, bg='#dfe3ee', bd=4,
                             highlightbackground='#759fe6', highlightthickness=3)
        self.form.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.66)

    def lista_frame(self):
        """
        Método lista_frame
        """
        # Cria o Frame para a Listagem de Perfis
        self.lista = tk.Frame(self.root, bg='#dfe3ee', bd=4,
                              highlightbackground='#759fe6', highlightthickness=3)
        self.lista.place(relx=0.02, rely=0.69, relwidth=0.96, relheight=0.29)

    def componentes(self):
        """
        Método perfis_componentes
        """
        bt_font = Font(family="verdana", size=8, weight="bold")
        # Criação do Botão Limpar
        bt_limpar = tk.Button(self.form, text="Limpar", bd=2, bg="#107db2",
                              fg="white", font=bt_font, command=self.limpa_tela)
        bt_limpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.1)
        # Criação do Botão Buscar
        bt_buscar = tk.Button(self.form, text="Buscar", bd=2, bg="#107db2",
                              fg="white", font=bt_font, command=self.busca_perfil)
        bt_buscar.place(relx=0.305, rely=0.1, relwidth=0.1, relheight=0.1)
        # Criação do Botão Novo
        bt_novo = tk.Button(self.form, text="Novo", bd=2, bg="#107db2",
                            fg="white", font=bt_font, command=self.cria_perfil)
        bt_novo.place(relx=0.55, rely=0.1, relwidth=0.1, relheight=0.1)
        # Criação do Botão Alterar
        bt_alterar = tk.Button(self.form, text="Alterar", bd=2, bg="#107db2",
                               fg="white", font=bt_font, command=self.altera_perfil)
        bt_alterar.place(relx=0.655, rely=0.1, relwidth=0.1, relheight=0.1)
        # Criação do Botão Apagar
        bt_apagar = tk.Button(self.form, text="Apagar",
                              bd=2, bg="#107db2", fg="white", font=bt_font, command=self.apaga_perfil)
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
        lb_nome.place(relx=0.05, rely=0.4)
        self.nome_entry = tk.Entry(self.form)
        self.nome_entry.place(relx=0.14, rely=0.4, relwidth=0.72)

        # Criação da Label e Entrada do sistema
        lb_sistema = tk.Label(self.form, text="Sistema*:",
                              bg="#dfe3ee", fg="#107db2")
        lb_sistema.place(relx=0.05, rely=0.3)

        cod_sistema = StringVar()

        self.codigo_sistema_cb = CustomCombobox(
            self.form, textvariable=cod_sistema)
        self.codigo_sistema_cb.place(relx=0.14, rely=0.3, relwidth=0.36)

        # Criação da Label e Entrada da descrição
        lb_descricao = tk.Label(self.form, text="Descrição*:",
                           bg="#dfe3ee", fg="#107db2")
        lb_descricao.place(relx=0.05, rely=0.5)
        self.descricao_text = tk.Text(self.form, height=5, width=30)
        self.descricao_text.place(relx=0.14, rely=0.5, relwidth=0.72)
        
    def lista_componentes(self):
        """
        Método lista_componentes
        """
        self.listaPerfis = ttk.Treeview(
        self.lista, height=3, columns=("col1", "col2", "col3", "col4"))
        self.listaPerfis.heading("#0", text="")
        self.listaPerfis.heading("#1", text="Código")
        self.listaPerfis.heading("#2", text="Sistema")
        self.listaPerfis.heading("#3", text="Nome")
        self.listaPerfis.heading("#4", text="Descrição")
        self.listaPerfis.column("#0", width=10)
        self.listaPerfis.column("#1", width=40)
        self.listaPerfis.column("#2", width=175)
        self.listaPerfis.column("#3", width=175)
        self.listaPerfis.column("#4", width=175)
        self.listaPerfis.place(relx=0.01, rely=0.02,
                                 relwidth=0.95, relheight=0.95)
        scrool_lista = tk.Scrollbar(self.lista, orient="vertical")
        self.listaPerfis.configure(yscroll=scrool_lista.set)
        scrool_lista.place(relx=0.96, rely=0.02, relwidth=0.03, relheight=0.95)
        self.listaPerfis.bind("<Double-1>", self.duplo_clique)
