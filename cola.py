#! /C:\Users\Admin\AppData\Local\Microsoft\WindowsApps\python.exe

class cola:

    __data = []
    __size = None
    
    def __init__(self, size):
        self.__size = size

    def h(self) -> int:
        return len(self.__data)

    def __str__(self) -> str:
        answ = "<"
        answ += f"{self.h()} de {self.__size}, {self.__data}"
        # if self.esVacia(): answ += " VACIA"        
        # if self.esLlena(): answ += " LLENA"
        answ += ">"
        return answ
    
    def esVacia(self) -> bool:
        pass

    def esLlena(self) -> bool:
        return False
        
    def enqueue(self, something):
        if not self.esLlena():
            self.__data.append(something)

    # def dqueue() -> object:
    #     cola = cola[1:]

if __name__ == "__main__":

    c=cola(4)
    print(c)

    c.enqueue(11)
    print(c)

    c.enqueue(22)
    print(c)

    c.enqueue(33)
    print(c)