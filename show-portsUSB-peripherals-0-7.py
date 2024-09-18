import tkinter as tk
import usbinfo

# Função para detectar e listar os dispositivos USB usando usbinfo
def detectar_dispositivos_usb():
    dispositivos_usb = usbinfo.usbinfo()  # Obtém as informações dos dispositivos USB conectados
    dispositivos_lista = []  # Lista para armazenar as informações formatadas

    # Itera sobre cada dispositivo USB encontrado
    for dispositivo in dispositivos_usb['devices']:
        fabricante = dispositivo.get('manufacturer', 'Fabricante desconhecido')
        produto = dispositivo.get('product', 'Produto desconhecido')
        vid = dispositivo.get('vendorid', 'ID do Fabricante desconhecido')
        pid = dispositivo.get('productid', 'ID do Produto desconhecido')

        dispositivo_info = f"ID {vid}:{pid} - {fabricante} - {produto}"
        dispositivos_lista.append(dispositivo_info)
    
    return dispositivos_lista

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
