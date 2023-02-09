if __name__ == "__main__":
        list = []
        for i in range(1, 101): #ciclo de los 100 numeros pares
            if i % 2 == 0: #condicion para que solo se impriman los numeros pares
                list.append(i)
        print(f"The list of even numbers is: {list}")

