import pandas as pd

def get_op(max):
    """
    get_op(max)

    Recieves an option for the main menu. If the number is higher than max then prints a message and asks again

    Inputs:
    - max:  (int)   maximum number of optins in the menu

    Returns:
    - op:   (int)   chosen option

    """
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
    """
    load_data(file)

    Reads a csv file with the test information to a pandas Dataframe

    Inputs:
    - file:         (string)            name of the csv file with the test information

    Returns:
    - data: (pandas Dataframe)  dataframe with the test information
    """
    data = pd.read_csv(file, sep=";")
    return data

def get_test_data(Data, opt):
    """
    get_test_data(Data, opt)

    Separates the data depending on the test

    Inputs:
    - Data: (pandas Dataframe)  dataframe with the test information
    - opt:  (int)               option integer to identify the test

    Returns:
    - Data_sample:  (pandas Dataframe)  dataframe with the selected test information shuffled  
    """
    if opt == 1:
        Data = Data[Data["Certamen"] == "C1"]
    elif opt == 2:
        Data = Data[Data["Certamen"] == "C2"]
    Data_sample = Data.sample(frac=1).reset_index(drop=True)
    return Data_sample

def get_op_q(tabu):
    """
    get_op_q(tabu)

    Recieves an option for the test menu. If the option is in the tabu string then wont be accepted.

    Inputs:
    - tabu: (string)    string containing the forbidden options

    Returns:
    - op:   (string)    string with the selected option

    """
    flag = True
    while flag:
        try:
            op=input("> ")
            if op not in "arsvARSV" or len(op) != 1:
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

def question_menu(i, data):
    """
    question_menu(i, nrows, data_line)

    Runs the menu for one question

    Inputs:
    - i    (int)                index in the dataframe of the current question
    - data (pandas dataframe)   dataframe with the test information

    Returns:
    - move  (int)               next move in the test, 1 for next cuestion, -1 for previous question and 0 to return to main menu

    """
    nrows = data.shape[0]
    template_q = "\nPregunta {num}: {tipo} - {certamen}\n{pregunta}"
    template_a = "Respuesta: {respuesta}"
    if data.at[i, "Tipo"] == "D":
            tipo = "Desarrollo"
    elif data.at[i, "Tipo"] == "VF":
        tipo = "Verdero y falso"
    print(template_q.format(num=i+1, tipo=tipo, certamen= data.at[i, "Certamen"], pregunta=data.at[i,"Pregunta"]))
    flag=True
    while flag:
        print("\nR - Ver respuesta\nA - Pregunta anterior\nS - Siguiente pregunta\nV - Volver al menu principal")
        if i == 0:
            op = get_op_q("a")
        elif i == nrows-1:
            op = get_op_q("s")
        else:
            op = get_op_q("")
        
        if op == "r":
            print(template_a.format(respuesta=data.at[i,"Respuesta"]))
        elif op == "a":
            move = -1
            return move
        elif op == "s":
            move = 1
            return move
        else:
            move = 0
            return move

def test(Data, opt):
    """
    test(Data, opt)

    Runs the selected test

    Inputs:
    - Data  (pandas Dataframe)  dataframe with the test information
    - opt   (int)               number with test option

    Returns:
    None
    """
    data_test = get_test_data(Data, opt)
    nrows = data_test.shape[0]
    if opt == 1:
        print("Preguntas certamen 1")
    elif opt == 2:
        print("Preguntas certamen 2")
    else:
        print("Preguntas Mixtas")
    i = 0
    while i  < nrows:
        op = question_menu(i, data_test)
        if op == 0:
            break
        else:
            i += op
    if op != 0:
        print("Fin del Set de Preguntas")


data = load_data("contenido.csv")
#print(data)
#print(get_test_data(data, 1))
#ret = question_menu(0, 13, data.iloc[[0]])
