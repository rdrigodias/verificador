# # Verificador de CloudFront - Documentação

O Verificador de CloudFront é um script em Python que verifica o status de uma lista de Clound usando a biblioteca python-telegram-bot. Ele envia notificações sobre o status de cada domínio para um chat no Telegram.

## Pré-requisitos

- Python 3 instalado
- pip3 instalado
- Acesso à internet para baixar as bibliotecas e o código do GitHub

## Instalação

1. Abra um terminal.
2. Execute o seguinte comando para baixar o script de instalação:

   ```bash
   wget https://raw.githubusercontent.com/rdrigodias/verificador/main/install.sh -O install.sh

3.Torne o arquivo install.sh executável com o comando:

chmod +x install.sh

4.Execute o script de instalação:

./install.sh

##Configuração

1.Após a instalação, você precisará configurar o token do bot Telegram e o ID do chat. Siga estas etapas:

2.Abra o arquivo /home/verificar_dominios2.py com um editor de texto.

3.Localize as seguintes linhas:

bot = telegram.Bot(token='AQUI_SEU_TOKEN')
chat_id = 'AQUI_SEU_ID'

4.Substitua 'AQUI_SEU_TOKEN' pelo token do seu bot Telegram e 'AQUI_SEU_ID' pelo ID do chat onde você deseja receber as mensagens de notificação.

5.Salve as alterações e feche o arquivo.

##Uso
Após a instalação e configuração, o Verificador de Domínios será executado automaticamente em intervalos regulares para verificar o status dos domínios listados no arquivo /home/dominios.txt.

As mensagens de notificação sobre o status de cada domínio serão enviadas para o chat configurado no Telegram.

##Suporte
Se você encontrar algum problema ou tiver dúvidas sobre o Verificador de Domínios, entre em contato com o autor do código.

##Contribuição
Se você deseja contribuir para o Verificador de Domínios, sinta-se à vontade para enviar pull requests com melhorias, correções de bugs ou novos recursos. O projeto está hospedado no GitHub em: https



