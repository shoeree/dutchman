from .api import *


def main():
    ap = AssetPairs(pair_name="ethcad").load()
    print(ap.data)


if __name__ == '__main__':
  main()

