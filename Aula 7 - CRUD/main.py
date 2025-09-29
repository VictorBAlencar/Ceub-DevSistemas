import sys
import sqlite3
import banco as inventario #python é case sensitive

inventario.iniciar_banco()

#inventario.inserir_item("Espada Vorpal", "Arma", 1000)
#caso rode de novo, "Item já existente" -> try except

# inventario.inserir_item("Escudo de Rubi",
#                         "Escudo",
#                         750.00)

# inventario.inserir_item("Poção de Cura Menor",
#                         "Poção",
#                         "20.50") #erro de tipagem

#inventario.listar_itens()

# inventario.atualizar_item(1, "Espada Vorpal", "Arma", 1500.00)
# inventario.atualizar_item(2, "Escudo de Rubi", "Proteção", 750.00)
# inventario.atualizar_item(3, "Poção de Cura Menor", "Poção", 20.50)

inventario.listar_itens()

inventario.excluir_item(2)

inventario.listar_itens()