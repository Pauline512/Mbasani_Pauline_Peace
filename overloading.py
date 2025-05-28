class Calculator:
    def add(self, *args):
        """Method overloading using *args to handle different parameter counts"""
        
        if len(args) == 2:
            # Two numbers
            return args[0] + args[1]
        
        elif len(args) == 3:
            # Three numbers
            return args[0] + args[1] + args[2]
        
        elif len(args) == 1 and isinstance(args[0], list):
            # List of numbers
            return sum(args[0])
        
        else:
            # Any number of arguments
            return sum(args)

# Demo usage
if __name__ == "__main__":
    calc = Calculator()
    
    # Same method name, different number of arguments
    print(f"5 + 3 = {calc.add(5, 3)}")
    print(f"5 + 3 + 2 = {calc.add(5, 3, 2)}")
    print(f"Array sum = {calc.add([1, 2, 3, 4, 5])}")
    print(f"Multiple args = {calc.add(1, 2, 3, 4, 5, 6)}")