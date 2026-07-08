A= float(input("Ingrese el valor del área de la base:  "))
H= float(input("Ingrese el valor de la altura:  "))
B= float(input("Ingrese el valor del perímetro de la base:  "))
def volumen_piramide(A, H, B):
    V= (1/3)*A*H*B
    return V
print("El volumen de la pirámide es: ", volumen_piramide(A, H, B))
