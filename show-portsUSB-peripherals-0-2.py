import tkinter as tk
import serial.tools.list_ports

# Função para detectar e listar as portas USB conectadas
def detectar_portas_usb():
    # Lista todas as portas USB conectadas ao sistema
    portas = serial.tools.list_ports.comports()
    return portas

# Função para atualizar a lista de portas USB na interface gráfica
def atualizar_lista_portas():
    lista_portas.delete(0, tk.END)  # Limpa o Listbox
    portas_detectadas = detectar_portas_usb()  # Detecta as portas USB
    
    # Exibe as portas no terminal/console
    print("Portas USB detectadas:")
    
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
janela.title("Detecção de Portas USB")

# Adicionando o Listbox para mostrar as portas USB detectadas
lista_portas = tk.Listbox(janela, width=60)
lista_portas.pack(pady=10)

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
