class A:
    def greet(self):
        return "Hello from A"

class B(A):
    def greet(self):
        return "Hello from B"

class C(A):
    def greet(self):
        return "Hello from C"

class D(B, C):  # Multiple inheritance
    pass

# Demo - MRO in action
if __name__ == "__main__":
    obj = D()
    
    print("Method called:", obj.greet())
    print("MRO (Method Resolution Order):")
    for i, cls in enumerate(D.__mro__):
        print(f"{i+1}. {cls.__name__}")
    
    print("\nPython checks classes in this order to find the method")