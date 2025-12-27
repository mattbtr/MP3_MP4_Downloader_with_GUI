import customtkinter as ctk

class StatusLabel(ctk.CTkFrame):
    """
    Widget zur Anzeige von Statusmeldungen.
    """

    def __init__(self, master):
        super().__init__(master)

        self.label = ctk.CTkLabel(
            self,
            text="Bereit.",
            wraplength=400
        )
        self.label.pack(padx=10, pady=10)

    def set_status(self, text: str):
        """
        Setzt den Status-Text.
        """
        self.label.configure(text=text)

