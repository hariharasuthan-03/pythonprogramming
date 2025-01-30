class UniqueCalculator:
    def __init__(self):
        self.history = []  
        self.last_result = None 

    def add(self, a, b):
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        self.last_result = result
        return result

    def subtract(self, a, b):
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        self.last_result = result
        return result

    def multiply(self, a, b):
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        self.last_result = result
        return result

    def divide(self, a, b):
        if b == 0:
            return "Error! Division by zero."
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        self.last_result = result
        return result

    def undo(self):
        if self.history:
            self.history.pop()
            if self.history:
                last_op = self.history[-1]
                self.last_result = float(last_op.split('=')[-1].strip())
            else:
                self.last_result = None
            return f"Last operation undone. Current result: {self.last_result if self.last_result is not None else 'None'}"
        else:
            return "No operations to undo."

    def view_history(self):
        if self.history:
            print("Operation History:")
            for operation in self.history:
                print(operation)
        else:
            print("No operations performed yet.")

    def run(self):
        print("Unique Calculator")
        while True:
            print("\nOptions:")
            print("1. Addition")
            print("2. Subtract")
            print("3. Multiply")
            print("4. Divide")
            print("5. View History")
            print("6. Undo last operation")
            print("7. Exit")

            choice = input("Choose an operation (1-7): ")

            if choice == "1":
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                print(f"Result: {self.add(a, b)}")
            elif choice == "2":
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                print(f"Result: {self.subtract(a, b)}")
            elif choice == "3":
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                print(f"Result: {self.multiply(a, b)}")
            elif choice == "4":
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                print(f"Result: {self.divide(a, b)}")
            elif choice == "5":
                self.view_history()
            elif choice == "6":
                print(self.undo())
            elif choice == "7":
                print("Exiting calculator. Goodbye!")
                break
            else:
                print("Invalid choice! Please choose a number between 1 and 7.")

if __name__ == "__main__":
    calculator = UniqueCalculator()
    calculator.run()
