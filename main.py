import tkinter as tk
from tkinter import ttk

# Função para adicionar um objetivo
def adicionar_objetivo():
    objetivo = entrada_objetivo.get()
    tempo = entrada_tempo.get()
    if objetivo and tempo:
        lista_objetivos.insert(tk.END, f"{objetivo} - {tempo} minutos")
        entrada_objetivo.delete(0, tk.END)
        entrada_tempo.delete(0, tk.END)

# Configuração da janela principal
root = tk.Tk()
root.title("Gerenciador de Objetivos")

# Configuração do frame
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Configuração dos widgets
ttk.Label(frame, text="Objetivo:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
entrada_objetivo = ttk.Entry(frame, width=30)
entrada_objetivo.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(frame, text="Tempo (minutos):").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
entrada_tempo = ttk.Entry(frame, width=10)
entrada_tempo.grid(row=1, column=1, padx=5, pady=5)

botao_adicionar = ttk.Button(frame, text="Adicionar", command=adicionar_objetivo)
botao_adicionar.grid(row=2, column=0, columnspan=2, pady=10)

lista_objetivos = tk.Listbox(frame, width=50, height=10)
lista_objetivos.grid(row=3, column=0, columnspan=2, pady=10)

# Inicializar a interface
root.mainloop()
