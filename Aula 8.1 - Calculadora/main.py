import tkinter as tk

# Janela
window = tk.Tk()
window.title("Calculadora")
window.geometry("400x400") #tamanho no formato largura x altura

# Field
field = tk.Text(window, height=1, width=20, font=("Times New Roman", 20))
field.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=5, pady=5) # sticky para expandir e nsew para norte,sul,leste,oeste --> todos os lados
#row é a linha onde o campo vai ficar, column é a coluna, columnspan é para quantas colunas ele vai se estender
#começa na linha 0 e na coluna 0, e se estende por 4 colunas

# Declaração das variáveis
text_value = ""

# Função para atualizar o valor da textbox
def update_field(value):
    global text_value
    text_value = text_value + str(value)
    field.delete("1.0", "end")
    field.insert("1.0", text_value)

# Função para calcular
def calculate():
    global text_value
    try: #caso dê erro na conta
        result = str(eval(text_value)) #eval é usado por ser uma função que avalia uma string como uma expressão Python --> nativo
    except Exception:
        result = "Error"
    text_value = result
    field.delete("1.0", "end")
    field.insert("1.0", result)

# Função para limpar o campo inteiro
def clear_field():
    global text_value
    text_value = ""
    field.delete("1.0", "end")

# grid expande uniformemente
for c in range(4):
    window.grid_columnconfigure(c, weight=1, uniform="col") #weight define o peso de expansão e uniform define que todas as colunas terão o mesmo peso
for r in range(1, 6):
    window.grid_rowconfigure(r, weight=1, uniform="row") #weight define o peso de expansão e uniform define que todas as linhas terão o mesmo peso


# Números
btn_1 = tk.Button(window, text="1", command=lambda: update_field(1))
btn_1.grid(row=3, column=0, sticky="nsew", padx=2, pady=2)

btn_2 = tk.Button(window, text="2", command=lambda: update_field(2))
btn_2.grid(row=3, column=1, sticky="nsew", padx=2, pady=2)

btn_3 = tk.Button(window, text="3", command=lambda: update_field(3))
btn_3.grid(row=3, column=2, sticky="nsew", padx=2, pady=2)

btn_4 = tk.Button(window, text="4", command=lambda: update_field(4))
btn_4.grid(row=2, column=0, sticky="nsew", padx=2, pady=2)

btn_5 = tk.Button(window, text="5", command=lambda: update_field(5))
btn_5.grid(row=2, column=1, sticky="nsew", padx=2, pady=2)

btn_6 = tk.Button(window, text="6", command=lambda: update_field(6))
btn_6.grid(row=2, column=2, sticky="nsew", padx=2, pady=2)

btn_7 = tk.Button(window, text="7", command=lambda: update_field(7))
btn_7.grid(row=1, column=0, sticky="nsew", padx=2, pady=2)

btn_8 = tk.Button(window, text="8", command=lambda: update_field(8))
btn_8.grid(row=1, column=1, sticky="nsew", padx=2, pady=2)

btn_9 = tk.Button(window, text="9", command=lambda: update_field(9))
btn_9.grid(row=1, column=2, sticky="nsew", padx=2, pady=2)

btn_0 = tk.Button(window, text="0", command=lambda: update_field(0))
btn_0.grid(row=4, column=0, sticky="nsew", padx=2, pady=2)

# Operações
btn_add = tk.Button(window, text="+", command=lambda: update_field("+"))
btn_add.grid(row=4, column=3, sticky="nsew", padx=2, pady=2)

btn_minus = tk.Button(window, text="-", command=lambda: update_field("-"))
btn_minus.grid(row=3, column=3, sticky="nsew", padx=2, pady=2)

btn_times = tk.Button(window, text="*", command=lambda: update_field("*"))
btn_times.grid(row=2, column=3, sticky="nsew", padx=2, pady=2)

btn_divide = tk.Button(window, text="/", command=lambda: update_field("/"))
btn_divide.grid(row=1, column=3, sticky="nsew", padx=2, pady=2)

btn_clear = tk.Button(window, text="clear", command=clear_field, font=("Times New Roman", 16)) #a função não precisa de () ou lambda pq não tem parâmetro
btn_clear.grid(row=4, column=2, sticky="nsew", padx=2, pady=2)

btn_decimal = tk.Button(window, text=".", command=lambda: update_field("."))
btn_decimal.grid(row=4, column=1, sticky="nsew", padx=2, pady=2)

btn_equals = tk.Button(window, text="=", command=calculate, font=("Times New Roman", 18)) #calculate realiza o cálculo pela função eval
btn_equals.grid(row=5, column=2, columnspan=2, sticky="nsew", padx=2, pady=4) 

btn_parentheses_open = tk.Button(window, text="(", command=lambda: update_field("("))
btn_parentheses_open.grid(row=5, column=0, sticky="nsew", padx=2, pady=2)

btn_parentheses_close = tk.Button(window, text=")", command=lambda: update_field(")"))
btn_parentheses_close.grid(row=5, column=1, sticky="nsew", padx=2, pady=2)

# Main
window.mainloop()