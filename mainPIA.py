from CursoTema import cursoTema
from Video import video
from CursoTemaVideo import cursotemavideo
from Temas import Tema

while True:

    print("\n***** MENU INICIAL *****\n")
    print("1.- Empleados\n2.- Cursos\n3.- Temas\n4.- Videos\n5.- Temas asignados al curso\n6.- Videos asignados a un tema\n7.- SALIR")

    opcionInicial = int(input("\nElija una opcion: "))

    if opcionInicial == 1:
        print("\n***** EMPLEADOS *****")
        print("1.- Agregar\n2.- Borrar\n3.- Modificar\n4.- Consultar todo\n5.- Ver detalles")
        opcion1 = int(input("\nElija una opcion: "))

    if opcionInicial == 2:
        print("\n***** CURSOS *****")
        print("1.- Agregar\n2.- Borrar\n3.- Modificar\n4.- Consultar todo\n5.- Ver detalles")
        opcion2 = int(input("\nElija una opcion: "))

        if opcion2 == 1:
            idCurso = int(input("Ingrese el id para guardar el Curso: "))
            descripcion = (input("Ingrese la descripción del Curso: "))
            idEmpleado = int(input("Ingrese el id del Empleado "))
            C = curso(idCurso, descripcion, idEmpleado)
            C.agregar()
            print("\nListo!\n")
            input("\nPresiona enter para continuar...\n")

        if opcion2 == 2:
            idCurso = int(input("Ingrese el id del Curso: "))
            descripcion = (input("Ingrese la descripcion del Curso: "))
            idEmpleado = int(input("ingrese el id del Empleado: "))
            C = curso(idCurso, descripcion, idEmpleado)
            C.borrar()
            print("\nListo!\n")
            input("\nPresiona enter para continuar...\n")

        if opcion2 == 3:
            C = curso(None, None, None)
            C.consultar()
            print("\n**Tome los datos de la informacion de arriba**\n")
            idCurso = int(input("Ingrese el id del Curso a modificar: "))
            descripcion = (input("Ingrese la descripción a modificar: "))
            idEmpleado = int(input("Ingrese la id del Empleado a modificar: "))
            C = curso(idCurso, descripcion, idEmpleado)
            C.borrar()
            print("------------------------------")
            idCurso = int(input("Ingrese el nuevo id del Curso: "))
            descripcion = (input("Ingrese la nueva descripcion del Curso: "))
            idEmpleado = int(input("Ingrese rl id nuevo del Empleado: "))
            C = curso(idCurso, descripcion, idEmpleado)
            C.agregar()
            print("\nListo!\n")
            input("\nPresiona enter para continuar...\n") 

        if opcion2 == 4:
            C = curso(None, None, None)
            C.consultar()
            input("\nPresiona enter para continuar...\n")

    if opcionInicial == 3:
        print("\n***** TEMAS *****")
        print("1.- Agregar\n2.- Borrar\n3.- Modificar\n4.- Consultar todo\n5.- Ver detalles")
        opcion3 = int(input("\nElija una opcion: "))

        if opcion3 == 1:
            idTema = int(input("Ingrese el id del tema: "))
            nombre = input("Ingrese el nombre del tema: ")
            t = Tema(idTema, nombre)
            t.agregar()
            input("\nPresiona enter para continuar...\n")

        if opcion3 == 2:
            idTema = int(input("Ingrese el id del tema: "))
            nombre = int(input("Ingrese el nombre del tema: "))
            t = Tema(idTema, nombre)
            t.borrar()
            input("\nPresiona enter para continuar...\n")

        if opcion3 == 3:
            t = Tema(None, None)
            t.consultar()
            print("\n**Tome los datos de la informacion de arriba**\n")
            idTema = int(input("Ingrese el id del tema que desea modificar: "))
            nombre = int(input("Ingrese el nombre del tema que desea modificar: "))
            t = Tema(idTema, nombre)
            t.borrar()
            print("--------------------------------------")
            idTema = int(input("Ingrese el nuevo id del tema: "))
            nombre = int(input("Ingrese el nuevo nombre del tema: "))
            t = Tema(idTema, nombre)
            t.agregar()
            print("\nListo!\n")
            input("\nPresiona enter para continuar...\n")

        if opcion3 == 4:
            t = Tema (None, None)
            t.consultar()
            input("\nPresiona enter para continuar...\n")
            

    if opcionInicial == 4:
        print("\n***** VIDEOS *****")
        print("1.- Agregar\n2.- Borrar\n3.- Modificar\n4.- Consultar todo\n5.- Ver detalles")
        opcion4 = int(input("\nElija una opcion: "))

        if opcion4 == 1:
            idVideo = int(input("Ingresa el id para guardar el Video: "))
            nombre = (input("Ingrese el nombre del Video: "))
            url = (input("Ingrese el url del Video: "))
            fechapublicacion = (input("Ingrese la Fecha de Publicación del Video: "))
            v = video(idVideo, nombre, url, fechapublicacion)
            v.agregar()
            print("\nListo!\n")
            input("\nPresiona enter para continuar...\n")

        if opcion4 == 2:
            idVideo =  int(input("Ingrese el id del Video: "))
            nombre = (input("Ingrese el nombre del Video: "))
            url = (input("Ingrese el url del Video: "))
            fechapublicacion = (input("Ingrese la Fecha de Publicación del Video: "))
            v = video(idVideo, nombre, url, fechapublicacion)
            v.borrar()
            print("\nListo!\n")
            input("\nPresiona enter para continuar...\n")

        if opcion4 == 3:
            v = video(None, None, None)
            v.consultar()
            print("\n**Tome los datos de la informacion de arriba**\n")
            idVideo = int(input("Ingrese el id del Video a modificar: "))
            nombre = (input("Ingrese el nombre del video a modificar: "))
            url = (input("Ingrese la url a modificar: "))
            fechapublicacion = (input("Ingrese la Fecha de Publicacion a modificar: "))
            v = video(idVideo, nombre, url, fechapublicacion)
            v.borrar()
            print("------------------------------")
            idVideo = int(input("Ingrese el nuevo id del Video: "))
            nombre = (input("Ingrese el nuevo nombre del Video: "))
            url = (input("Ingrese la nueva url para guardarla: "))
            fechapublicacion = (input("Ingrese la nueva Fecha de Publicacion: "))
            v = video(idVideo, nombre, url, fechapublicacion)
            v.agregar()
            print("\nListo!\n")
            input("\nPresiona enter para continuar...\n")   

        if opcion4 == 4:
            v = video(None, None, None)
            v.consultar()
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
            print("\nListo!\n")
            input("\nPresiona enter para continuar...\n")

        if opcion5 == 2:
            ct = cursoTema(None, None, None)
            ct.consultar()
            print("\n**Tome los datos de la informacion de arriba**\n")
            idCurso = int(input("Ingrese el id del curso: "))
            idTema = int(input("Ingrese el id del tema: "))
            idCursoTema = int(input("Ingrese idCursoTema: "))
            ct = cursoTema(idCursoTema, idCurso, idTema)
            ct.borrar()
            print("\nListo!\n")
            input("\nPresiona enter para continuar...\n")

        if opcion5 == 3:
            ct = cursoTema(None, None, None)
            ct.consultar()
            print("\n**Tome los datos de la informacion de arriba**\n")
            idCurso = int(input("Ingrese el id del curso a modificar: "))
            idTema = int(input("Ingrese el id del tema a modificar: "))
            idCursoTema = int(input("Ingrese idCursoTema a modificar: "))
            ct = cursoTema(idCursoTema, idCurso, idTema)
            ct.borrar()
            print("------------------------------")
            idCurso = int(input("Ingrese el nuevo id del curso: "))
            idTema = int(input("Ingrese el nuevo id del tema: "))
            idCursoTema = int(input("Ingrese el nuevo id para guardarlo: "))
            ct = cursoTema(idCursoTema, idCurso, idTema)
            ct.agregar()
            print("\nListo!\n")
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
            print("\nListo!\n")
            input("\nPresiona enter para continuar...\n")

        if opcion6 == 2: 
            ctv = cursotemavideo(None, None, None)
            ctv.consultar()
            print("\n**Tome los datos de la informacion de arriba**\n")
            idCT = int(input("Ingrese el id del CursoTema: "))
            idV = int(input("Ingrese el id del Video: "))
            idCursoTV = int(input("Ingrese idCursoTemaVideo: "))
            ctv = cursotemavideo(idCursoTV, idCT, idV)
            ctv.borrar()
            print("\nListo!\n")
            input("\nPresiona enter para continuar...\n")

        if opcion6 == 3:
            ctv = cursotemavideo(None, None, None)
            ctv.consultar()
            print("\n**Tome los datos de la informacion de arriba**\n")
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
            print("\nListo!\n")
            input("\nPresiona enter para continuar...\n")

        if opcion6 == 4:
            ctv = cursotemavideo(None, None, None)
            ctv.consultar()
            input("\nPresiona enter para continuar...\n")
    
    if opcionInicial == 7:
        break