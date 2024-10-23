class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        # Vector Addition
        result = Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        return result

    def __mul__(self, other):
        # Dot product
        dot_product = (self.x * other.x + self.y * other.y + self.z * other.z)
        return dot_product

    def __xor__(self, other):
        # Cross product
        cross_x = self.y * other.z - self.z * other.y
        cross_y = self.z * other.x - self.x * other.z
        cross_z = self.x * other.y - self.y * other.x
        return Vector(cross_x, cross_y, cross_z)

    def __str__(self):
        # Returning vector in i, j, k form
        return f"Vector({self.x}i + {self.y}j + {self.z}k)"


def input_vector():
    # Function to take vector input from the user
    x = float(input("Enter x component: "))
    y = float(input("Enter y component: "))
    z = float(input("Enter z component: "))
    return Vector(x, y, z)


# Input vectors from the user
print("Input first vector:")
v1 = input_vector()

print("\nInput second vector:")
v2 = input_vector()

print("\nInput third vector:")
v3 = input_vector()

# Perform Operations
print("\nAddition:", v1 + v2)
print("Dot Product:", v1 * v2)
print("Cross Product:", v1 ^ v2)

print("Addition:", v1 + v3)
print("Dot Product:", v1 * v3)
print("Cross Product:", v1 ^ v3)
