ids = []
configuraciones = []
categorias = []
valores = []
estados = []
fechas = []
usuarios = []
descripciones = []
observaciones = []
#-----------------------------------------------#
#--|menu_principal_asistente_de_configuración|--#
#-----------------------------------------------#
while True:
    print("menu principal asistente de configuración")
    print("1) registrar configuración")
    print("2) editar configuración")
    print("3) eliminar configuración")
    print("4) buscar configuración")
    print("5) lista de datos")
    print("6) salir")
    opcion = input("seleccione una opción: ")
    #-----------------------------#
    #--|registrar_configuracion|--#
    #-----------------------------#
    if opcion == "1":
        if len(ids) == 0:
            id_configuracion = 1
        else:
            id_configuracion = ids[-1] + 1
        configuracion = input("nombre de la configuración: ")
        categoria = input("categoría: ")
        valor = input("valor: ")
        estado = input("estado (activa o inactiva): ")
        fecha = input("fecha de creación: ")
        usuario = input("usuario responsable: ")
        descripcion = input("descripción: ")
        observacion = input("observación: ")
        ids.append(id_configuracion)
        configuraciones.append(configuracion)
        categorias.append(categoria)
        valores.append(valor)
        estados.append(estado)
        fechas.append(fecha)
        usuarios.append(usuario)
        descripciones.append(descripcion)
        observaciones.append(observacion)
        print("configuración registrada correctamente.")
        print("id:", id_configuracion)
    #--------------------------#
    #--|editar_configuracion|--#
    #--------------------------#
    elif opcion == "2":
        if len(ids) == 0:
            print("no existen configuraciones registradas.")
        else:
            print("editar configuración")
            for i in range(len(ids)):
                print(f"{ids[i]} | {configuraciones[i]} | {estados[i]}")
            id_buscar = int(input("ingrese la id de la configuración: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos actuales")
                print("id:", ids[posicion])
                print("configuración:", configuraciones[posicion])
                configuraciones[posicion] = input("nuevo nombre: ")
                categorias[posicion] = input("nueva categoría: ")
                valores[posicion] = input("nuevo valor: ")
                estados[posicion] = input("nuevo estado: ")
                fechas[posicion] = input("nueva fecha: ")
                usuarios[posicion] = input("nuevo usuario responsable: ")
                descripciones[posicion] = input("nueva descripción: ")
                observaciones[posicion] = input("nueva observación: ")
                print("configuración actualizada correctamente.")
            else:
                print("id no encontrada.")
    #----------------------------#
    #--|eliminar_configuracion|--#
    #----------------------------#
    elif opcion == "3":
        if len(ids) == 0:
            print("no existen configuraciones registradas.")
        else:
            print("eliminar configuración")
            for i in range(len(ids)):
                print(f"{ids[i]} | {configuraciones[i]}")
            id_buscar = int(input("ingrese la id de la configuración: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("id:", ids[posicion])
                print("configuración:", configuraciones[posicion])
                respuesta = input("¿desea eliminar esta configuración? (s/n): ")
                if respuesta.upper() == "S":
                    ids.pop(posicion)
                    configuraciones.pop(posicion)
                    categorias.pop(posicion)
                    valores.pop(posicion)
                    estados.pop(posicion)
                    fechas.pop(posicion)
                    usuarios.pop(posicion)
                    descripciones.pop(posicion)
                    observaciones.pop(posicion)
                    print("configuración eliminada correctamente.")
                else:
                    print("la configuración no fue eliminada.")
            else:
                print("id no encontrada.")
    #--------------------------#
    #--|buscar_configuracion|--#
    #--------------------------#
    elif opcion == "4":
        if len(ids) == 0:
            print("no existen configuraciones registradas.")
        else:
            print("buscar configuración")
            id_buscar = int(input("ingrese la id de la configuración: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("id:", ids[posicion])
                print("configuración:", configuraciones[posicion])
                print("categoría:", categorias[posicion])
                print("valor:", valores[posicion])
                print("estado:", estados[posicion])
                print("fecha:", fechas[posicion])
                print("usuario:", usuarios[posicion])
                print("descripción:", descripciones[posicion])
                print("observación:", observaciones[posicion])
            else:
                print("id no encontrada.")
    #--------------------#
    #--|lista_de_datos|--#
    #--------------------#
    elif opcion == "5":
        if len(ids) == 0:
            print("no existen configuraciones registradas.")
        else:
            activas = 0
            inactivas = 0
            apariencia = 0
            idioma = 0
            audio = 0
            print("lista de datos")
            for i in range(len(ids)):
                print(f"{ids[i]} | {configuraciones[i]} | {categorias[i]} | {estados[i]}")
                if estados[i].lower() == "activa":
                    activas += 1
                elif estados[i].lower() == "inactiva":
                    inactivas += 1
                if categorias[i].lower() == "apariencia":
                    apariencia += 1
                elif categorias[i].lower() == "idioma":
                    idioma += 1
                elif categorias[i].lower() == "audio":
                    audio += 1
            print("estadísticas asistente de configuración")
            print("cantidad de configuraciones:", len(ids))
            print("activas:", activas)
            print("inactivas:", inactivas)
            print("apariencia:", apariencia)
            print("idioma:", idioma)
            print("audio:", audio)
            nombre = input("ingrese el nombre de la configuración a aplicar: ")
            encontrado = False
            for i in range(len(configuraciones)):
                if configuraciones[i].lower() == nombre.lower():
                    encontrado = True
                    if estados[i].lower() == "activa":
                        print("configuración aplicada correctamente.")
                        print("configuración:", configuraciones[i])
                        print("valor:", valores[i])
                    else:
                        print("la configuración está deshabilitada.")
                    break
            if encontrado == False:
                print("configuración no encontrada.")
    #------------------------------#
    #--|salir_del_menu_principal|--#
    #------------------------------#
    elif opcion == "6":
        print("gracias por utilizar el asistente de configuración.")
        break
    else:
        print("opción no válida.")