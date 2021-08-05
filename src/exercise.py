def main():
    #write your code below this line
    with open("data.txt",'r') as f:
        file = f.read().splitlines()

    for line in file:
        print(line)

if __name__ == '__main__':
    main()
