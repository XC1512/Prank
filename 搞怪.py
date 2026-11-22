import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.withdraw()
for i in range(100):
    messagebox.showinfo(title="提示：点击100次", message="受到！")
root.destroy()