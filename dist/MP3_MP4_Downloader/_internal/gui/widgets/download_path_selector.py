import customtkinter as ctk
from tkinter import filedialog


class DownloadPathSelector(ctk.CTkFrame):
    def __init__(self, master, default_path):
        super().__init__(master)

        self.path = default_path

        self.label = ctk.CTkLabel(
            self,
            text=f"Download-Ordner:\n{self.path}",
            anchor="w",
            justify="left"
        )
        self.label.pack(fill="x", padx=10, pady=5)

        self.button = ctk.CTkButton(
            self,
            text="📁 Ordner wählen",
            command=self.choose_folder
        )
        self.button.pack(padx=10, pady=(0, 10))

    def choose_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.path = folder
            self.label.configure(text=f"Download-Ordner:\n{self.path}")
        if hasattr(self.master, "settings"):
            self.master.settings.set("download_path", self.path)
            self.master.settings.save()

    def get_path(self):
        return self.path
