# função para carregar os data.frames
def files(year): # format YY
    import glob 
    import pandas as pd
    all_files = glob.glob("ano_" + str(year) + "_*.csv")
    df = pd.concat((pd.read_csv(f, encoding='ISO-8859-1', on_bad_lines='skip', sep = ';', decimal = ",") for f in all_files))
    df = df[(df['Tipo Viagem'] == 11)] # eliminando viagens para garagens 
    return(df) 
    

def pas(df):
    import pandas as pd
    df['Data Coleta'] = pd.to_datetime(df['Data Coleta'], format='%d/%m/%Y')
    diario = df.groupby('Data Coleta')['Passageiros'].agg('sum')
    diario = diario.reset_index()
    diario['Data Coleta'] = pd.to_datetime(diario['Data Coleta'])
    diario['dia_semana'] = diario['Data Coleta'].dt.dayofweek
    #print(len(diario))
    return(diario)