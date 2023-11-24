import os
import datetime
import zipfile

#Automatizar a tarefa de backup da pasta /var/log


backup_dir = '~/Documents/backup'  #diretório de backup


if not os.path.exists(backup_dir):  
    os.mkdir(backup_dir)


# Cria um diretório dentro do diretório de backups para armazenar os backups de hoje.
# Usando o nome do dia atual, que podemos obter com a função `datetime.date.today()`.
today_date = datetime.date.today() 
formatted_date = today_date.strftime('%Y-%m-%d') 

target_dir = os.path.join(backup_dir, formatted_date) 
if not os.path.exists(target_dir): 
    os.mkdir(target_dir)

#O modulo zipfile cria um arquivo ZIP chamado `logs.zip` no diretório de destino.

with zipfile.ZipFile(os.path.join(target_dir, 'logs.zip'), 'w') as zip_ref: 
    # o módulo `os.walk()` será utilizado para percorrer todos arquivos e pastas do directório /var/log
    for root, _, files in os.walk('/var/log'):
        # Para cada arquivo encontrado, irei adicioná-lo ao arquivo ZIP.
        # O método `write()` do módulo `zipfile` será utilizado para isso.
        for file in files:
            zip_ref.write(os.path.join(root, file), arcname=os.path.relpath(os.path.join(root, file), '/var/log'))

# Por fim, é enviado uma mensagem informando que o backup foi concluído.
#Created backup archive for 2023-11-21 Logsx

print(f"Created backup archive for {formatted_date} Logs")