import tkinter as tk
import subprocess

# Função para capturar a saída do comando `wmic` e obter informações dos dispositivos USB
def obter_informacoes_usb():
    try:
        # Executa o comando `wmic` para listar dispositivos USB e captura a saída
        resultado = subprocess.run(['wmic', 'path', 'Win32_USBControllerDevice', 'get', 'Dependent'], capture_output=True, text=True)
        return resultado.stdout.splitlines()  # Retorna a saída como uma lista de strings (linhas)
    except FileNotFoundError:
        return ["Erro: 'wmic' não encontrado no sistema."]  # Caso o comando não seja encontrado
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
            if info.strip():  # Ignora linhas vazias
                print(info)  # Mostra no terminal
                lista_dispositivos.insert(tk.END, info)  # Adiciona cada linha de informação no Listbox da interface

# Função para fechar o programa
def sair_programa():
    janela.quit()

# Criando a janela principal
janela = tk.Tk()
janela.title("Informações sobre Portas USB e Periféricos")

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
