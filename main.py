#import tkinter

#janela = tkinter.Tk()
#janela.geometry('500x300')

#def clique():
#   print('Fazer login')


#texto = tkinter.Label(janela, text='Fazer login')
#texto.pack(padx=10, pady=10)

#botao = tkinter.Button(janela, text='login', command=clique)
#botao.pack(padx=10, pady=10)

#janela.mainloop()
import customtkinter

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

janela = customtkinter.CTk()
janela.geometry('500x300')

def clique():
    print('fazer login')

texto = customtkinter.CTkLabel(janela, text='Fazer login')
texto.pack(padx=10, pady=10)

email = customtkinter.CTkEntry(janela, placeholder_text='Seu email...')
email.pack(padx=10, pady=10)

senha = customtkinter.CTkEntry(janela, placeholder_text='Sua senha...', show='*')
senha.pack(padx=10, pady=10)

checkbox = customtkinter.CTkCheckBox(janela, text='Lembrar senha')
checkbox.pack(padx=10, pady=10)


botao = customtkinter.CTkButton(janela, text='Login', command=clique)
botao.pack(padx=10, pady=10)

janela.mainloop()
