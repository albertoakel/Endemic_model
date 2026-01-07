import streamlit as st
import plotly.graph_objects as go
from load_data import carregar_dados
from visualize import plot_casos, plot_ajuste
from fit_model import ajustar_modelo

# Título do app
st.title("Modelagem Epidemiológica - Modelo SIRC")

# Leitura dos dados diretamente no código
df_estado, _ = carregar_dados("/home/akel/PycharmProjects/Endemic_model/data/caso_full.parquet", estado="PA")

# Ajuste do modelo
x, y, result = ajustar_modelo(df_estado)

# Gráficos com Plotly
fig_dados = go.Figure()
fig_dados.add_trace(go.Bar(x=x, y=y, name='Casos acumulados', marker_color='red'))
fig_dados.update_layout(
    title="Casos Acumulados de COVID-19 - Estado do MA",
    xaxis_title="Data",
    yaxis_title="Casos",
    bargap=0.2,
    template="plotly_white"
)

fig_ajuste = go.Figure()
fig_ajuste.add_trace(go.Scatter(x=x, y=y, mode='markers', name='Dados'))
fig_ajuste.add_trace(go.Scatter(x=x, y=result.best_fit, mode='lines', name='Melhor ajuste'))
fig_ajuste.add_trace(go.Scatter(
    x=list(x) + list(x[::-1]),
    y=list(result.best_fit + result.residual.std()) + list((result.best_fit - result.residual.std())[::-1]),
    fill='toself',
    fillcolor='rgba(255,165,0,0.2)',
    line=dict(color='rgba(255,255,255,0)'),
    hoverinfo="skip",
    showlegend=True,
    name='Incerteza'
))
fig_ajuste.update_layout(
    title="Ajuste do Modelo SIRC",
    xaxis_title="Data",
    yaxis_title="Casos acumulados",
    template="plotly_white"
)

# Exibir os gráficos
st.plotly_chart(fig_dados, use_container_width=True)
st.plotly_chart(fig_ajuste, use_container_width=True)

# Exibir o relatório do ajuste
with st.expander("Ver relatório do ajuste"):
    st.text(result.fit_report())