import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('database/base_padronizada.csv')

def plot_approval_distribution(df):
    approval_counts = df['aprovado'].value_counts()
    labels = [f"{label} ({count})" for label, count in zip(approval_counts.index, approval_counts.values)]
    approval_counts.plot(kind='pie', labels=labels, autopct='%1.1f%%', startangle=30, colors=['crimson', 'dodgerblue'])

    plt.title('Distribuição de Aprovação')
    plt.ylabel('')  # Remove o rótulo do eixo y
    plt.show()

def plot_sex_distribution(df):
    df['sexo'].value_counts().plot(kind='bar', color=['mediumseagreen', 'gold'])

    plt.title('Distribuição de Sexo')
    plt.xlabel('Sexo')
    plt.ylabel('Contagem')
    plt.xticks(rotation=0)
    plt.show()

def plot_best_means_ranking(df):
    top_means = df.nlargest(5, 'media')[['nome', 'media']]
    ax = top_means.set_index('nome')['media'].sort_values(ascending=True).plot(kind='barh', color='orangered')

    for i, value in enumerate(top_means['media'].sort_values(ascending=True)):
        ax.text(value + 0.02, i, f"{value:.2f}", va='center')

    plt.title('Top 5 Melhores Médias')
    plt.xlabel('Média')
    plt.ylabel('Nome do Aluno')
    plt.xlim(7, 9)
    plt.subplots_adjust(left=0.3)
    plt.show()

def plot_most_frequencies_ranking(df):
    top_frequencies = df.nlargest(5, 'frequencia')[['nome', 'frequencia']]
    ax = top_frequencies.set_index('nome')['frequencia'].sort_values(ascending=True).plot(kind='barh', color='yellowgreen')

    for i, value in enumerate(top_frequencies['frequencia'].sort_values(ascending=True)):
        ax.text(value + 0.1, i, f"{value:.1f}", va='center')

    plt.title('Top 5 Melhores Frequências')
    plt.xlabel('Frequência (%)')
    plt.ylabel('Aluno')
    plt.xlim(95, 100)
    plt.subplots_adjust(left=0.3)
    plt.show()

plot_approval_distribution(df)
plot_sex_distribution(df)
plot_best_means_ranking(df)
plot_most_frequencies_ranking(df)