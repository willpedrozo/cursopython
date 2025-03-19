import sqlite3 as meu_bd

# conectar ao banco de dados ou criar um novo caso não exista
def conectar_banco():
    conexao = meu_bd.connect("meu_banco.db") #nome do banco
    return conexao

# criar a tabela
def criar_tabela():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            idade INTEGER    
        )
    ''')
    conexao.commit()
    conexao.close()

# inserir dados na tabela que foi gerada
def inserir_usuario(lala_nome, lala_idade):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('''
        INSERT INTO usuarios (nome, idade) VALUES (?, ?)
    ''', (lala_nome, lala_idade))
    conexao.commit()
    conexao.close()

#ler dados do banco de dados
def listar_usuarios():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('''
        SELECT * FROM usuarios
    ''')
    usuarios = cursor.fetchall()
    for usuario in usuarios:
        print(usuario)
    conexao.close()


# atualizar dados
def atualizar_dados(id, novo_nome, nova_idade):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('''
        UPDATE usuarios 
        SET nome = ?,
            idade = ?
        WHERE id = ?    
    ''', (novo_nome, nova_idade, id))
    conexao.commit()
    conexao.close()

#excluir dados
def excluir_usuario(id):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('DELETE FROM usuarios WHERE id = ?', (id,))
    conexao.commit()
    conexao.close()

#questão de continuar
def deseja_continuar():
    executar = True
    while executar:
        pergunta ='''
        [1] Desejo alterar mais um nome
        [2] Desejo sair
    '''
        print(f'{pergunta}')
        escolha = input(f'Qual sua opção? ')
        if escolha == '2':
            print("Obrigado")
            executar = False

        



#criando a tabela, executar apenas uma vez
#criar_tabela()

#inserir alguns usuarios
#inserir_usuario('Caio','55')
#inserir_usuario('Neemias','30')
#inserir_usuario('Carlos','20')

# editar usuario
#atualizar_dados(1, 'cah', '66')

# excluir uma linha
#excluir_usuario(4)

#listar todos os usuarios
#listar_usuarios()

#novo nome do usuario e nova idade
# nome_atualizado = input(f'Qual será o novo nome? ')
# idade_atualizada = int(input(f'Qual será a nova idade? ')) 
# atualizar_dados(2, nome_atualizado, idade_atualizada)

# listar_usuarios()

# deseja_continuar()

def perguntar_e_inserir():
    while True:
        try:
            nome = input(f'Qual será o novo nome? ')
            idade = int(input(f'Qual será a nova idade? '))
            inserir_usuario(nome, idade)
            listar_usuarios()
            continuar = input(f'Deseja continuar? \n (S/N):').lower()
            if continuar != "s":
                break
        except ValueError:
            print(f'Erro: a idade deve ser um número inteiro')
        except Exception as deu_ruim:
            print(f'ocorreu um erro: {deu_ruim}')
            

perguntar_e_inserir()



