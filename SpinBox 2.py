from tkinter import *
from tkinter import ttk

# Configuração da janela principal
root = Tk()
root.title("Seleção de Itens")
root.geometry("400x500")
root.configure(bg="#f0f8ff")

# Função para atualizar a mensagem exibida
def atualizar_mensagem(spinbox, label):
    label.config(text=f"Selecionado: {spinbox.get()}")

# Criação dos Spinboxes com rótulos e mensagens exibidas abaixo
frame1 = Frame(root, bg="#f0f8ff")
frame1.pack(pady=10)

Label(frame1, text="Selecione um número de 0 a 25:", bg="#f0f8ff", font=("Arial", 14, "bold")).pack()
s1 = Spinbox(frame1, from_=0, to=25, font=("Arial", 12))
s1.pack()
label1 = Label(frame1, text="", bg="#f0f8ff", font=("Arial", 12))
label1.pack()
Button(frame1, text="Mostrar Seleção", command=lambda: atualizar_mensagem(s1, label1), bg="#4682b4", fg="white", font=("Arial", 10, "bold")).pack(pady=5)

frame2 = Frame(root, bg="#f0f8ff")
frame2.pack(pady=10)

Label(frame2, text="Selecione um valor:", bg="#f0f8ff", font=("Arial", 14, "bold")).pack()
s2 = Spinbox(frame2, values=(10, 20, 30, 40, 50), wrap=True, font=("Arial", 12))
s2.pack()
label2 = Label(frame2, text="", bg="#f0f8ff", font=("Arial", 12))
label2.pack()
Button(frame2, text="Mostrar Seleção", command=lambda: atualizar_mensagem(s2, label2), bg="#4682b4", fg="white", font=("Arial", 10, "bold")).pack(pady=5)

frame3 = Frame(root, bg="#f0f8ff")
frame3.pack(pady=10)

Label(frame3, text="Selecione uma fruta:", bg="#f0f8ff", font=("Arial", 14, "bold")).pack()
s3 = Spinbox(frame3, values=("Abacate", "Morango", "Melancia", "Abacaxi"), wrap=True, font=("Arial", 12))
s3.pack()
label3 = Label(frame3, text="", bg="#f0f8ff", font=("Arial", 12))
label3.pack()
Button(frame3, text="Mostrar Seleção", command=lambda: atualizar_mensagem(s3, label3), bg="#4682b4", fg="white", font=("Arial", 10, "bold")).pack(pady=5)

root.mainloop()
