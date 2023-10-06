class MyException(Exception):
    def __init__(self, message):
        super().__init__(message)

try:
    raise MyException("Wystąpił wyjątek") # - rzucenie wyjatku
except MyException:
    print("Wystąpił wyjatek MyException")

except Exception as e:
    print("Bład", e)