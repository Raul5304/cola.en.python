#! /C:\Users\Admin\AppData\Local\Microsoft\WindowsApps\python.exe

class cola:

    __data = []
    __maxsize = None
    
    def __init__(self, size):
        self.__maxsize = size

    def len(self) -> int:
        return len(self.__data)

    def __str__(self) -> str:
        answ = "<"
        answ += f"{self.len()} de {self.__maxsize}, {self.__data}"
        if self.esVacia(): answ += " VACIA"        
        if self.esLlena(): answ += " LLENA"
        answ += ">"
        return answ
    
    def esVacia(self) -> bool:
        return len(self.__data) == 0

    def esLlena(self) -> bool:
        return len(self.__data) == self.__maxsize
        
    def enqueue(self, something):
        if not self.esLlena():
            self.__data.append(something)
        else:
            raise OverflowError(f"Queue: Cola llena")

    # def dqueue() -> object:
    #     cola = cola[1:]

if __name__ == "__main__":

    c=cola(4)
    print(c)

    try:
        c.enqueue(11)
        print(c)

        c.enqueue(22)
        print(c)

        c.enqueue(33)
        print(c)

        c.enqueue(44)
        print(c)

        c.enqueue(55)
        print(c)
    except OverflowError:
        print("Número introducido no entró, cola llena")