import tkinter as tk

window = tk.Tk()
# window.geometry("268x288")
window.title("Demo")
# window.resizable(width=False, height=False)

# border_effects = {
#     "flat": tk.FLAT,
#     "sunken": tk.SUNKEN,
#     "raised": tk.RAISED,
#     "groove": tk.GROOVE,
#     "ridge": tk.RIDGE,
# }

# for relief_name, relief in border_effects.items():
#     frame = tk.Frame(master=window, relief=relief, borderwidth=2)
#     frame.pack(side=tk.LEFT)
#     label = tk.Label(master=frame, text=relief_name)
#     label.pack()
frame1 = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
frame1.grid(row=0,column=0)
label = tk.Label(master=frame1, text=f"Row 1")
label.pack()
for i in range(1,4):
    for j in range(1,4):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j)
        label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
        label.pack()

window.mainloop()