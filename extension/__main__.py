
from extension.order_json import start
import sys

def main():
  args = sys.argv[1::]
  if len(args) > 0:
    start(args)
  else:
    start()

if __name__ == '__main__':
  main()