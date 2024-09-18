import tkinter as tk
import usb.core
import usb.util

# Função para detectar dispositivos USB conectados usando PyUSB
def detectar_dispositivos_usb():
    dispositivos = usb.core.find(find_all=True)  # Encontra todos os dispositivos USB conectados
    dispositivos_usb = []
    
    # Itera sobre cada dispositivo USB encontrado
    for dispositivo in dispositivos:
        # Obtém as informações do fabricante e produto, se disponível
        fabricante = usb.util.get_string(dispositivo, dispositivo.iManufacturer) if dispositivo.iManufacturer else "Fabricante desconhecido"
        produto = usb.util.get_string(dispositivo, dispositivo.iProduct) if dispositivo.iProduct else "Produto desconhecido"
        dispositivo_info = f"ID {dispositivo.idVendor}:{dispositivo.idProduct} - {fabricante} - {produto}"
        dispositivos_usb.append(dispositivo_info)
    
    return dispositivos_usb

# Função para atualizar a lista de dispositivos USB na interface gráfica
def atualizar_lista_dispositivos():
    lista_dispositivos.delete(0, tk.END)  # Limpa a lista atual no Listbox
    dispositivos_usb = detectar_dispositivos_usb()  # Obtém os dispositivos USB conectados
    
    if not dispositivos_usb:  # Caso não haja dispositivos USB conectados
        lista_dispositivos.insert(tk.END, "Nenhum dispositivo USB conectado.")
        print("Nenhum dispositivo USB conectado.")
    else:
        # Exibe os dispositivos detectados no terminal/console e na interface gráfica
        print("Dispositivos USB conectados:")
        for dispositivo in dispositivos_usb:
            print(dispositivo)  # Mostra no terminal
            lista_dispositivos.insert(tk.END, dispositivo)  # Adiciona cada dispositivo no Listbox da interface

# Função para fechar o programa
def sair_programa():
    janela.quit()

# Criando a janela principal
janela = tk.Tk()
janela.title("Lista de Dispositivos USB")

# Criando o Listbox para exibir os dispositivos USB conectados
lista_dispositivos = tk.Listbox(janela, width=80, height=10)
lista_dispositivos.pack(pady=10)

# Botão para atualizar a lista de dispositivos USB
botao_atualizar = tk.Button(janela, text="Atualizar Lista", command=atualizar_lista_dispositivos)
botao_atualizar.pack(pady=5)

# Botão para sair do programa
botao_sair = tk.Button(janela, text="Sair", command=sair_programa)
botao_sair.pack(pady=5)

# Atualiza a lista de dispositivos USB ao iniciar o programa
atualizar_lista_dispositivos()

# Inicia o loop principal da aplicação Tkinter
janela.mainloop()
