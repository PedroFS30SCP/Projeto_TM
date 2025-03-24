import pandas as pd

# Caminhos dos ficheiros
input_file = '../dataset/NCR-lexicon_ORIGIN.csv'
output_file = '../dataset/NCR-lexicon.csv'

def clean_ncr(input_file, output_file):
    # Carregar o ficheiro original com separador correto
    print(f"A carregar o ficheiro: {input_file}")
    df = pd.read_csv(input_file, sep=';')

    # Mostrar as primeiras linhas para verificar estrutura
    print("Estrutura original do ficheiro:")
    print(df.head())

    # Selecionar apenas as colunas que interessam
    df_clean = df[['English', 'Positive', 'Negative']]
    df_clean.columns = ['word', 'positive', 'negative']

    # Guardar o ficheiro tratado
    print(f"A guardar o ficheiro tratado em: {output_file}")
    df_clean.to_csv(output_file, index=False)

    print("Ficheiro tratado com sucesso! Novo ficheiro criado.")

# Executar a função
clean_ncr(input_file, output_file)
