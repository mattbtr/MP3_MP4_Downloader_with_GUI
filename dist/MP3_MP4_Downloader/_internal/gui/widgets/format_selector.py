import customtkinter as ctk

class FormatSelector(ctk.CTkFrame):
    """
    Widget zur Auswahl des Download-Formats (MP3 / MP4).
    """

    def __init__(self, master, default="mp3"):
        super().__init__(master)

        self.label = ctk.CTkLabel(
            self,
            text="Format auswählen:"
        )
        self.label.pack(anchor="w", padx=10, pady=(10, 0))

        # Variable speichert den aktuellen Wert
        self.format_var = ctk.StringVar(value=default)

        # Radiobuttons für MP3 / MP4
        self.mp3_radio = ctk.CTkRadioButton(
            self,
            text="MP3 (Audio)",
            variable=self.format_var,
            value="mp3"
        )
        self.mp3_radio.pack(anchor="w", padx=20, pady=5)

        self.mp4_radio = ctk.CTkRadioButton(
            self,
            text="MP4 (Video)",
            variable=self.format_var,
            value="mp4"
        )
        self.mp4_radio.pack(anchor="w", padx=20, pady=5)

    def get_format(self) -> str:
        """
        Gibt das ausgewählte Format zurück ("mp3" oder "mp4").
        """
        return self.format_var.get()