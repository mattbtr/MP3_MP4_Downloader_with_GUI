import customtkinter as ctk

class ActionButtons(ctk.CTkFrame):
    """
    Widget für die Aktions-Buttons (Download & Update).
    """

    def __init__(self, master, on_download, on_update):
        """
        :param on_download: Funktion, die beim Klick auf 'Download' aufgerufen wird
        :param on_update: Funktion, die beim Klick auf 'Update' aufgerufen wird
        """
        super().__init__(master)

        self.download_button = ctk.CTkButton(
            self,
            text="⬇ Download starten",
            command=on_download
        )
        self.download_button.pack(fill="x", padx=10, pady=(10, 5))

        self.update_button = ctk.CTkButton(
            self,
            text="🔄 Programm aktualisieren",
            command=on_update
        )
        self.update_button.pack(fill="x", padx=10, pady=(5, 10))

    def disable(self):
        """
        Deaktiviert alle Aktions-Buttons.
        """
        self.download_button.configure(state="disabled")
        self.update_button.configure(state="disabled")

    def enable(self):
        """
        Aktiviert alle Aktions-Buttons.
        """
        self.download_button.configure(state="normal")
        self.update_button.configure(state="normal")
