if __name__ == "__main__":
        import random
        my_matriz = []
        for i in range(4): # la cantidad de posiciones que habran en la matriz
            my_matriz.append([])
            for j in range(4): # el tamaño de cada posicion que tendra la matriz
                my_matriz[i].append(random.randint(0, 9)) #append para unir y randit para generar numeros aleatorios
        print(f"The random matrix is: {my_matriz}")
