if __name__ == "__main__":
    data=input("Please enter a list of numbers separated by commas: ")
    list=[int(i) for i in data.split(",")] #Se convierte la lista de strings a lista de enteros
    print(sum(list))


