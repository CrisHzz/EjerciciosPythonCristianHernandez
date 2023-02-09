if __name__ == "__main__":
    data=input("Please enter a list of numbers separated by commas: ")
    list = [int(i) for i in data.split(",")]
    print(f"The biggest number of the list is: {max(list)}")
    print(f"The smallest number of the list is: {min(list)}")
