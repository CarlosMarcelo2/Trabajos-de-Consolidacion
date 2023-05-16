todos = ["Harry Houdini", "Newton", "David Blaine", "Hawking", "Messi", "Teller", "Einstein", "Pelé", "Juanes"]
magos = ["Harry Houdini", "David Blaine", "Teller"]
cientificos = ["Newton", "Hawking", "Einstein"]
otros = ["Messi", "Pelé", "Juanes"]

def subrayar():
    for i in range(0,17):
        print("_", end="")
    print()

def hacer_grandioso():
    for m in range(len(magos)):
        magos[m] = "El gran " + magos[m]

def imprimir_nombres():
    for name in todos:
        print(name)

print("Lista de Nombres:")
subrayar()
imprimir_nombres()
hacer_grandioso()
print("\n   \n")

print("Magos Grandiosos:")
subrayar()
for magic in magos:
    print(magic)

print("\n   \n")

print("Científicos:")
subrayar()
for cientifico in cientificos:
    print(cientifico)
print("\n   \n")

print("Otros:")
subrayar()
for others in otros:
    print(others)
