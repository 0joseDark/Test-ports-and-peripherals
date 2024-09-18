import tkinter as tk
import subprocess

# Mapeamento de periféricos comuns em inglês para português
PERIFERICOS_USB = {
    "Keyboard": "Teclado",
    "Mouse": "Rato",
    "Printer": "Impressora",
    "Scanner": "Scanner",
    "Webcam": "Câmera",
    "Audio": "Dispositivo de Áudio",
    "Mass Storage": "Dispositivo de Armazenamento",
    "HID-compliant": "Dispositivo HID (Ex: Controle ou Teclado)",
    "Hub": "Hub USB"
}

# Função para capturar informações gerais sobre dispositivos USB
def obter_informacoes_usb():
    try:
        # Executa o comando `wmic` para listar os dispositivos USB conectados
        resultado_dispositivos = subprocess.run(['wmic', 'path', 'Win32_PnPEntity', 'where', "PNPClass='USB'", 'get', 'Name,DeviceID'], capture_output=True, text=True)

        # Divide o resultado em linhas
        dispositivos = resultado_dispositivos.stdout.splitlines()

        dispositivos_traduzidos = []
        
        # Para cada dispositivo identificado, traduzimos o nome se possível
        for dispositivo in dispositivos:
            dispositivo = dispositivo.strip()  # Remove espaços em branco

            if dispositivo:  # Ignora linhas vazias
                dispositivo_traduzido = dispositivo

                # Tentamos traduzir com base no mapeamento PERIFERICOS_USB
                for termo_ingles, termo_portugues in PERIFERICOS_USB.items():
                    if termo_ingles in dispositivo:
                        dispositivo_traduzido = dispositivo.replace(termo_ingles, termo_portugues)
                        break

                # Adicionamos o dispositivo à lista traduzida
                dispositivos_traduzidos.append(dispositivo_traduzido)

        return dispositivos_traduzidos

    except FileNotFoundError:
        return ["Erro: 'wmic' não encontrado no sistema."]
    except Exception as e:
        return [f"Erro ao executar o comando: {str(e)}"]

# Função para atualizar a lista de dispositivos USB na interface gráfica
def atualizar_lista_dispositivos():
    lista_dispositivos.delete(0, tk.END)  # Limpa a lista atual no Listbox
    informacoes_usb = obter_informacoes_usb()  # Obtém as informações dos dispositivos USB

    if not informacoes_usb or "No Instance(s) Available" in informacoes_usb:  # Caso não haja dispositivos ou erro na execução
        lista_dispositivos.insert(tk.END, "Nenhuma informação sobre dispositivos USB disponível.")
    else:
        # Exibe as informações dos dispositivos USB no terminal/console e na interface gráfica
        print("Dispositivos USB conectados:")
        for info in informacoes_usb:
            print(info)  # Mostra no terminal
            lista_dispositivos.insert(tk.END, info)  # Adiciona cada linha de informação no Listbox da interface

# Função para fechar o programa
def sair_programa():
    janela.quit()

# Criando a janela principal
janela = tk.Tk()
janela.title("Dispositivos USB conectados")

# Definindo o tamanho da janela (aumentando ainda mais)
janela.geometry("1200x800")  # 1200x800 pixels
janela.minsize(1200, 800)  # Tamanho mínimo

# Frame para colocar o Listbox e as barras de rolagem
frame_lista = tk.Frame(janela)
frame_lista.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

# Criando a barra de rolagem vertical
scrollbar_vertical = tk.Scrollbar(frame_lista, orient=tk.VERTICAL)
scrollbar_vertical.pack(side=tk.RIGHT, fill=tk.Y)

# Criando a barra de rolagem horizontal
scrollbar_horizontal = tk.Scrollbar(frame_lista, orient=tk.HORIZONTAL)
scrollbar_horizontal.pack(side=tk.BOTTOM, fill=tk.X)

# Criando o Listbox para exibir as informações dos dispositivos USB
lista_dispositivos = tk.Listbox(frame_lista, width=150, height=30, yscrollcommand=scrollbar_vertical.set, xscrollcommand=scrollbar_horizontal.set)
lista_dispositivos.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Conectando as barras de rolagem ao Listbox
scrollbar_vertical.config(command=lista_dispositivos.yview)
scrollbar_horizontal.config(command=lista_dispositivos.xview)

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
