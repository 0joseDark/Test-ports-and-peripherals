import tkinter as tk
import serial.tools.list_ports

# Função para detectar e listar as portas USB conectadas
def detectar_portas_usb():
    # Obtém a lista de todas as portas USB e dispositivos conectados
    portas = serial.tools.list_ports.comports()
    portas_usb = []  # Lista para armazenar as portas conectadas
    
    for porta in portas:
        # Verifica se a porta tem uma descrição e adiciona à lista
        descricao = porta.description if porta.description else "Dispositivo desconhecido"
        portas_usb.append(f"{porta.device} - {descricao}")
    
    return portas_usb

# Função para atualizar a lista de portas USB na interface gráfica
def atualizar_lista_portas():
    lista_portas.delete(0, tk.END)  # Limpa a lista atual no Listbox
    portas_usb = detectar_portas_usb()  # Obtém as portas USB conectadas
    
    if not portas_usb:  # Caso não haja portas USB conectadas
        lista_portas.insert(tk.END, "Nenhuma porta USB conectada.")
        print("Nenhuma porta USB conectada.")
    else:
        # Exibe as portas detectadas no terminal/console e na interface gráfica
        print("Portas USB conectadas:")
        for porta in portas_usb:
            print(porta)  # Mostra no terminal
            lista_portas.insert(tk.END, porta)  # Adiciona cada porta no Listbox da interface

# Função para fechar o programa
def sair_programa():
    janela.quit()

# Criando a janela principal
janela = tk.Tk()
janela.title("Lista de Portas USB e Periféricos")

# Criando o Listbox para exibir as portas USB conectadas
lista_portas = tk.Listbox(janela, width=60, height=10)
lista_portas.pack(pady=10)

# Botão para atualizar a lista de portas USB
botao_atualizar = tk.Button(janela, text="Atualizar Lista", command=atualizar_lista_portas)
botao_atualizar.pack(pady=5)

# Botão para sair do programa
botao_sair = tk.Button(janela, text="Sair", command=sair_programa)
botao_sair.pack(pady=5)

# Atualiza a lista de portas USB ao iniciar o programa
atualizar_lista_portas()

# Inicia o loop principal da aplicação Tkinter
janela.mainloop()
