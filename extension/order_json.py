import os
import json
class OrderJson:

  def __init__(self, files=None) -> None:
    self.files = files
    self.count = 0    

  def print_result(self):
    if self.count > 0:
      print(f'\033[1mObaaa, {self.count} arquivos estao bunitos agora =)')
    else:
      print("\033[93mNão foi processado nenhum arquivo dentro do directorio informado")

  def order_dict(self, data):
    result = {}
    for k, v in sorted(data.items()):
      if isinstance(v, dict):
        result[k] = self.order_dict(v)
      else:
        result[k] = v
    return result

  def process_file(self, file):
    try:
      with open(file, encoding='UTF-8') as json_data:
        data = json.load(json_data)
        final_data = self.order_dict(data)
      with open(file, 'w') as fp:
        json.dump(final_data, fp, indent=2, ensure_ascii=False)
        self.count+=1
    except:
      print(f'\033[93mNão foi possível processar o arquivo {file}')

  def process_files_current_path(self):
    for path, dir, files in os.walk(os.path.abspath('.')):
      for file in files :
        filename, extension = os.path.splitext(file)
        if extension.replace('.', '') == 'json':
          self.process_file(f"{path}/{file}")

    self.print_result()

  def process_args_files(self):
    for file in self.files:
      if(os.path.isfile(file)):
        self.process_file(file)
      else:
        print(f'\033[93mO arquivo {file} não existe no directorio informado')
    self.print_result()

  def start(self):
    if self.files == None:
      self.process_files_current_path()
    else:
      self.process_args_files()
   
  
  
 
