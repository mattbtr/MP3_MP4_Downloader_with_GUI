# widget/url_input.py
import tkinter as tk
import customtkinter as ctk


class UrlInput(ctk.CTkFrame):
    """
    Widget für die Eingabe einer YouTube-URL.
    """

    def __init__(self, master):
        super().__init__(master)

        self.label = ctk.CTkLabel(
            self,
            text="YouTube-Link eingeben:"
        )
        self.label.pack(anchor="w", padx=10, pady=(10, 0))

        self.entry = ctk.CTkEntry(
            self,
            placeholder_text="https://www.youtube.com/..."
        )
        self.entry.pack(fill="x", padx=10, pady=10)

        self._add_context_menu()



    def _add_context_menu(self):
        menu = tk.Menu(self.entry, tearoff=0)

        def copy():
            try:
                selection = self.entry.selection_get()
                self.entry.clipboard_clear()
                self.entry.clipboard_append(selection)
            except Exception:
                pass

        def cut():
            try:
                selection = self.entry.selection_get()
                self.entry.clipboard_clear()
                self.entry.clipboard_append(selection)
                self.entry.delete("sel.first", "sel.last")
            except Exception:
                pass

        def paste():
            try:
                text = self.entry.clipboard_get()
                self.entry.insert(tk.INSERT, text)
            except Exception:
                pass

        def select_all():
            self.entry.select_range(0, tk.END)
            self.entry.icursor(tk.END)

        menu.add_command(label="Ausschneiden", command=cut)
        menu.add_command(label="Kopieren", command=copy)
        menu.add_command(label="Einfügen", command=paste)
        menu.add_separator()
        menu.add_command(label="Alles auswählen", command=select_all)

        def show_menu(event):
            self.entry.focus_set()
            menu.tk_popup(event.x_root, event.y_root)

        self.entry.bind("<Button-3>", show_menu)
        self.entry.bind("<Control-Button-1>", show_menu)



    def get_url(self) -> str:
        return self.entry.get()
