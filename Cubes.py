
# Method 1: Simple calculation
number = 3
cube = number ** 3
print(f

"The cube of {number} is {cube}")

# Method 2: Cubing a range of numbers
print("\nCubing numbers from 1 to 5:")
for x in range(1, 6):
    print(f"{x} cubed is {x**3}")

# Method 3: Using a function (Professional approach)
def get_cube(num):
    return num * num * num

print(f"\nUsing a function for 10: {get_cube(10)}")