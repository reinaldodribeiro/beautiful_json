import os
import json

def order_dict(data):
  result = {}
  for k, v in sorted(data.items()):
    if isinstance(v, dict):
      result[k] = order_dict(v)
    else:
      result[k] = v
  return result

def start():
  count = 0
  for p, _, files in os.walk(os.path.abspath('.')):
    for file in files :
      filename, extension = os.path.splitext(file)
      if extension.replace('.', '') == 'json':
        count+=1
        with open(file, encoding='utf-8') as json_data:
          data = json.load(json_data)
          final_data = order_dict(data)
          with open(file, 'w') as fp:
            json.dump(final_data, fp, indent=2, ensure_ascii=False)
      
  if count > 0:
    print(f'\033[1mObaaa, {count} arquivos estao bunitos agora =)')
  else:
    print("\033[93mNao encontramos nenhum arquivo json nessa pasta")

 
