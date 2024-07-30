import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
from datetime import datetime
import locale

def adicionar_tarefa():
    tarefa = entrada_tarefa.get()
    tempo = entrada_tempo.get()
    data = calendario.get_date()

    if tarefa and tempo:
        # Definir o locale para inglês e francês
        locale.setlocale(locale.LC_TIME, 'en_US.UTF-8')
        dia_semana_en = datetime.strptime(data, '%m/%d/%y').strftime('%A')

        locale.setlocale(locale.LC_TIME, 'fr_FR.UTF-8')
        dia_semana_fr = datetime.strptime(data, '%m/%d/%y').strftime('%A')

        # Adicionar tarefa na lista com os dias da semana em inglês e francês
        lista_tarefas.insert(tk.END, f"{data} ({dia_semana_en}/{dia_semana_fr}): {tarefa} - {tempo} minutos")
        entrada_tarefa.delete(0, tk.END)
        entrada_tempo.delete(0, tk.END)

def trocar_fundo(cor):
    # Atualiza a cor de fundo de todos os widgets
    frame_principal.config(bg=cor)
    frame_entrada.config(bg=cor)
    frame_lista_calendario.config(bg=cor)
    calendario.config(background=cor)
    lista_tarefas.config(bg=cor, fg='black' if cor == 'white' else 'white')

root = tk.Tk()
root.title("Gerenciador de Tarefas")
root.geometry("800x600")

# Configuração do estilo
style = ttk.Style()
style.configure('TButton', font=('JetBrains Mono', 10))
style.configure('TEntry', font=('JetBrains Mono', 12))
style.configure('TLabel', font=('JetBrains Mono', 12))

# Frame principal
frame_principal = tk.Frame(root, bg='purple')
frame_principal.pack(expand=True, fill='both')

# Sub-frame para as entradas de tarefa e tempo
frame_entrada = tk.Frame(frame_principal, bg='purple')
frame_entrada.pack(pady=10, padx=10, fill='x')

ttk.Label(frame_entrada, text="Tarefa:", background='purple').grid(row=0, column=0, sticky=tk.E, padx=5, pady=5)
entrada_tarefa = ttk.Entry(frame_entrada, width=30, font=('JetBrains Mono', 12))
entrada_tarefa.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(frame_entrada, text="Tempo (minutos):", background='purple').grid(row=1, column=0, sticky=tk.E, padx=5, pady=5)
entrada_tempo = ttk.Entry(frame_entrada, width=10, font=('JetBrains Mono', 12))
entrada_tempo.grid(row=1, column=1, padx=5, pady=5)

botao_adicionar = ttk.Button(frame_entrada, text="Adicionar", command=adicionar_tarefa)
botao_adicionar.grid(row=2, column=0, columnspan=2, pady=10)

# Sub-frame para a lista de tarefas e calendário
frame_lista_calendario = tk.Frame(frame_principal, bg='purple')
frame_lista_calendario.pack(pady=10, padx=10, fill='both', expand=True)

# Listbox para exibir as tarefas
lista_tarefas = tk.Listbox(frame_lista_calendario, width=40, height=15, font=('JetBrains Mono', 12), bg='white', fg='black')
lista_tarefas.pack(side=tk.LEFT, padx=10, pady=10, fill='both', expand=True)

# Adicionando o calendário
calendario = Calendar(frame_lista_calendario, selectmode='day', font=('JetBrains Mono', 12), background='white', foreground='black', bordercolor='black')
calendario.pack(side=tk.RIGHT, pady=10, padx=10, fill='both', expand=True)

# Exibição da data atual em francês e inglês
locale.setlocale(locale.LC_TIME, 'en_US.UTF-8')
data_atual_en = datetime.now().strftime('%A, %d %B %Y')
locale.setlocale(locale.LC_TIME, 'fr_FR.UTF-8')
data_atual_fr = datetime.now().strftime('%A, %d %B %Y')
ttk.Label(frame_principal, text=f"Hoje é {data_atual_en} / {data_atual_fr}", background='purple').pack(pady=10)

# Botões para trocar o fundo
frame_opcoes = tk.Frame(frame_principal)
frame_opcoes.pack(pady=10, padx=10, fill='x')

botao_roxo = ttk.Button(frame_opcoes, text="Roxo", command=lambda: trocar_fundo('purple'))
botao_roxo.pack(side=tk.LEFT, padx=5)

botao_azul = ttk.Button(frame_opcoes, text="Azul", command=lambda: trocar_fundo('blue'))
botao_azul.pack(side=tk.LEFT, padx=5)

botao_verde = ttk.Button(frame_opcoes, text="Verde", command=lambda: trocar_fundo('green'))
botao_verde.pack(side=tk.LEFT, padx=5)

botao_cinza = ttk.Button(frame_opcoes, text="Cinza", command=lambda: trocar_fundo('gray'))
botao_cinza.pack(side=tk.LEFT, padx=5)

root.mainloop()
