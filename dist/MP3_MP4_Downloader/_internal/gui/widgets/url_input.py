import customtkinter as ctk


class UrlInput(ctk.CTkFrame):
    """
    Widget für die Eingabe einer YouTube-URL.
    """

    def __init__(self, master):
        super().__init__(master)

        # Label über dem Eingabefeld
        self.label = ctk.CTkLabel(
            self,
            text="YouTube-Link eingeben:"
        )
        self.label.pack(anchor="w", padx=10, pady=(10, 0))

        # Eingabefeld
        self.entry = ctk.CTkEntry(
            self,
            placeholder_text="https://www.youtube.com/..."
        )
        self.entry.pack(fill="x", padx=10, pady=10)

    def get_url(self) -> str:
        """
        Gibt die aktuell eingegebene URL zurück.
        """
        return self.entry.get()