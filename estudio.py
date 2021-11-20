import functions as fnc

print("--------------------------------------------------------------------------------------------------------------------------")
print("\nBienvenido a la herramienta de estudio para IA de Raimundo Gross")
print("\nEsta herramienta fue creada con la finalidad de ayudar al estudio con los temas de Inteligencia Artificial")
print("Sugerencias o comentarios dirigir a raimundo.gross.labbe@gmail.com\n")

data = fnc.load_data("contenido.csv")

flag1 = True
while flag1:
    print("Menu Principal\n1.- Preguntas certamen 1\n2.- Preguntas certamen 2\n3.- Preguntas de ambos certamenes\n4.- Configuraciones\n5.- Salir")
    op1 = fnc.get_op(5)
    if op1 == 5:
        print("\nHasta la proxima.\n")
        flag1 = False
    elif op1 == 1:
        #certamen1
        fnc.get_test_data(data, opt=1)
        pass
    elif op1 == 2:
        #certamen2
        fnc.get_test_data(data, opt=2)
        pass
    elif op1 == 3:
        #ambos certamenes
        fnc.get_test_data(data)
    else:
        #config
        pass
    
