from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import  messagebox

cor0 = "#444466"  # cor preta / black
cor1 = "#F0F2F5"  # cor cinza / grey
cor2 = "#FF5C72"  # cor vermelha / red

# importando strings

import string 
import random





# Configurando janela
janela = Tk()
janela.title('')
janela.geometry("288x364")
janela.configure(bg=cor1)

# estilo 

estilo = ttk.Style(janela)
estilo.theme_use("clam")

# Dividindo a tela em dois frames
Frame_cima = Frame(janela, width=295, height=50, bg=cor1, padx=0, pady=0, relief="flat")
Frame_cima.grid(row=0, column=0, sticky=NSEW)

Frame_baixo = Frame(janela, width=295, height=310, bg=cor1, padx=0, pady=0, relief="flat")
Frame_baixo.grid(row=1, column=0, sticky=NSEW)

# Trabalhando no frame cima
# Trabalhando no frame cima
img = Image.open('pyhton.jpg')  # Adiciona a imagem
img = img.resize((40, 40))  # Configura o tamanho da imagem
img = ImageTk.PhotoImage(img)  # Abre a imagem no tkinter


# Logo
app_logo = Label(Frame_cima, height=60, image=img, compound=LEFT, padx=10, relief="flat", anchor='nw', bg=cor1)
app_logo.place(x=2, y=0)

# Configurando label cima

app_nome = Label(Frame_cima,text='GERADOR DE SENHAS', height=2, width=28, padx=0, relief="flat", anchor='nw', bg=cor1, fg=cor0, font="Ivy 16 bold")
app_nome.place(x=50, y=8)
app_linha = Label(Frame_cima,text='', height=0, width=42, padx=0, relief="flat", anchor='nw', bg=cor2, fg=cor0, font="Ivy 10")
app_linha.place(x=0, y=40)

# Configurando label baixo

app_senha = Label(Frame_baixo, text='- - - - -', height=2, width=20 , anchor='center', padx=0, relief="solid",bg=cor1, fg=cor0, font="Ivy 13 bold")
app_senha.grid(row=0, column=0, columnspan=1, sticky=NSEW, padx=3, pady=10)


app_infor = Label(Frame_baixo,text='Numero total de caracteres na senha', height=1, width=30,anchor='nw' ,padx=0, relief="flat",bg=cor1, fg=cor0, font="Ivy 10 bold", )
app_infor.grid(row=1, column=0, columnspan=2, sticky=NSEW, padx=5, pady=1)

# Spin box

var = IntVar()
var.set(8)
spin = Spinbox(Frame_baixo, from_=0 , to=20, width=5, textvariable=var)
spin.grid(row=2, column=0, columnspan=2, sticky=NW, padx=5, pady=8)

alfa_maior = string.ascii_uppercase
alfa_menor = string.ascii_lowercase
numero = '123456789'
simbolos = '[]{}()*;/,_-'



Frame_carecteres = Frame(Frame_baixo, width=295, height=210, bg=cor1, padx=0, pady=0, relief="flat" )
Frame_carecteres.grid(row=3, column=0, sticky=NSEW, columnspan=3)

# chuckbutton




# ----------------------------------------- letras maiusculas ---------------------------------------------------------

estado_1= StringVar()
estado_1.set(False)

check_1 = Checkbutton(Frame_carecteres, width=1, var=estado_1, onvalue=alfa_maior,offvalue='off', relief='flat', bg=cor1)
check_1.grid(row=0, column=0, sticky=NSEW, padx=2, pady=5)

app_infor = Label(Frame_carecteres,text='ABC Letras maiusculas', height=1, width=30,anchor='nw' ,padx=0, relief="flat",bg=cor1, fg=cor0, font="Ivy 10 bold", )
app_infor.grid(row=0, column=1, sticky=NW, padx=2, pady=8)


# ----------------------------------------- letras minusculas ---------------------------------------------------------

