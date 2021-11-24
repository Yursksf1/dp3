
# -*- coding: utf-8 -*-
""""
# Ejercicio 3
Una función para validar usuario y contraseña esta función debe validar
si el usuario corresponde a la contraseña, un usuario puede confundir como
ingreso el email, entonces si ingresa en mayúscula o minúscula se le debe
‘perdonar’ pero la contraseña debes ser exactamente igual
Como lo harias?

Base email: yurs.ksf1@gmai.com  pass: DiplomadoPython123.
V email: yurs.Ksf1@gmai.com  pass: DiplomadoPython123.
X email: yurs.ksf1@gmai.com  pass: diplomadopython123.
X email: yurs.ksf1@gmai.com  pass: DiplomaDopython1234
"""

CORREOS_REGISTRADOS = [
    ['albueno1186@gmail.com', 'albueno1186'],
    ['basp0606@gmail.com', 'basp0606'],
    ['camilonavarro14@gmail.com', 'camilonavarro14'],
    ['cristo_blanco@hotmail.com', 'cristo_blanco'],
    ['santiagogalvis771@gmail.com', 'santiagogalvis771'],
    ['deyvyjava@hotmail.com', 'deyvyjava'],
    ['santarosasur@hotmail.com', 'santarosasur'],
    ['elkinleoardo08@gmail.com', 'elkinleoardo08'],
    ['e.bernal0322@gmail.com', 'bernal0322'],
    ['erika.pita1982@hotmail.com', 'pita1982'],
    ['taverap@gmail.com', 'taverap'],
    ['Fjsr1098@gmail.com', 'Fjsr1098'],
    ['jelirodriguez23@gmail.com', 'jelirodriguez23'],
    ['Calderonnjhonj@gmail.com', 'Calderonnjhonj'],
    ['milton_mote@hotmail.com', 'milton_mote'],
    ['Jdpalomino31@gmail.com', 'Jdpalomino31'],
    ['Juank_fortin10@hotmail.com', 'Juank_fortin10'],
    ['Meyerlafm@gmail.com', 'Meyerlafm'],
    ['jhofrgo@gmail.com', 'jhofrgo'],
]


def validar(email, password):
    for ee in CORREOS_REGISTRADOS:
        validacion_email = ee[0].upper() == email.upper()
        if validacion_email:
            validacion_password = ee[1] == password
            if validacion_password:
                return True

    return False


def run():
    message = """
    Hola! para ingresar debes poner tu email y password 
    """

    while True:
        print(message)
        email = input("ingresa email: ")
        password = input("ingresa password: ")

        if validar(email, password):
            print("te logueaste correctamente")
            break
        else:
            print("te no te pudiste loguear, intenta nuevamente")

    print('fin codigo')

if __name__ == "__main__":
    run()