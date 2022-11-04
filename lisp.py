def fact(n):
    n = int(n)
    resultado = 1
    count = 1

    while count <= n:
        resultado *= count
        count += 1
        print(resultado)

def fibonacci(n):
    n = int(n)
    if n <= 1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

arquivo =[linhas.strip().split() for linhas in open("./input.dat").readlines()]

with open("output.dat","w") as out:
    l = 1
    for linha in arquivo:
        x, y = linha
        fx = fibonacci(int(x))
        fy = fact(int(y))
        exponencial = f"linha {l}: fibonacci: {fx}; fact: {fy}"
        out.write(exponencial)
        l+=1
        if 1 <= len(arquivo):
            out.write("\n")

