import tkinter as tk
from tkinter import messagebox
import serial.tools.list_ports  # Biblioteca para detectar portas USB

# Função para detectar e listar as portas USB conectadas
def detectar_portas_usb():
    # Listar todas as portas USB disponíveis
    portas = serial.tools.list_ports.comports()
    return portas

# Função para salvar as informações das portas USB detectadas em um arquivo
def salvar_informacoes_em_arquivo(portas):
    with open("note.txt", "w") as arquivo:
        for porta in portas:
            # Escrever no arquivo informações da porta (nome da porta, descrição e fabricante)
            arquivo.write(f"Porta: {porta.device}, Descrição: {porta.description}, Fabricante: {porta.manufacturer}\n")

# Função para mostrar detalhes da porta USB selecionada pelo usuário
def mostrar_informacao_selecionada():
    try:
        # Obter o índice da seleção no Listbox
        index = lista_portas.curselection()[0]
        # Pegar a porta correspondente na lista de portas detectadas
        porta = portas_detectadas[index]
        # Exibir as informações detalhadas em uma mensagem
        messagebox.showinfo("Informação da Porta USB",
                            f"Porta: {porta.device}\n"
                            f"Descrição: {porta.description}\n"
                            f"Fabricante: {porta.manufacturer}")
    except IndexError:
        # Exibir um aviso caso nenhuma porta tenha sido selecionada
        messagebox.showwarning("Aviso", "Selecione uma porta USB da lista.")

# Função para atualizar a lista de portas USB detectadas na interface gráfica
def atualizar_lista_portas():
    global portas_detectadas
    lista_portas.delete(0, tk.END)  # Limpar o Listbox
    portas_detectadas = detectar_portas_usb()  # Detectar as portas USB
    salvar_informacoes_em_arquivo(portas_detectadas)  # Salvar informações em um arquivo
    for porta in portas_detectadas:
        # Adicionar a porta e a descrição ao Listbox
        lista_portas.insert(tk.END, f"{porta.device} - {porta.description}")

# Função para fechar o programa
def sair_programa():
    janela.quit()

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
lista_portas = tk.Listbox(janela, width=60)
lista_portas.pack(pady=10)

# Botão para mostrar detalhes da porta USB selecionada
botao_selecionar = tk.Button(janela, text="Mostrar Informações", command=mostrar_informacao_selecionada)
botao_selecionar.pack(pady=5)

# Botão para sair do programa
botao_sair = tk.Button(janela, text="Sair", command=sair_programa)
botao_sair.pack(pady=5)

# Atualizar a lista de portas USB na inicialização
atualizar_lista_portas()

# Iniciar o loop principal da aplicação Tkinter
janela.mainloop()
