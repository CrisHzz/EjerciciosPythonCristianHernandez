if __name__ == "__main__":
    def invertirnumeroslista():
        data=input("Please enter a list of numbers separated by commas: ")
        list = [int(i) for i in data.split(",")]
        list.reverse()
        print(f"The list of numbers in reverse order of the list is: {list}")
        return list
    invertirnumeroslista()
