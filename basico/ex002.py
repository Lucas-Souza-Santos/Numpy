import numpy as np

# a = np.array([2, 3, 4])

# print(a, " ", a.dtype)

# b = np.array([1.2, 3.5, 5.1])

# print(b.dtype)

"""
a = np.array(1, 2, 3, 4)
vai gerar um erro, pois não pode ser passado vários argumentos
"""


c = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(type(c))

#   Matriz complexa     #
d = np.array([[1, 2], [3, 4]], dtype=complex)

print(d)

# funções para criar array com tamanho conhecido  #
# função zero

print("===== Funcao zero =====")
print(np.zeros((3, 4)))

print("===== funcao um =====")
print(np.ones((2, 3, 4), dtype=np.int16))

"""
Função empty cria uma matriz cujo conteúdo inicial é aleatório e 
depende do estado da memória. Por padrão, o dtype da matriz criada 
é float64
"""

print(np.empty((2, 3)))
