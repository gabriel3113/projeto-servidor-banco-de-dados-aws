import io
import psycopg2
import pandas as pd

# Carregar o arquivo CSV
usuarios = pd.read_csv(r'arquivo_csv\usuarios_exemplo.csv')

# Exibir o DataFrame resultante
print(usuarios)

# Função para carregar dados no PostgreSQL
def carregar_dados(conn, df, tabela, colunas):
    cur = conn.cursor()
    output = io.StringIO()
    # Incluir apenas as colunas especificadas
    df.to_csv(output, sep='\t', header=False, index=False, columns=colunas)
    output.seek(0)
    try:
        cur.copy_from(output, tabela, null="", columns=colunas)
        conn.commit()
        print(f"Dados carregados com sucesso na tabela {tabela}.")
    except Exception as e:
        print(f"Erro ao carregar dados: {e}")
        conn.rollback()
    finally:
        cur.close()

# Conexão com o banco de dados
conn = psycopg2.connect(
    host='localhost',
    port='5432',
    database='postgres',
    user='admin',
    password='admin'
)

# Definir as colunas para a inserção, excluindo 'id' pois ele é autoincremento
colunas = ['nome', 'email', 'data_criacao']

# Carregar os dados na tabela 'usuarios'
carregar_dados(conn, usuarios, 'usuarios', colunas)

# Fechar a conexão
conn.close()
