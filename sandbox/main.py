from load_data import carregar_dados
from visualize import plot_casos, plot_ajuste
from fit_model import ajustar_modelo
import numpy as np
import pandas as pd

def main():
    # Leitura e seleção
    df_estado, _ = carregar_dados("/home/akel/PycharmProjects/Endemic_model/data/caso_full.parquet", estado="MA")
    y = np.cumsum(df_estado['new_confirmed'].values[:180])
    x = df_estado['date'].values[:180]
    print("y (entrada para initial_SIRC):", y)
    print("Tipo:", y.dtype)
    # Visualização dos dados acumulados
    #plot_casos(x, y, 'Casos acumulados COVID-19 - PA (início da pandemia)')
    #
    # # Ajuste do modelo
    result, t = ajustar_modelo(y)
    # print(result.fit_report())
    #
    # # Visualização do ajuste
    # plot_ajuste(x, y, result.best_fit, result.residual.std())

if __name__ == '__main__':
    main()
