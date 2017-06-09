from api import *


def main():
    ap = AssetPairs(pair_name="ethcad")
    ap.fetch()
    print(ap.data)


if __name__ == '__main__':
  main()

