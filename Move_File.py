import os
import shutil

from_dir = 'C:/Users/leona/Downloads'
to_dir = 'C:/Users/leona/Documents/Arquivos_Documentos'

list_of_files = os.listdir(from_dir)
document_ext_list = ['.txt', '.doc', '.docx', '.pdf']

for file_name in list_of_files:
  root, ext = os.path.splitext(file_name)
  if(ext == ""):
    continue

  if ext in document_ext_list:
    path1 = from_dir + '/' + file_name
    path2 = to_dir + '/'
    path3 = to_dir + '/' + file_name

    if os.path.exists(path2):
      print('Movendo ' + file_name + '.....')
      shutil.move(path1, path3)
    else:
      print('Criando a pasta...')
      os.makedirs(path2)
      print('Movendo ' + file_name + '.....')
      shutil.move(path1, path3)