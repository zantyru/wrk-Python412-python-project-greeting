class Greeter:
    def __init__(self, greeting_text="Привет, Мир"):
        self.__greeting_text = str(greeting_text)

    def greet(self):
        return self.__greeting_text
