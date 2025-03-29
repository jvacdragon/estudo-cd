import numpy as np

arr = np.array([12,2,45,56,6])
print(arr)
print(arr.dtype)

#Criar array com tipo especifico
arr = np.array([12,6,46,36], dtype=np.int64)
print(arr)
print(arr.dtype)

arr = np.array([12,6,46.235,36.5], dtype=np.float32)
print(arr)
print(arr.dtype)

print("Alterando tipo de dado de float para int: ", arr.astype(np.int32))

#os arrays de multiplas dimensões devem ter a mesma dimensao
arr = np.array([[12,2,3], [1,4,5]])
print(arr)

#criando array não inicializado com 3 linhas e duas colunas
#o array apenas não tem seus valores inicializados, nao quer dizer que são vazios. Por isso a alternancia de valores. Ele meio que fica como lixo na memória
arrEmpty = np.empty([3,2], dtype=np.int16)
print(arrEmpty)
print(arr.dtype)

#criando array com valores zerados tendo 2 linhas e 3 colunas
arr = np.zeros((2,3))
print(arr)

#criando array com valores em 1
arr = np.ones((3,2))
print(arr)

#criando array com valores definidos
arr = np.full((2,2), 9)
print(arr)

#matriz com valores na diagonal tendo valor 1
arr = np.eye(5)
print(arr)

#gerando numero aleatório entre 0 e 1. por default ele gera apenas um numero, mas com parametro é possível definir quantos serão gerados
print(np.random.random(6))

#gerando valores de distribuição normal(gausiana) contendo valores negativos
print(np.random.randn(10,2))

#removendo numeros duplicados de um array
arr = np.array([1,32,3,2,5,4,5,5,6,1,1,3])
print(np.unique(arr))
#testando se modifica o array original
print(arr)

#mostrar o formato da matriz
arr = np.full((2,6), 2)
print(arr.shape)

#desvio padrão da matriz(o quanto os valores estão longe da média)
arr = np.array([1,2,3])
print(arr.std())

arr = np.array([[1,2,3], [5,6,4]])
print(arr.std())

#multiplicação de matrizes
arr = np.array([[1,2], [3,4]])
arr2 = np.array([[1,1], [1,1]])
print(arr*arr2)

#transposição de matriz
arr = np.arange(15).reshape((3,5)) #cria um array de 15 elementos indo de 0 até 14 e depois deixa no formato 3 linhas e 5 colunas. Todos os numeros precisam caber no reshape para que não dê erro
print(arr)
#aqui se faz a transposição invertendo linhas e colunas
print(arr.T)

#criando matriz baseado em valores de outra matriz
arr = np.random.randn(10) 
print(arr)
print(np.where(arr > 0, True, False))#se valor de arr for maior que 0, retornar true na nova array, se nao for retorna false