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

        nova_tarefa = f"{data} ({dia_semana_en}/{dia_semana_fr}): {tarefa} - {tempo} minutos"

        # Adicionar tarefa ao dicionário de tarefas
        if data not in tarefas:
            tarefas[data] = []
        tarefas[data].append(nova_tarefa)

        # Atualizar a lista de tarefas
        atualizar_tarefas(data)

        entrada_tarefa.delete(0, tk.END)
        entrada_tempo.delete(0, tk.END)

def converter_minutos():
    try:
        minutos = int(entrada_tempo.get())
        horas = minutos // 60
        minutos_restantes = minutos % 60
        return f"{horas} horas e {minutos_restantes} minutos"
    except ValueError:
        return "Entrada inválida"

def atualizar_tarefas(data):
    lista_tarefas.delete(0, tk.END)
    tarefas_do_dia = tarefas.get(data, [])
    if tarefas_do_dia:
        for tarefa in tarefas_do_dia:
            lista_tarefas.insert(tk.END, tarefa)
    else:
        lista_tarefas.insert(tk.END, "Nenhuma tarefa realizada nesse dia.")

def mostrar_tarefas_do_dia(event):
    data = calendario.get_date()
    atualizar_tarefas(data)

def trocar_fundo(cor):
    # Atualiza a cor de fundo de todos os widgets
    frame_principal.config(bg=cor)
    frame_entrada.config(bg=cor)
    frame_lista_calendario.config(bg=cor)
    calendario.config(background=cor)
    lista_tarefas.config(bg=cor, fg='black' if cor == 'white' else 'white')
    botao_adicionar.config(style='TButton')
    style.configure('TButton', background=cor, padding=[10, 5])

root = tk.Tk()
root.title("MetaDiaria - Denizard")
root.geometry("800x600")

# Configuração do estilo
style = ttk.Style()
style.configure('TButton', font=('JetBrains Mono', 10))
style.configure('TEntry', font=('JetBrains Mono', 12))
style.configure('TLabel', font=('JetBrains Mono', 12))
style.configure('TButton', padding=[10, 5], relief='flat', borderwidth=1)  # Ajuste no botão

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
entrada_tempo = ttk.Entry(frame_entrada, width=10, font=('JetBrains Mono', 12), validate='key')
entrada_tempo['validatecommand'] = (entrada_tempo.register(lambda P: P.isdigit() or P == ''), '%P')
entrada_tempo.grid(row=1, column=1, padx=5, pady=5)

botao_adicionar = ttk.Button(frame_entrada, text="Adicionar", command=adicionar_tarefa)
botao_adicionar.grid(row=2, column=0, columnspan=2, pady=10, ipadx=15, ipady=10)

# Sub-frame para a lista de tarefas e calendário
frame_lista_calendario = tk.Frame(frame_principal, bg='purple')
frame_lista_calendario.pack(pady=10, padx=10, fill='both', expand=True)

# Listbox para exibir as tarefas
lista_tarefas = tk.Listbox(frame_lista_calendario, width=40, height=15, font=('JetBrains Mono', 12), bg='white', fg='black')
lista_tarefas.pack(side=tk.LEFT, padx=10, pady=10, fill='both', expand=True)

# Adicionando o calendário
calendario = Calendar(frame_lista_calendario, selectmode='day', font=('JetBrains Mono', 12), background='white', foreground='black', bordercolor='black')
calendario.pack(side=tk.RIGHT, pady=10, padx=10, fill='both', expand=True)
calendario.bind("<<CalendarSelected>>", mostrar_tarefas_do_dia)

# Dados aleatórios para teste
tarefas = {
    '07/01/2024': [
        "01/07/2024 (Monday/Lundi): Estudar Python - 120 minutos",
        "01/07/2024 (Monday/Lundi): Ler livro - 60 minutos"
    ],
    '07/02/2024': [
        "02/07/2024 (Tuesday/Mardi): Exercício físico - 45 minutos",
        "02/07/2024 (Tuesday/Mardi): Meditar - 30 minutos"
    ],
    '07/03/2024': [
        "03/07/2024 (Wednesday/Mercredi): Trabalho - 90 minutos"
    ],
    '07/04/2024': []
}

# Adiciona as tarefas de teste à lista
atualizar_tarefas(calendario.get_date())

# Exibição da data atual em francês e inglês
locale.setlocale(locale.LC_TIME, 'en_US.UTF-8')
data_atual_en = datetime.now().strftime('%A, %d %B %Y')
locale.setlocale(locale.LC_TIME, 'fr_FR.UTF-8')
data_atual_fr = datetime.now().strftime('%A, %d %B %Y')
ttk.Label(frame_principal, text=f"Hoje é {data_atual_en} / {data_atual_fr}", background='purple').pack(pady=10)

# Botões para trocar o fundo
frame_opcoes = tk.Frame(frame_principal)
frame_opcoes.pack(pady=10, padx=10, fill='x')

cores = ['purple', 'blue', 'green', 'gray', 'red', 'orange', 'yellow', 'pink']
for cor in cores:
    botao = ttk.Button(frame_opcoes, text=cor.capitalize(), command=lambda cor=cor: trocar_fundo(cor))
    botao.pack(side=tk.LEFT, padx=5)

root.mainloop()
