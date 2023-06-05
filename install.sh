#!/bin/bash

# Verificar se o Python está instalado
if ! command -v python3 &> /dev/null; then
    echo "Python3 não está instalado. Instalando..."
    sudo apt-get update
    sudo apt-get install python3 -y
fi

# Verificar se o pip está instalado
if ! command -v pip3 &> /dev/null; then
    echo "pip3 não está instalado. Instalando..."
    sudo apt-get update
    sudo apt-get install python3-pip -y
fi

# Instalar as bibliotecas necessárias
echo "Instalando as bibliotecas necessárias..."
sudo pip3 install python-telegram-bot

# Baixar o codigo do GitHub
echo "Baixando o código..."
wget https://raw.githubusercontent.com/rdrigodias/verificador/main/verificar_dominios2.py -O /home/verificar_dominios2.py

# Abrir o arquivo verificar_dominios2.py com o editor Nano
echo "Abrindo o arquivo com o editor Nano para configurar o token e o ID do chat. Pressione Ctrl + X para salvar e sair"
read -p "Pressione Enter para abrir o arquivo..."
nano /home/verificar_dominios2.py

# Baixar Arquivo Base
echo "Baixando arquivo de base..."
wget https://raw.githubusercontent.com/rdrigodias/verificador/main/meus-front.txt -O /home/meus-front.txt

# Adicionar os dominios manualmente
echo "Adicione os domínios um por linha. Pressione Ctrl + X para salvar e sair."
read -p "Pressione Enter para abrir o arquivo..."
nano /home/meus-front.txt

# Executar o código pela primeira vez
echo "Executando o código pela primeira vez..."
python3 /home/verificar_dominios2.py

# Configurar o cron job para executar a verificação a cada 5 minutos
echo "Configurando o cron job para executar a verificação a cada 5 minutos..."
(crontab -l ; echo "*/5 * * * * python3 /home/verificar_dominios2.py") | crontab -

echo "Instalação e configuração concluídas!"
