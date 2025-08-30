import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image, PageBreak
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

st.set_page_config(page_title="Gerenciador Financeiro", layout="centered")

# ----------------------------
# Função para gerar PDF
# ----------------------------
def gerar_pdf(nome, salario, valor_invest, perc_invest, total_despesas, saldo, data_atual, df):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    elements = []

    styles = getSampleStyleSheet()

    # Título
    title = Paragraph(f"<b><font size=16>📊 Relatório Financeiro</font></b>", styles['Title'])
    subtitle = Paragraph(f"<font size=12>👋 Olá {nome}, sua despesa em {data_atual} é:</font>", styles['Normal'])
    
    elements.append(title)
    elements.append(Spacer(1, 12))
    elements.append(subtitle)
    elements.append(Spacer(1, 20))

    # Resumo
    resumo = [
        f"💵 Salário: R$ {salario:,.2f}",
        f"📈 Investimento ({perc_invest}%): R$ {valor_invest:,.2f}" if valor_invest > 0 else "",
        f"💸 Total de Despesas: R$ {total_despesas:,.2f}",
        f"✅ Saldo Final: R$ {saldo:,.2f}"
    ]
    for r in resumo:
        if r:  # não imprimir vazio
            elements.append(Paragraph(r, styles['Normal']))
            elements.append(Spacer(1, 6))

    elements.append(Spacer(1, 20))

    # ----- TABELA -----
    data = [df.columns.tolist()] + df.values.tolist()
    table = Table(data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#4F81BD")),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0,0), (-1,0), 10),
        ('BACKGROUND', (0,1), (-1,-1), colors.whitesmoke),
        ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
    ]))
    elements.append(table)
    elements.append(Spacer(1, 20))

    # ----- GRÁFICO DE BARRAS -----
    fig, ax = plt.subplots(figsize=(5,3))
    df.groupby("Categoria")["Valor"].sum().plot(kind="bar", ax=ax, color="#4F81BD")
    ax.set_title("Despesas por Categoria")
    ax.set_ylabel("R$")
    img_buf = BytesIO()
    plt.savefig(img_buf, format="png", bbox_inches="tight")
    img_buf.seek(0)
    elements.append(PageBreak())
    elements.append(Paragraph("<b>📊 Gráfico de Barras</b>", styles['Heading2']))
    elements.append(Spacer(1, 12))
    elements.append(Image(img_buf, width=400, height=250))

    # ----- GRÁFICO DE PIZZA -----
    fig, ax = plt.subplots(figsize=(5,3))
    df.groupby("Categoria")["Valor"].sum().plot(kind="pie", ax=ax, autopct="%1.1f%%", startangle=90, cmap="tab20")
    ax.set_ylabel("")
    ax.set_title("Distribuição de Despesas (%)")
    img_buf2 = BytesIO()
    plt.savefig(img_buf2, format="png", bbox_inches="tight")
    img_buf2.seek(0)
    elements.append(PageBreak())
    elements.append(Paragraph("<b>🥧 Gráfico de Pizza</b>", styles['Heading2']))
    elements.append(Spacer(1, 12))
    elements.append(Image(img_buf2, width=400, height=250))

    doc.build(elements)
    pdf = buffer.getvalue()
    buffer.close()
    return pdf

# ----------------------------
# Início da aplicação
# ----------------------------
st.title("💰 Gerenciador de Despesas e Investimentos")

# Nome da pessoa
nome = st.text_input("Digite seu nome:")

# Entrada: salário
salario = st.number_input("Informe seu salário mensal (R$):", min_value=0.0, step=100.0)

if nome and salario > 0:
    investir = st.radio("Deseja investir uma porcentagem do salário?", ["Não", "Sim"])
    perc_invest, valor_invest = 0, 0

    if investir == "Sim":
        perc_invest = st.slider("Informe a % para investimento:", 0, 100, 10)
        valor_invest = salario * (perc_invest / 100)

    # Despesas
    st.subheader("📌 Informe suas despesas")
    despesas = {}
    categorias = ["Aluguel", "Alimentação", "Transporte", "Lazer", "Outros"]
    for cat in categorias:
        despesas[cat] = st.number_input(f"{cat} (R$):", min_value=0.0, step=50.0)

    df_despesas = pd.DataFrame(list(despesas.items()), columns=["Categoria", "Valor"])
    total_despesas = df_despesas["Valor"].sum()
    saldo = salario - total_despesas - valor_invest
    data_atual = datetime.now().strftime("%d/%m/%Y")

    # Resumo
    st.subheader("📊 Resumo Financeiro")
    st.write(f"👋 Olá **{nome}**, sua despesa em **{data_atual}** é:")
    st.write(f"💵 Salário: R$ {salario:,.2f}")
    if investir == "Sim":
        st.write(f"📈 Investimento ({perc_invest}%): R$ {valor_invest:,.2f}")
    st.write(f"💸 Total de Despesas: R$ {total_despesas:,.2f}")
    st.write(f"✅ Saldo Final: R$ {saldo:,.2f}")

    # Gráficos na interface
    st.subheader("📊 Gráficos de Despesas")
    fig_bar, ax_bar = plt.subplots()
    ax_bar.bar(df_despesas["Categoria"], df_despesas["Valor"], color="skyblue")
    ax_bar.set_title("Despesas por Categoria")
    st.pyplot(fig_bar)

    fig_pie, ax_pie = plt.subplots()
    ax_pie.pie(df_despesas["Valor"], labels=df_despesas["Categoria"], autopct="%1.1f%%", startangle=90)
    ax_pie.set_title("Distribuição das Despesas")
    st.pyplot(fig_pie)

    # Botão para baixar PDF
    pdf = gerar_pdf(nome, salario, valor_invest, perc_invest, total_despesas, saldo, data_atual, df_despesas)
    st.download_button("📥 Baixar relatório em PDF", data=pdf, file_name=f"relatorio_{nome}.pdf", mime="application/pdf")
