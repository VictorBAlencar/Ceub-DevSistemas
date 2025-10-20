import tkinter

#Root é a janela principal
root = tkinter.Tk() #Tk é comando do tkinter para criar a janela principal

root.title("Main Window")
root.geometry("300x300")
root.configure(bg = "#ffffff") #cores em hexadecimal

#Definição da função do botão
def on_button_click():
    label.config(text = "Hello Tkinter!")

#Criação dos widgets
label = tkinter.Label(root, text = "And...", font = ("Comic Sans MS", 14, "bold", "italic", "underline"), bg = "#12AD12") #root é para dizer que o label pertence à janela principal
label.pack(pady = 10) #pack é um gerenciador de layout que organiza os widgets na janela, pady é o espaçamento vertical

#Criação do botão
button = tkinter.Button(root, text = "Click for a surprise!", command = on_button_click)
button.pack(pady = 5)

#Inicia o loop principal da interface gráfica
root.mainloop()