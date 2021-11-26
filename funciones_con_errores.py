from api_exceptions import (
    InputError
)

while True:
    try:
        a = int(input('iingresa un valor numerico'))
    except Exception as e:
        raise InputError('', 'error ingresando un valor numerico')
