import pandas as pd

def carregar_dados(path, estado='PA', cidade=None):
    df = pd.read_parquet(path)
    df['date'] = pd.to_datetime(df['date'])

    df_estado = df.groupby(['date', 'state'])['new_confirmed'].sum().reset_index()
    df_estado = df_estado[df_estado['state'] == estado]

    if cidade:
        df_cidade = df[(df['city'] == cidade) & (df['state'] == estado)]
        return df_estado, df_cidade

    return df_estado, None
