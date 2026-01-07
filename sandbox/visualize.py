import matplotlib.pyplot as plt
import pandas as pd

def plot_casos(x, y, titulo, caminho=None):
    plt.figure(figsize=(12, 6))
    plt.bar(x, y, color='red', label='Dados originais')
    plt.title(titulo)
    plt.xlabel('Data')
    plt.tight_layout()
    plt.ylim([0, max(y)*1.1])
    plt.xlim(pd.to_datetime([x[0], x[-1]]))

    # plt.ylim([0, 300000])
    # plt.xlim(pd.to_datetime(['2020-03-18', '2020-07-30']))
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.xticks(rotation=45)
    if caminho:
        plt.savefig(caminho)
    plt.show()

def plot_ajuste(x, y, ajuste, std=None):
    plt.figure(figsize=(12, 6))
    plt.plot(x, y, 'o', label='Dados')
    plt.plot(x, ajuste, label='Melhor ajuste')
    if std is not None:
        plt.fill_between(x, ajuste - std, ajuste + std, color='orange', alpha=0.2, label='Incerteza')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
