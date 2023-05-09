import tkinter as tk
from tkinter import ttk

class CustomCombobox(ttk.Combobox):
    def __init__(self, master, values_id=None, **kw):
        self._values_id = values_id
        super().__init__(master, **kw)

    def set(self, value):
        if self._values_id:
            if value in self._values_id:
                super().set(self._values_id.index(value))
            else:
                super().set("")
        else:
            super().set(value)

    def get(self):
        if self._values_id:
            return self._values_id[self.current()]
        else:
            return super().get()

    def configure(self, cnf=None, **kw):
        if cnf and "values_id" in cnf:
            self._values_id = cnf.pop("values_id")
        super().configure(cnf=cnf, **kw)

    def __setitem__(self, key, value):
        if key == "values_id":
            self._values_id = value
        else:
            super().__setitem__(key, value)

    def __getitem__(self, key):
        if key == "values_id":
            return self._values_id
        else:
            return super().__getitem__(key)

