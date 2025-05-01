import pandas as pd

def load_data():
    df = pd.read_csv('database/base_despadronizada.csv')

    df['sexo'] = df['sexo'].map({
        'F': 'Feminino', 
        'M': 'Masculino',
        'fem': 'Feminino',
        'masc': 'Masculino',
        'Feminino': 'Feminino',
        'Masculino': 'Masculino',
    })

    df['nota_matematica'] = df['nota_matematica'].map(lambda x: str(x).replace('.', ','))
    df['nota_portugues'] = df['nota_portugues'].map(lambda x: str(x).replace('.', ','))

    df['media'] = round((
        df['nota_matematica'].apply(lambda x: float(x.replace(',', '.'))) + 
        df['nota_portugues'].apply(lambda x: float(x.replace(',', '.'))) + 
        df['frequencia']/10) / 3, 
        2) # 2 casas decimais

    df['aprovado'] = df['media'].apply(lambda x: 'Sim' if x >= 7 else 'Não')

    return df

df = load_data()
df.to_csv('database/base_padronizada.csv', index=False)

print(df)