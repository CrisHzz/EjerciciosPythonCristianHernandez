if __name__ == "__main__":
    def media():
        data = input("Please enter a list of numbers separated by commas: ") #pedimos al usuario que introduzca una lista de numeros separados por comas
        list = [int(i) for i in data.split(",")]
        media = sum(list) / len(list) #la suma de los elementos de la lista dividido entre el numero de elementos de la lista
        print(f"The media of the list is: {media}")
        return media
media()
