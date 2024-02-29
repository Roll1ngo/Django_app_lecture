from uuid import uuid4

def main():
    for code in range(20):
        print(uuid4().hex)


if __name__ == '__main__':
    main()
