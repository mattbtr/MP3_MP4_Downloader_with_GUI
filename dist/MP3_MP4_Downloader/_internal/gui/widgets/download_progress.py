import customtkinter as ctk


class DownloadProgress(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.progressbar = ctk.CTkProgressBar(self)
        self.progressbar.pack(fill="x", padx=10, pady=(10, 2))

        self.label = ctk.CTkLabel(self, text="0 %")
        self.label.pack(pady=(0, 10))

        self.progressbar.set(0)

    def update_progress(self, percent, downloaded_mb, total_mb):
        self.progressbar.set(percent)

        percent_text = int(percent * 100)

        if total_mb > 0:
            text = f"{percent_text} % ({downloaded_mb:.1f} MB / {total_mb:.1f} MB)"
        else:
            text = f"{percent_text} %"

        self.label.configure(text=text)

    def reset(self):
        self.progressbar.set(0)
        self.label.configure(text="0 %")
