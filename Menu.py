def main():
    app = main()
    while True:
        print("1. Insertar documento")
        print("2. Actualizar documento")
        print("3. Reemplazar documento")
        print("4. Eliminar documento")
        print("5. Mostrar todos los documentos")
        print("6. Búsqueda de documento")
        print("7. Eliminar todos los documentos")
        print("8. Salir")

        choice = input("Seleccione una opción: ")

        if choice == '1':
            collection_name = input("Ingrese el nombre de la colección: ")
            document = {}
            app.insert_document(collection_name, document)
        elif choice == '2':
            # Implementar la actualización de documentos
            pass
        elif choice == '3':
            # Implementar el reemplazo de documentos
            pass
        elif choice == '4':
            # Implementar la eliminación de documentos
            pass
        elif choice == '5':
            # Implementar la visualización de todos los documentos
            pass
        elif choice == '6':
            # Implementar la búsqueda de documentos
            pass
        elif choice == '7':
            # Implementar la eliminación de todos los documentos
            pass
        elif choice == '8':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()