import tkinter as tk
import subprocess

# Mapeamento simples de dispositivos de entrada para português
DISPOSITIVOS_ENTRADA = {
    "Keyboard": "Teclado",
    "Mouse": "Rato",
    "HID-compliant": "Dispositivo HID (Ex: Controle ou Teclado)"
}

# Função para capturar informações sobre o teclado
def obter_teclado():
    try:
        resultado_teclado = subprocess.run(['wmic', 'path', 'Win32_Keyboard', 'get', 'Name,DeviceID'], capture_output=True, text=True)
        teclados = resultado_teclado.stdout.splitlines()
        return [linha.strip() for linha in teclados if linha.strip()]
    except Exception as e:
        return [f"Erro ao obter informações do teclado: {str(e)}"]

# Função para capturar informações sobre o rato
def obter_rato():
    try:
        resultado_rato = subprocess.run(['wmic', 'path', 'Win32_PointingDevice', 'get', 'Name,DeviceID'], capture_output=True, text=True)
        ratos = resultado_rato.stdout.splitlines()
        return [linha.strip() for linha in ratos if linha.strip()]
    except Exception as e:
        return [f"Erro ao obter informações do rato: {str(e)}"]

# Função para capturar informações gerais sobre dispositivos USB
def obter_informacoes_usb():
    try:
        resultado_usb = subprocess.run(['wmic', 'path', 'Win32_USBControllerDevice', 'get', 'Dependent'], capture_output=True, text=True)
        usb_devices = resultado_usb.stdout.splitlines()
        return [linha.strip() for linha in usb_devices if linha.strip()]
    except Exception as e:
        return [f"Erro ao obter informações USB: {str(e)}"]

# Função para traduzir dispositivos de entrada (rato e teclado) para português
def traduzir_dispositivo(dispositivo):
    for termo_ingles, termo_portugues in DISPOSITIVOS_ENTRADA.items():
        if termo_ingles in dispositivo:
            return dispositivo.replace(termo_ingles, termo_portugues)
    return dispositivo

# Função para atualizar a lista de dispositivos USB e suas portas na interface gráfica
def atualizar_lista_dispositivos():
    lista_dispositivos.delete(0, tk.END)  # Limpa a lista atual no Listbox
    
    # Obtém informações de teclado e rato
    teclados = obter_teclado()
    ratos = obter_rato()
    
    # Exibe as informações de teclado
    if teclados:
        lista_dispositivos.insert(tk.END, "Teclado(s) conectado(s):")
        for teclado in teclados:
            lista_dispositivos.insert(tk.END, traduzir_dispositivo(teclado))
    else:
        lista_dispositivos.insert(tk.END, "Nenhum teclado encontrado.")
    
    # Exibe as informações de rato
    if ratos:
        lista_dispositivos.insert(tk.END, "Rato(s) conectado(s):")
        for rato in ratos:
            lista_dispositivos.insert(tk.END, traduzir_dispositivo(rato))
    else:
        lista_dispositivos.insert(tk.END, "Nenhum rato encontrado.")
    
    # Exibe outras informações de dispositivos USB
    usb_devices = obter_informacoes_usb()
    lista_dispositivos.insert(tk.END, "")
    lista_dispositivos.insert(tk.END, "Outros dispositivos USB:")
    if usb_devices:
        for usb in usb_devices:
            lista_dispositivos.insert(tk.END, usb)
    else:
        lista_dispositivos.insert(tk.END, "Nenhum dispositivo USB adicional encontrado.")

# Função para fechar o programa
def sair_programa():
    janela.quit()

# Criando a janela principal
janela = tk.Tk()
janela.title("Dispositivos USB conectados (Teclado e Rato)")

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
