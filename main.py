"""
Permite adicionar o diretório pai do arquivo atual ao caminho de busca de módulos (sys.path).
"""
import sys
from pathlib import Path
import tkinter as tk
from tkinter.font import Font
from controller.main_controller import MainController

file = Path(__file__).resolve()
parent, master = file.parent, file.parents[1]
sys.path.append(str(master))

class Main(tk.Frame):
    """
    Classe Main
    """
    def __init__(self, root=None):
        """
        Método init
        """
        super().__init__(root)
        self.root = root
        self.controller = MainController(self.root)
        self.tela()  # Chama o método que configura a tela.
        self.menu()  # Chama o método que constroi o menu.
        self.frame()  # Chama o método que define o frame.

    def tela(self):
        """
        Método tela
        """
        self.root.title("Missão Certificação")
        self.root.configure(background='#1e3743')
        self.root.geometry("700x500")
        self.root.resizable(True, True)
        self.root.maxsize(width=1200, height=800)
        self.root.minsize(width=700, height=400)

    def menu(self):
        """
        Método menu
        """
        menu = tk.Menu(self.root)
        filemenu = tk.Menu(menu, tearoff=0)
        filemenu2 = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Opções", menu=filemenu)
        menu.add_cascade(label="Sobre", menu=filemenu2)

        filemenu.add_command(label="Home", command=self.frame)
        filemenu.add_separator()
        filemenu.add_command(label="Sistemas", command=self.sistema_frame)
        filemenu.add_command(label="Perfis")
        filemenu.add_command(label="MatrizSoD")
        filemenu.add_command(label="Usuários")
        filemenu.add_separator()
        def sair():
            self.root.destroy()
        filemenu.add_command(label="Sair", command=sair)
        self.root.config(menu=menu)

    def frame(self):
        """
        Método home_frame
        """
        self.fecha_componentes()
        self.home_frame = tk.Frame(self.root, bg='#1e3743', bd=4)
        self.home_frame.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.componentes()

    def componentes(self):
        """
        Método home_componentes
        """
        home_label_font = Font(family="verdana", size=22)
        home_label = tk.Label(self.home_frame, text="Bem-vindo à tela inicial",
                                bg='#1e3743', fg='white', font=home_label_font)
        home_label.place(relx=0.25, rely=0.25)

    def sistema_frame(self):
        """
        Método sistema_frame
        """
        self.fecha_componentes()
        self.controller.lista_sistemas()

    def fecha_componentes(self):
        """
        Destroi todos os widgets exceto o menu
        """
        for widget in self.root.winfo_children():
            if widget.winfo_class() != 'Menu':
                widget.destroy()        

if __name__ == "__main__":
    root = tk.Tk()
    Main(root)
    root.mainloop()
