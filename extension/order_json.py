import os
import json

def print_result(count):
  if count > 0:
    print(f'\033[1mObaaa, {count} arquivos estao bunitos agora =)')
  else:
    print("\033[93mNao encontramos nenhum arquivo json nessa pasta")

def order_dict(data):
  result = {}
  for k, v in sorted(data.items()):
    if isinstance(v, dict):
      result[k] = order_dict(v)
    else:
      result[k] = v
  return result

def process_file(file):
  with open(file, encoding='UTF-8') as json_data:
    data = json.load(json_data)
    final_data = order_dict(data)
  with open(file, 'w') as fp:
    json.dump(final_data, fp, indent=2, ensure_ascii=False)

def process_files_current_path():
  count = 0
  for p, _, files in os.walk(os.path.abspath('.')):
    for file in files :
      filename, extension = os.path.splitext(file)
      if extension.replace('.', '') == 'json':
        count+=1
        process_file(file)
  print_result(count)

def process_args_files(files):
  count = 0
  for file in files:
    if(os.path.isfile(file)):
      process_file(file)
      count+=1
    else:
      print(f'\033[93mO arquivo {file} não existe no directorio informado')
  print_result(count)

def start(files=None):
  try:
    if files == None:
      process_files_current_path()
    else:
      process_args_files(files)
  except:
    print(f'\033[93mNão foi possível processar os arquivos verifique o conteudo deles')

 
