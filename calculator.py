import tkinter as tk
root= tk.Tk()
root.title("calculator")
 entry = tk.Entry(root, width=35, borderwidth=5)
 entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
root.mainloop()