estado_2= StringVar()
estado_2.set(False)

check_2 = Checkbutton(Frame_carecteres, width=1, var=estado_2, onvalue=alfa_menor,offvalue='off', relief='flat', bg=cor1)
check_2.grid(row=1, column=0, sticky=NSEW, padx=2, pady=5)



app_infor = Label(Frame_carecteres,text='ABC Letras minusculas', height=1, width=30,anchor='nw' ,padx=0, relief="flat",bg=cor1, fg=cor0, font="Ivy 10 bold", )
app_infor.grid(row=1, column=1, sticky=NW, padx=2, pady=8)


# ---------------------------------------------- Numeros --------------------------------------------------------------

estado_3= StringVar()
estado_3.set(False)

check_3 = Checkbutton(Frame_carecteres, width=1, var=estado_3, onvalue=numero,offvalue='off', relief='flat', bg=cor1)
check_3.grid(row=2, column=0, sticky=NSEW, padx=2, pady=5)



app_infor = Label(Frame_carecteres,text='123 Numeros', height=1, width=30,anchor='nw' ,padx=0, relief="flat",bg=cor1, fg=cor0, font="Ivy 10 bold", )
app_infor.grid(row=2, column=1, sticky=NW, padx=2, pady=8)

# ---------------------------------------------- Simbolos ------------------------------------------------------------

estado_4= StringVar()
estado_4.set(False)

check_4 = Checkbutton(Frame_carecteres, width=1, var=estado_4, onvalue=simbolos,offvalue='off', relief='flat', bg=cor1)
check_4.grid(row=3, column=0, sticky=NSEW, padx=2, pady=5)



app_infor = Label(Frame_carecteres,text='Simbolos', height=1, width=30,anchor='nw' ,padx=0, relief="flat",bg=cor1, fg=cor0, font="Ivy 10 bold", )
app_infor.grid(row=3, column=1, sticky=NW, padx=2, pady=8)


# botao 



# Função gerar senha


def gerar_senha():
    alfa_maior = string.ascii_uppercase
    alfa_menor = string.ascii_lowercase
    numero = '123456789'
    simbolos = '[]{}()*;/,_-'

    global combinar

    combinar = alfa_maior + alfa_menor + numero + simbolos

    # Condição para maiuscula
    if estado_1 == alfa_maior:  
        combinar = alfa_maior
    else:
        pass
  
    # Condição para mainuscula
    if estado_2 == alfa_menor:  
        combinar = combinar + alfa_menor
    else:
        pass
    
    # Condição para numeros
    if estado_3 == numero:  
        combinar = combinar + numero
    else:
        pass

    # Simbolos
    if estado_4 == simbolos:  
        combinar = combinar + simbolos
    else:
        pass

    cumprimento = int(spin.get())
    senha = "". join(random.sample(combinar, cumprimento))
    app_senha['text'] = senha
    
    
def copiar_senha():
    
    infor = app_senha['text']
    Frame_baixo.clipboard_clear()
    Frame_baixo.clipboard_append(infor)

    messagebox.showinfo("sucesso", "A Senha foi copiada com sucesso")

botaoa_final = Button(Frame_carecteres,text='GERAR SENHA', height=1, width=32,anchor='center' ,padx=0, relief="flat", overrelief='solid',bg=cor2, fg=cor1, font="Ivy 10 bold", command=gerar_senha)
botaoa_final.grid(row=4, column=0, sticky=NSEW, padx=2, pady=5, columnspan=5)    
botaoa_copiar = Button(Frame_baixo,text='Copiar', height=2, width=7,anchor='center' ,padx=0, relief="raised", overrelief='solid',bg=cor1, fg=cor0, font="Ivy 10 bold", command=copiar_senha)
botaoa_copiar.grid(row=0, column=1, sticky=NW, padx=5, pady=10, columnspan=5)



janela.mainloop()
