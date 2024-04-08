import argparse

def main():
    parser = argparse.ArgumentParser(description='Script de ejemplo con argumentos.')
    parser.add_argument('-i', '--integer', type=int, help='Un número entero')
    parser.add_argument('-d', '--color', help='Un color')

    args = parser.parse_args()

    if args.integer:
        print('Número entero:', args.integer)
    if args.color:
        print('Color:', args.color)

if __name__ == '__main__':
    main()
