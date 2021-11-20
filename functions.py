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

def get_test_data(Data, opt = 0):
    if opt == 1:
        Data = Data[Data["Certamen"] == "C1"]
    elif opt == 2:
        Data = Data[Data["Certamen"] == "C2"]
    Data = Data.sample(frac=1).reset_index(drop=True)
    return Data
    


