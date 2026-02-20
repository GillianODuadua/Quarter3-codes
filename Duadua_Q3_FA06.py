
student = {}
name = input("Enter your name: ")
age = input("Enter your age: ")
subject = input("Enter your favorite subject: ")

student["Enter your name:"] = name
student["Enter your age:"] = age
student["Enter your favorite subject:"] = subject

print("\nStudent Record:")
print("Name:", student["Enter your name:"])
print("Age:", student["Enter your age:"])
print("Favorite Subject:", student["Enter your favorite subject:"])