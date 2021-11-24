
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
    ['albueno1186@gmail.com', 'albueno1186', 0],
    ['basp0606@gmail.com', 'basp0606', 0],
    ['camilonavarro14@gmail.com', 'camilonavarro14', 0],
    ['cristo_blanco@hotmail.com', 'cristo_blanco', 0],
    ['santiagogalvis771@gmail.com', 'santiagogalvis771', 0],
    ['deyvyjava@hotmail.com', 'deyvyjava', 0],
    ['santarosasur@hotmail.com', 'santarosasur', 0],
    ['elkinleoardo08@gmail.com', 'elkinleoardo08', 0],
    ['e.bernal0322@gmail.com', 'bernal0322', 0],
    ['erika.pita1982@hotmail.com', 'pita1982', 0],
    ['taverap@gmail.com', 'taverap', 0],
    ['Fjsr1098@gmail.com', 'Fjsr1098', 0],
    ['jelirodriguez23@gmail.com', 'jelirodriguez23', 0],
    ['Calderonnjhonj@gmail.com', 'Calderonnjhonj', 0],
    ['milton_mote@hotmail.com', 'milton_mote', 0],
    ['Jdpalomino31@gmail.com', 'Jdpalomino31', 0],
    ['Juank_fortin10@hotmail.com', 'Juank_fortin10', 0],
    ['Meyerlafm@gmail.com', 'Meyerlafm', 0],
    ['jhofrgo@gmail.com', 'jhofrgo', 0],
]


def validar(email, password):
    for ee in CORREOS_REGISTRADOS:
        validacion_email = ee[0].upper() == email.upper()
        if validacion_email:
            if ee[2] >= 3:
                print('contrasena bloqueada. contacta con el admin')
                return False
            validacion_password = ee[1] == password
            if validacion_password:
                ee[2] = 0
                return True
            else:
                ee[2] = ee[2] + 1

    return False

def validar_email(email):
    return '@' in email

def run():
    message = """
    Hola! para ingresar debes poner tu email y password 
    """

    while True:
        print(message)
        email = input("ingresa email: ")
        if validar_email(email):
            password = input("ingresa password: ")
            if validar(email, password):
                print("te logueaste correctamente")
            else:
                print("te no te pudiste loguear, intenta nuevamente")
        else:
            print("email no valido, debe tener un @")

    print('fin codigo')

if __name__ == "__main__":
    run()