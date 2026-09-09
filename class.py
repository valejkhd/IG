class Estudiantes:
    def __init__(self, nombre, edad, carrera, semestre):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
        self.semestre = semestre

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Carrera: {self.carrera}, Semestre: {self.semestre}"

class Libros:
    def __init__(self, titulo, autor, anio, genero):
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio    
        self.genero = genero

    def __str__(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Año de Publicación: {self.anio_publicacion}"


class Vehiculos:
    def __init__(self, marca, modelo, anio, color):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.color = color

    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.anio}, Color: {self.color}"


class Productos:
    def __init__(self, nombre, precio, cantidad, categoria):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.categoria = categoria

    def valor_total(self):
        return self.precio * self.cantidad

    def __str__(self):
        return f"Producto: {self.nombre}, Precio: ${self.precio:.2f}, Cantidad: {self.cantidad}"

class Animales:
    def __init__(self, especie, nombre, edad, habitat):
        self.especie = especie
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat

    def __str__(self):
        return f"Especie: {self.especie}, Nombre: {self.nombre}, Edad: {self.edad}, Hábitat: {self.habitat}"    

def main():
     estudiantes = [
        Estudiantes("Ana", 20, "Ingeniería", 3),
        Estudiantes("Luis", 22, "Medicina", 5),
        Estudiantes("Carla", 19, "Derecho", 2),
        Estudiantes("Pedro", 21, "Arquitectura", 4),
        Estudiantes("María", 23, "Psicología", 6)
    ]
     libros = [
        Libros("Cien Años de Soledad", "Gabriel García Márquez", 1967, "Novela"),
        Libros("1984", "George Orwell", 1949, "Distopía"),
        Libros("To Kill a Mockingbird", "Harper Lee", 1960, "Ficción"),
        Libros("El Principito", "Antoine de Saint-Exupéry", 1943, "Fábula"),
        Libros("Moby Dick", "Herman Melville", 1851, "Aventura")
    ]
     vehiculos = [
        Vehiculos("Toyota", "Corolla", 2020, "Blanco"),
        Vehiculos("Honda", "Civic", 2019, "Negro"),
        Vehiculos("Ford", "Mustang", 2021, "Rojo"),
        Vehiculos("Chevrolet", "Camaro", 2022, "Azul"),
        Vehiculos("BMW", "X5", 2023, "Blanco")
    ]
     productos = [
        Productos("Laptop", 1500.00, 5, "Electrónica"),
        Productos("Libro", 20.00, 10, "Educación"),
        Productos("Zapatos", 100.00, 7, "Moda"),
        Productos("Teléfono", 800.00, 3, "Electrónica"),
        Productos("Mochila", 50.00, 8, "Accesorios")
    ]
     animales = [
        Animales("León", "Simba", 5, "Savana"),
        Animales("Elefante", "Dumbo", 10, "Selva"),
        Animales("Pingüino", "Pingu", 2, "Antártida"),
        Animales("Hipopótamo", "Hippo", 8, "Río"),
        Animales("Girafa", "Melman", 6, "Savana")
    ]
     print("Estudiantes:")
     for estudiante in estudiantes:
         print(estudiante)
     print("\nLibros:")
     for libro in libros:
         print(libro)
     print("\nVehículos:")
     for vehiculo in vehiculos:
         print(vehiculo)
     print("\nProductos:")
     for producto in productos:
         print(producto)
     print("\nAnimales:")
     for animal in animales:
         print(animal)
if __name__ == "__main__":
    main()