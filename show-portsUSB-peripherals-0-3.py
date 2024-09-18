import tkinter as tk
import serial.tools.list_ports
from tkinter import messagebox

# Função para detectar e listar as portas USB conectadas
def detectar_portas_usb():
    # Lista todas as portas USB conectadas ao sistema
    portas = serial.tools.list_ports.comports()
    return portas

# Função para mostrar detalhes da porta USB selecionada
def mostrar_detalhes_porta():
    try:
        index = lista_portas.curselection()[0]  # Pega o índice da seleção no Listbox
        porta = portas_detectadas[index]  # Obtém a porta correspondente
        # Exibe uma mensagem com detalhes da porta USB
        messagebox.showinfo("Detalhes da Porta USB",
                            f"Porta: {porta.device}\n"
                            f"Descrição: {porta.description}\n"
                            f"Fabricante: {porta.manufacturer}")
    except IndexError:
        messagebox.showwarning("Aviso", "Selecione uma porta USB da lista.")

# Função para atualizar a lista de portas USB na interface gráfica e no terminal
def atualizar_lista_portas():
    global portas_detectadas
    lista_portas.delete(0, tk.END)  # Limpa o Listbox
    portas_detectadas = detectar_portas_usb()  # Detecta as portas USB
    
    # Exibe as portas no terminal/console
    print("Portas USB e periféricos detectados:")
    
    for porta in portas_detectadas:
        # Mostra cada porta e descrição no console
        print(f"{porta.device} - {porta.description}")
        
        # Adiciona a porta e a descrição ao Listbox na interface
        lista_portas.insert(tk.END, f"{porta.device} - {porta.description}")

# Função para fechar o programa
def sair_programa():
    janela.quit()

# Criando a janela principal
janela = tk.Tk()
janela.title("Detecção de Portas USB e Periféricos")

# Adicionando o Listbox para mostrar as portas USB detectadas
lista_portas = tk.Listbox(janela, width=60)
lista_portas.pack(pady=10)

# Botão para mostrar detalhes da porta USB selecionada
botao_mostrar_detalhes = tk.Button(janela, text="Mostrar Detalhes", command=mostrar_detalhes_porta)
botao_mostrar_detalhes.pack(pady=5)

# Botão para atualizar a lista de portas USB
botao_atualizar = tk.Button(janela, text="Atualizar Lista", command=atualizar_lista_portas)
botao_atualizar.pack(pady=5)

# Botão para sair do programa
botao_sair = tk.Button(janela, text="Sair", command=sair_programa)
botao_sair.pack(pady=5)

# Atualizar a lista de portas USB na inicialização
atualizar_lista_portas()

# Iniciar o loop principal da aplicação Tkinter
janela.mainloop()
