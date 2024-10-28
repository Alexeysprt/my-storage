import tkinter as tk

root = tk.Tk()

root.title("Hello app")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 900
window_height = 550
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

root.geometry(f"{window_width}x{window_height}+{x}+{y}")

def get_cat():
    label2.config(text="я не кот")

def get_med():
    print('Медоед')
    label1.config(text="змеи с мёдом")

def button_click_input():
    input_text = entry.get()
    label1.config(text=input_text)

label1 = tk.Label(root, text="пример пакета - pack()")
label1.pack()

button1 = tk.Button(root, text="Кот", command=get_cat)
button1.pack()

label2 = tk.Label(root, text="пример пласе - place()")
label2.place(x=500, y=400)

button2 = tk.Button(root, text="МЕДОЕД", command=get_med)
button2.place(x=510, y=420)

entry = tk.Entry(root)
entry.place(x=30, y=200)

button3 = tk.Button(root, text="Отправить", command=button_click_input)
button3.place(x=50, y=220)

def get_pow():
    res = pow(int(entry1.get()), int(entry2.get()))
    label3 = tk.Label(text = res)
    label3.pack()

entry1 = tk.Entry(root)
entry2 = tk.Entry(root)
button4 = tk.Button(root, text = 'считай', command=get_pow)
entry1.pack()
entry2.pack()
button4.pack()
root.mainloop()