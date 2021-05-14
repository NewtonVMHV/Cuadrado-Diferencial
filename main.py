def square(n):
    Square = []
    for i in range(n):
        l = []
        for j in range(n):
            l.append(0)
        Square.append(l)
    i = n // 2
    j = n - 1
    num = n * n
    count = 1
    while (count <= num):
        if (i == -1 and j == n):
            j = n - 2
            i = 0
        else:
            if (j == n):
                j = 0
            if (i < 0):
                i = n - 1
        if (Square[i][j] != 0):
            j = j - 2
            i = i + 1
            continue
        else:
            Square[i][j] = count
            count = count + 1
        i = i - 1
        j = j + 1
    for i in range(n):
        for j in range(n):
            print(Square[i][j], end=" ")
        print()
    print("La suma de la diagonal es:", (n * (n ** 2 + 1)) / 2)
n = int(input("Ingrese el tamaño de la Matriz que desea obtener: \n"))
square(n)
