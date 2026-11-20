import os
import subprocess
import time
import sys

os.system("title PyAssistent")
print("============================")
print("| Bem-vindo ao PyAssistent |")
print("============================")
print()

pyw = input("O que vai fazer agora? ").lower().strip()

if pyw == "exit" or pyw == "sair" or pyw == "fechar":
    print("Fechando...")
    time.sleep(2)
    sys.exit()
elif pyw == "help" or pyw == "ajuda":
    os.startfile("paths_.md")
    sys.exit()
elif pyw == "jogar" or pyw == "play":
    print("Iniciando seu app de jogos...")
    try:
        os.startfile("steam://open/main")
    except OSError:
        try:
            os.startfile("xbox://")
        except OSError:
            print("Nenhum app de jogos encontrado. Suporte a Epic Games e GOG chegando em breve.")
    time.sleep(5)
    sys.exit()            
elif pyw == "programar" or pyw == "code":
    print("Abrindo Python...")
    subprocess.Popen([sys.executable, "-m", "idlelib"])
    time.sleep(3)
    sys.exit()

elif pyw == "navegar" or pyw == "internet":
    print("Abrindo navegador...")
    os.startfile("http://")
    time.sleep(3)
    sys.exit()

elif pyw == "arquivos" or pyw == "files":
    print("Abrindo File Explorer...")
    os.startfile("explorer")
    time.sleep(2)
    sys.exit()

elif pyw == "nota" or pyw == "note":
    print("Abrindo Bloco de Notas...")
    os.startfile("notepad")
    time.sleep(2)
    sys.exit()

elif pyw == "cmd":
    print("Abrindo Prompt de Comando...")
    os.system("start cmd")
    time.sleep(2)
    sys.exit()

elif pyw == "config":
    print("Abrindo Configurações...")
    os.startfile("ms-settings:")
    time.sleep(2)
    sys.exit()

elif pyw == "desligar" or pyw == "shutdown":
    print("Desligando o computador em 5 segundos...")
    os.system("shutdown /s /t 5")
    time.sleep(2)
    sys.exit()

elif pyw == "reiniciar" or pyw == "restart":
    print("Reiniciando o computador em 5 segundos...")
    os.system("shutdown /r /t 5")
    time.sleep(2)
    sys.exit()

elif pyw == "calc":
    print("Abrindo calculadora...")
    os.startfile("calc.exe")
    time.sleep(3)
    sys.exit()

else:
    print("Comando não reconhecido!")
    time.sleep(2)
    sys.exit()
