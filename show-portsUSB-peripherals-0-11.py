import tkinter as tk
import subprocess

# Mapeamento simples de dispositivos comuns (para tradução automática)
DISPOSITIVOS_COMUNS = {
    "Keyboard": "Teclado",
    "Mouse": "Rato",
    "HID-compliant": "Dispositivo HID (Ex: Controle ou Teclado)",
    "Mass Storage": "Armazenamento em Massa (Ex: Pen Drive)",
    "Printer": "Impressora",
    "Audio": "Dispositivo de Áudio",
    "Webcam": "Câmera"
}

# Função para capturar informações das portas USB e dispositivos conectados
def obter_informacoes_usb():
    try:
        # Executa o comando `wmic` para listar dispositivos USB e captura a saída
        resultado_dispositivos = subprocess.run(['wmic', 'path', 'Win32_PnPEntity', 'where', "PNPClass='USB'", 'get', 'Name,DeviceID'], capture_output=True, text=True)
        resultado_portas = subprocess.run(['wmic', 'path', 'Win32_USBHub', 'get', 'DeviceID,Name'], capture_output=True, text=True)

        # Processa os dispositivos USB conectados
        dispositivos = resultado_dispositivos.stdout.splitlines()
        portas = resultado_portas.stdout.splitlines()

        dispositivos_traduzidos = []
        for dispositivo in dispositivos:
            dispositivo = dispositivo.strip()
            if dispositivo:  # Ignora linhas vazias
                dispositivo_traduzido = dispositivo
                for termo_ingles, termo_portugues in DISPOSITIVOS_COMUNS.items():
                    if termo_ingles in dispositivo:
                        dispositivo_traduzido = dispositivo.replace(termo_ingles, termo_portugues)
                        break
                dispositivos_traduzidos.append(dispositivo_traduzido)

        # Adiciona as informações sobre as portas USB
        dispositivos_e_portas = []
        for dispositivo in dispositivos_traduzidos:
            for porta in portas:
                if dispositivo.split()[0] in porta:  # Verifica se a DeviceID coincide
                    dispositivos_e_portas.append(f"{dispositivo} - {porta}")
                    break
            else:
                dispositivos_e_portas.append(f"{dispositivo} - Porta desconhecida")

        return dispositivos_e_portas

    except FileNotFoundError:
        return ["Erro: 'wmic' não encontrado no sistema."]
    except Exception as e:
        return [f"Erro ao executar o comando: {str(e)}"]

# Função para atualizar a lista de dispositivos USB e suas portas na interface gráfica
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
janela.title("Dispositivos USB e Portas")

# Criando o Listbox para exibir as informações dos dispositivos USB
lista_dispositivos = tk.Listbox(janela, width=100, height=20)
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
