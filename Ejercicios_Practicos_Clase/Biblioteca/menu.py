from book import Book
from library import Library
class Menu:
    def __init__(self):
        self.library = Library()
        print("--------------------------")
        print("=== Biblioteca ===")
        print("1. Mostrar Libros")  # Opción para sumar
        print("2. Añadir Libro")  # Opción para restar
        print("3. Coger Libro Prestado")  # Opción para multiplicar
        print("4. Devolver Libro")  # Opción para dividir
        print("5. Salir")  # Opción para salir del programa

    def seleccionar_opcion(self):
        opcion = input("\nElige una opción (1-5):")  # Solicita una opción entre 1 y 5
        if opcion == "1":
            self.library.show_books()
        return opcion
