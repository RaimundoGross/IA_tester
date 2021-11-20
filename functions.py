import pandas as pd

def get_op(max):
    flag = True
    while flag:
        try:
            op=int(input("> "))
            if op > max:
                raise ValueError
        except ValueError:
            print("Por favor ingrese una de las opciones señaladas\n")
        else:
            flag=False
    return op

def load_data(file):
    data = pd.read_csv(file, sep=";")
    return data

def get_test_data(Data, opt):
    if opt == 1:
        Data = Data[Data["Certamen"] == "C1"]
    elif opt == 2:
        Data = Data[Data["Certamen"] == "C2"]
    Data = Data.sample(frac=1).reset_index(drop=True)
    return Data

def get_op_q(tabu):
    flag = True
    while flag:
        try:
            op=input("> ")
            if op not in "arsvARSV" and len(op) == 1:
                raise ValueError("Por favor ingrese una de las opciones señaladas\n")
            elif tabu == "a" and op in "aA":
                raise ValueError("No hay pregunta anterior")
            elif tabu == "s" and op in "sS":
                raise ValueError("No hay pregunta siguiente")
        except ValueError as ve:
            print(ve)
        else:
            flag=False
    return op.lower()

def question_menu(i, nrows, data_line):
    print(data_line)
    template_q = "\nPregunta {num}: {tipo}\n{pregunta}"
    template_a = "Respuesta: {respuesta}"
    if data_line.at[0, "Tipo"] == "D":
            tipo = "Desarrollo"
    elif data_line.at[0, "Tipo"] == "VF":
        tipo = "Verdero y falso"
    print(template_q.format(num=i+1, tipo=tipo, pregunta=data_line.at[0,"Pregunta"]))
    flag=True
    while flag:
        print("\nR - Ver respuesta\nA - Pregunta anterior\nS - Siguiente pregunta\nV - Volver al menu principal")
        if i == 0:
            op = get_op_q("a")
        elif i == nrows - 1:
            op = get_op_q("s")
        else:
            op = get_op("")
        
        if op == "r":
            print(template_a.format(respuesta=data_line.at[0,"Respuesta"]))
        elif op == "a":
            return -1
        elif op == "s":
            return 1
        else:
            return 0

def test(Data, opt):
    data_test = get_test_data(Data, opt)
    nrows = data_test.shape[0]
    i = 0
    while i  < nrows:
        pass

data = load_data("contenido.csv")
print(data)
ret = question_menu(0, 13, data.iloc[[0]])
print(ret)