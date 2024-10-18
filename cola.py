#! /C:\Users\Admin\AppData\Local\Microsoft\WindowsApps\python.exe

class cola:

    __data = []
    __maxsize = None
    
    def __init__(self, size = 10):
        self.__maxsize = size

    def __len__(self):
        return len(self.__data)

    def __str__(self) -> str:
        answ = "<"
        answ += f"{len(self)} de {self.__maxsize}, {self.__data}"
        if self.esVacia(): answ += " VACIA"        
        if self.esLlena(): answ += " LLENA"
        answ += ">"
        return answ
    
    def esVacia(self) -> bool:
        return len(self) == 0

    def esLlena(self) -> bool:
        return len(self) == self.__maxsize
        
    def enqueue(self, something):
        if not self.esLlena():
            self.__data.append(something)
        else:
            raise OverflowError(f"Queue: Cola llena")

    def dequeue(self) -> object:
        if len(self) == 0:
            raise ValueError
        else:
            item = self.__data[0]
            self.__data = self.__data[1:]
            return item

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
        
        item = c.dequeue()
        print(item, c)

        item = c.dequeue()
        print(item, c)

        item = c.dequeue()
        print(item, c)

        item = c.dequeue()
        print(item, c)

    except OverflowError:
        print("Número introducido no entró, cola llena")
    except ValueError:
        print("Nada sale, lista vacía")