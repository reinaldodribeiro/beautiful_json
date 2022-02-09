
from extension.order_json import OrderJson
import sys

def main():
  args = sys.argv[1::]
  if len(args) > 0:
    OrderJson(args).start()
  else:
    OrderJson().start()

if __name__ == '__main__':
  main()