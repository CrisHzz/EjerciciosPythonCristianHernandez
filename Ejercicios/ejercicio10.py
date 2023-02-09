if __name__ == "__main__":
    def factorial():
        number = int(input("Please enter a number: "))
        factorial = 1
        for i in range(1, number + 1):
            factorial = factorial * i
            print(f"The factorial of {number} is: {factorial}")
        return factorial



    factorial()
