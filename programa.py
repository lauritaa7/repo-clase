from sys import argv

def __main__():
    print("Hola mundo!")
    if len(argv) > 1:
        print("Tenemos más de un argumento:")
        for item in argv:
            print(item)

if __name__ == '__main__':
    __main__()