import customtkinter as ctk

class ProcessResultPopup(ctk.CTkToplevel):
    def __init__(self, parent, title, success, summary, details):
        super().__init__(parent)

        self.title(title)
        self.geometry("500x400")
        self.resizable(False, False)

        self.grab_set()   # Modal
        self.focus()

        # Titel
        title_label = ctk.CTkLabel(
            self,
            text=title,
            font=ctk.CTkFont(size=18, weight="bold")
        )
        title_label.pack(pady=(20, 10))

        # Status
        status_color = "green" if success else "red"
        status_text = "✔ Erfolgreich" if success else "✖ Fehlgeschlagen"

        status_label = ctk.CTkLabel(
            self,
            text=status_text,
            text_color=status_color,
            font=ctk.CTkFont(size=14, weight="bold")
        )
        status_label.pack(pady=5)

        # Summary
        summary_label = ctk.CTkLabel(
            self,
            text=summary,
            wraplength=460,
            justify="left"
        )
        summary_label.pack(pady=(10, 10))

        # Details Box
        textbox = ctk.CTkTextbox(self, width=460, height=180)
        textbox.pack(padx=20, pady=10)

        for line in details:
            textbox.insert("end", f"• {line}\n")

        textbox.configure(state="disabled")

        # Close Button
        close_btn = ctk.CTkButton(self, text="Schließen", command=self.destroy)
        close_btn.pack(pady=(5, 15))
