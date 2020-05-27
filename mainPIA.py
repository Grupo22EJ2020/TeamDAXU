from CursoTema import cursoTema
from Video import video
from CursoTemaVideo import cursotemavideo
from Temas import Tema

while True:

    print("\n***** MENU INICIAL *****\n")
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

        if opcion3 == 1:
            idTema = int(input("Ingrese el id del tema: "))
            nombre = (input("Ingrese el nombre del tema: "))
            t = Tema(idTema, nombre)
            t.agregar()
            input("\nPresiona enter para continuar...\n")


    if opcionInicial == 4:
        print("\n***** VIDEOS *****")
        print("1.- Agregar\n2.- Borrar\n3.- Modificar\n4.- Consultar todo\n5.- Ver detalles")
        opcion4 = int(input("\nElija una opcion: "))

        if opcion4 == 1:
            idVideo = int(input("Ingrese el id para guardar el Video: "))
            nombre = (input("Ingrese el nombre del Video: "))
            url = (input("Ingrese el url del Video: "))
            fechapublicacion = (input("Ingrese la Fecha de Publicación del Video: "))
            v = video(idVideo, nombre, url, fechapublicacion)
            v.agregar()
            input("\nPresiona enter para continuar...\n")

        if opcion4 == 2:
            idVideo =  int(input("Ingrese el id del Video: "))
            nombre = (input("Ingrese el nombre del Video: "))
            url = (input("Ingrese el url del Video: "))
            fechapublicacion = (input("Ingrese la Fecha de Publicación del Video: "))
            v = video(idVideo, nombre, url, fechapublicacion)
            v.borrar()
            input("\nPresiona enter para continuar...\n")

    if opcionInicial == 5:
        print("\n***** TEMAS ASIGNADOS AL CURSO *****")
        print("1.- Agregar\n2.- Borrar\n3.- Modificar\n4.- Consultar todo\n5.- Ver detalles")
        opcion5 = int(input("\nElija una opcion: "))

        if opcion5 == 1:
            idCurso = int(input("Ingrese el id del curso: "))
            idTema = int(input("Ingrese el id del tema: "))
            idCursoTema = int(input("Ingrese id para guardarlo: "))
            ct = cursoTema(idCursoTema, idCurso, idTema)
            ct.agregar()
            input("\nPresiona enter para continuar...\n")

        if opcion5 == 2:
            idCurso = int(input("Ingrese el id del curso: "))
            idTema = int(input("Ingrese el id del tema: "))
            idCursoTema = int(input("Ingrese idCursoTema: "))
            ctd = cursoTema(idCursoTema, idCurso, idTema)
            ctd.borrar()
            input("\nPresiona enter para continuar...\n")

        if opcion5 == 3:
            idCurso = int(input("Ingrese el id del curso a modificar: "))
            idTema = int(input("Ingrese el id del tema a modificar: "))
            idCursoTema = int(input("Ingrese idCursoTema a modificar: "))
            ctb = cursoTema(idCursoTema, idCurso, idTema)
            ctb.borrar()
            idCurso = int(input("Ingrese el nuevo id del curso: "))
            idTema = int(input("Ingrese el nuevo id del tema: "))
            idCursoTema = int(input("Ingrese el nuevo id para guardarlo: "))
            ctm = cursoTema(idCursoTema, idCurso, idTema)
            ctm.agregar()
            input("\nPresiona enter para continuar...\n")

        if opcion5 == 4:
            ct = cursoTema(None, None, None)
            ct.consultar()
            input("\nPresiona enter para continuar...\n")
    
    if opcionInicial == 6:
        print("\n***** VIDEOS ASIGNADOS A UN TEMA *****")
        print("1.- Agregar\n2.- Borrar\n3.- Modificar\n4.- Consultar todo\n5.- Ver detalles")
        opcion6 = int(input("\nElija una opcion: "))

        if opcion6 == 1:
            idCT = int(input("Ingrese el id del CursoTema: "))
            idV = int(input("Ingrese el id del Video que quiere asignar: "))
            idCursoTV = int(input("Ingrese el id para guardarlo: "))
            ctv = cursotemavideo(idCursoTV, idCT, idV)
            ctv.agregar()
            input("\nPresiona enter para continuar...\n")

        if opcion6 == 2: 
            idCT = int(input("Ingrese el id del CursoTema: "))
            idV = int(input("Ingrese el id del Video: "))
            idCursoTV = int(input("Ingrese idCursoTemaVideo: "))
            ctv = cursotemavideo(idCursoTV, idCT, idV)
            ctv.borrar()
            input("\nPresiona enter para continuar...\n")

        if opcion6 == 3:
            idCT = int(input("Ingrese el id del CursoTema a modificar: "))
            idV = int(input("Ingrese el id del video a modificar: "))
            idCursoTV = int(input("Ingrese idCursoTemaVideo a modificar: "))
            ctv = cursotemavideo(idCursoTV, idCT, idV)
            ctv.borrar()
            print("------------------------------")
            idCT = int(input("Ingrese el nuevo id del CursoTema: "))
            idV = int(input("Ingrese el nuevo id del video: "))
            idCursoTV = int(input("Ingrese el nuevo id para guardarlo: "))
            ctv = cursotemavideo(idCursoTV, idCT, idV)
            ctv.agregar()
            input("\nPresiona enter para continuar...\n")

        if opcion6 == 4:
            ctv = cursotemavideo(None, None, None)
            ctv.consultar()
            input("\nPresiona enter para continuar...\n")
