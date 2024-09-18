import tkinter as tk
from tkinter import messagebox
import serial.tools.list_ports  # Biblioteca para detectar portas USB
import os  # Para salvar a informação em um arquivo

# Função para detectar e listar as portas USB
def detectar_portas_usb():
    # Usamos 'serial.tools.list_ports.comports()' para listar todas as portas disponíveis
    portas = serial.tools.list_ports.comports()
    return portas

# Função para salvar as informações de dispositivos USB em um arquivo
def salvar_informacoes_em_arquivo(portas):
    with open("note.txt", "w") as arquivo:
        for porta in portas:
            # Escrevemos no arquivo o nome da porta, descrição e fabricante (se disponível)
            arquivo.write(f"Porta: {porta.device}, Descrição: {porta.description}, Fabricante: {porta.manufacturer}\n")

# Função chamada quando o botão de "Selecionar" é clicado
def mostrar_informacao_selecionada():
    try:
        # Pegamos o índice da seleção no Listbox
        index = lista_portas.curselection()[0]
        # Pegamos o objeto da porta correspondente
        porta = portas_detectadas[index]
        # Exibimos as informações da porta selecionada em uma mensagem
        messagebox.showinfo("Informação da Porta USB",
                            f"Porta: {porta.device}\n"
                            f"Descrição: {porta.description}\n"
                            f"Fabricante: {porta.manufacturer}")
    except IndexError:
        # Caso não haja seleção, mostramos um aviso
        messagebox.showwarning("Aviso", "Selecione uma porta USB da lista.")

# Função para atualizar a lista de portas USB na interface gráfica
def atualizar_lista_portas():
    global portas_detectadas
    lista_portas.delete(0, tk.END)  # Limpamos o Listbox
    portas_detectadas = detectar_portas_usb()  # Detectamos as portas USB
    salvar_informacoes_em_arquivo(portas_detectadas)  # Salvamos as informações em um arquivo
    for porta in portas_detectadas:
        # Adicionamos a porta e descrição ao Listbox
        lista_portas.insert(tk.END, f"{porta.device} - {porta.description}")

# Criando a janela principal
janela = tk.Tk()
janela.title("Detecção de Dispositivos USB")

# Criando a barra de menu
menu_barra = tk.Menu(janela)
janela.config(menu=menu_barra)

# Adicionando uma opção de "Atualizar" no menu
menu_arquivo = tk.Menu(menu_barra, tearoff=0)
menu_barra.add_cascade(label="Opções", menu=menu_arquivo)
menu_arquivo.add_command(label="Atualizar", command=atualizar_lista_portas)

# Adicionando a lista (Listbox) para mostrar as portas USB detectadas
lista_portas = tk.Listbox(janela, width=50)
lista_portas.pack(pady=10)

# Botão para mostrar detalhes da porta USB selecionada
botao_selecionar = tk.Button(janela, text="Mostrar Informações", command=mostrar_informacao_selecionada)
botao_selecionar.pack(pady=5)

# Atualizar a lista de portas USB na inicialização
atualizar_lista_portas()

# Iniciar o loop principal da aplicação Tkinter
janela.mainloop()