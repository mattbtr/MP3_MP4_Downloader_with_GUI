import customtkinter as ctk


class VersionLabel(ctk.CTkFrame):
    def __init__(self, master, versions: dict):
        super().__init__(master)

        text = (
            f"App-Version: {versions['app']}\n"
            f"yt-dlp: {versions['yt_dlp']}\n"
            f"ffmpeg: {versions['ffmpeg']}"
        )

        label = ctk.CTkLabel(
            self,
            text=text,
            justify="left",
            anchor="w",
            font=ctk.CTkFont(size=12)
        )
        label.pack(fill="x", padx=10, pady=10)
