# def mi_decorador(f):
#     def funcion_de_decorador():
#         print('esto se ejecuto primiero')
#         return f()
#     return funcion_de_decorador
#
# @mi_decorador
# def di_hola():
#     return "hola"
#
# @mi_decorador
# def despidete():
#     return "chao"
#
# print(di_hola())
# print(despidete())


import time

def mide_tiempo(funcion):
    def funcion_medida(*args, **kwargs):
        inicio = time.time()
        c = funcion(*args, **kwargs)
        print(time.time() - inicio)
        return c
    return funcion_medida

@mide_tiempo
def calcula_pares(n):
    return [i for i in range(n) if i%2 == 0]

print(len(calcula_pares(10000000)))

print('este es el tiempo que demoro')