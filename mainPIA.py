from CursoTema import cursoTema

print("***** MENU INICIAL *****")
print("1.- Empleados\n2.- Cursos\n3.- Temas\n4.- Videos\n5.- Temas asignados al curso\n6.- Videos asignados a un tema")

opcionInicial = int(input("\nElija una opcion: "))

if opcionInicial == 1:
    print("\n***** EMPLEADOS *****")
    print("1.- Agregar\n2.- Borrar\n3.- Modificar\n4.- Consultar todo\n5.- Ver detalles")
    opcion1 = int(input("\nElija una opcion: "))

if opcionInicial == 2:
    print("\n***** CURSOS *****")
    print("1.- Agregar\n2.- Borrar\n3.- Modificar\n4.- Consultar todo\n5.- Ver detalles")
    opcion2 = int(input("\nElija una opcion: "))

if opcionInicial == 3:
    print("\n***** TEMAS *****")
    print("1.- Agregar\n2.- Borrar\n3.- Modificar\n4.- Consultar todo\n5.- Ver detalles")
    opcion3 = int(input("\nElija una opcion: "))

if opcionInicial == 4:
    print("\n***** VIDEOS *****")
    print("1.- Agregar\n2.- Borrar\n3.- Modificar\n4.- Consultar todo\n5.- Ver detalles")
    opcion4 = int(input("\nElija una opcion: "))

if opcionInicial == 5:
    print("\n***** TEMAS ASIGNADOS AL CURSO *****")
    print("1.- Agregar\n2.- Borrar\n3.- Modificar\n4.- Consultar todo\n5.- Ver detalles")
    opcion5 = int(input("\nElija una opcion: "))

    if opcion5 == 1:
        idCurso = int(input("Ingrese el id del curso: "))
        idTema = int(input("Ingrese el id del tema: "))
        idCursoTema = int(input("Ingrese id nuevo para guardarlo: "))
        ct = cursoTema(idCursoTema, idCurso, idTema)
        ct.agregar()

if opcionInicial == 6:
    print("\n***** VIDEOS ASIGNADOS A UN TEMA *****")
    print("1.- Agregar\n2.- Borrar\n3.- Modificar\n4.- Consultar todo\n5.- Ver detalles")
    opcion6 = int(input("\nElija una opcion: "))
