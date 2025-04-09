#!/bin/bash

echo "Listando arquivos no repositório..."
ls
echo "Caminho atual:"
pwd

# Instala o mailutils
sudo apt-get update
sudo apt-get install -y mailutils

# Envia o e-mail
echo "Pipeline executado com sucesso!" | mail -s "CI/CD - Notificação" "$EMAIL_DESTINO"