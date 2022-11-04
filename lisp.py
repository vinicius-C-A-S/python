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
ultimo=1
penultimo=1


if (n==1) or (n==2):
    print("1")
else:
    count=3
    while count <= n:
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        count += 1
    print(termo)

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

