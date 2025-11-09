wimport tkinter as tk
from tkinter import ttk #para abas

###Funções
def change_slider(valor): #string
    #pass parar de dar erro --> como return
    valor_float = f"{float(valor):.0f}" #0f são 0 casas decimais / f é format
    label_valorSlider.config(text = f"Frequência Semanal: {valor_float}")

def select_combo(event):
    valor = combo_options.get()
    if valor != "---Selecione---":
        label_comboValue.config(text = f"Opção de Notificação: {valor}")



root = tk.Tk()
root.title("Window Test")
root.geometry("450x300")

#Criar notebook(container de abas)
notebook = ttk.Notebook(root) #na root

#Criar abas em instância
window1 = ttk.Frame(notebook) #no notebook
window2 = ttk.Frame(notebook)
window3 = ttk.Frame(notebook)

#Adicionar frames ao notebook
notebook.add(window1, text = "Cadastro")
notebook.add(window2, text = "Consulta")
notebook.add(window3, text = "Configurações")

#Empacotar o notebook
notebook.pack(expand = True, fill = "both") #expand e fill para ocupar toda a tela

##Wndow 1
label_window1 = ttk.Label(window1, text = "Formulário de Cadastro")
label_window1.pack(padx = 20, pady = 20) #pack é para organizar - como o grid

entry_nome = ttk.Entry(window1, width = 40)
entry_nome.pack(padx = 20, pady = 5)

btn_save = ttk.Button(window1, text = "Salvar")
btn_save.pack(pady = 10) 

##Window2
label_window2 = ttk.Label(window2, text = "Área de Consulta")
label_window2.pack(padx = 20, pady = 20)

entry_nome = ttk.Entry(window2, text = "Formulário de Busca")
entry_nome.pack(padx = 20, pady = 5)

btn_search = ttk.Button(window2, text = "Buscar")
btn_search.pack(pady = 10)

##Window3
#Default State
var_check = tk.BooleanVar()
var_check.set(False) #ou True

check_notification = ttk.Checkbutton(window3,
    text = "Receber Notificações", variable = var_check)
check_notification.pack(padx = 20, pady = 10)
#on_state = check_notification.getBoolean() --> para ver se está selecionado(1) ou não(0)

#Dropdown Combobox
frame = ttk.LabelFrame(window3, text = "Opções")
frame.pack(padx = 10, pady = 10)

list_notificationOption = [
    "---Selecione---",
    "Gmail",
    "Outlook",
    "Mensagens",
    "Whatsapp"
]

combo_options = ttk.Combobox(frame, values = list_notificationOption, state = "readonly")
combo_options.pack(padx = 5, pady = 10)
combo_options.current(0) #seleciona o 1* valor como default
#combo_options.get() -> pegar valor da string(a opção selecionada)

label_comboValue = ttk.Label(frame, text = "Opção de Notificação")
label_comboValue.pack(padx = 10, pady = 5)
combo_options.bind("<<ComboboxSelected>>", select_combo)

#Slider Scale
slider = ttk.Scale(
    frame,
    from_ = 0, 
    to = 7,
    orient = "horizontal",
    command = change_slider
)
slider.pack(padx = 5, pady = 10, fill = "x")

label_valorSlider = ttk.Label(frame, text = "Frequência Semanal : 0")
label_valorSlider.pack(padx = 10, pady = 5)

#Salvar
btn_save = ttk.Button(window3, text = "Salvar")
btn_save.pack(padx = 10, pady = 5, expand = "True")

#Rodar
root.mainloop()