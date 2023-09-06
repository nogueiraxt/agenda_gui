from tkinter import *
from tkinter import messagebox
import subprocess

usuarios = [
    {"email": "nogueira@gmail.com", "senha": "1234"},
    {"email": "nogueiraxt@gmail.com", "senha": "12345"},
]

def abrir_tela_agenda():
    subprocess.Popen(["python", "agenda.py"])
    subprocess.


def limparCampos() -> None:
    txt_email.delete(0, END)
    txt_senha.delete(0, END)


def login():
    email = txt_email.get()
    senha = txt_senha.get()

    for usuario in usuarios:
        if usuario["email"] == email and usuario["senha"] == senha:
            messagebox.showinfo("Login bem-sucedido", "Login realizado com sucesso!")
            limparCampos()
            abrir_tela_agenda()
            break
    else:
        messagebox.showerror("Erro de login", "Email ou senha incorretos.")


# INICIO --------TELA LOGIN--------
tela_login = Tk()

tela_login.title("Login")

label_email = Label(tela_login, text="Email: ", fg="navy", font="Tahoma 14 bold")
label_email.grid(row=0, column=0)
txt_email = Entry(tela_login, font="Tahoma 14", width=27)
txt_email.grid(row=0, column=1)

label_senha = Label(tela_login, text="Senha: ", fg="navy", font="Tahoma 14 bold")
label_senha.grid(row=1, column=0)
txt_senha = Entry(tela_login, font="Tahoma 14", width=27)
txt_senha.grid(row=1, column=1)

btn_login = Button(tela_login, text="Login", font="Tahoma 14 bold", command=login)
btn_login.grid(row=2, column=1)

tela_login.mainloop()
# FIM--------TELA LOGIN--------
