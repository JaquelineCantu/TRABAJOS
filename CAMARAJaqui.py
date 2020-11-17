import cv2 

while 1:
    opcion=1
    print("""
    ¿Que desea hacer? (Escoga la opcion que desea utilizar)
    1)Tomar foto nuevamente
    2)Salir
    """)
    opcion=int(input('¿Que desea hacer?'))

    if opcion == 1:
               
 camara = cv2.VideoCapture(0)

 foto,frame=camara.read()

    if foto == True:
 cv2.imwrite('foto.png',frame)
 print('Se tomo con exito!')

    else:
 print('Error de camara, esta apagada o no esta configurada!!')

 camara.release()

    elif opcion == 2:
        break
    
    else:
        print('No existe esa opcion')
