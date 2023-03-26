""" 
Defina uma interface para criar um objeto, mas deixe as subclasses decidirem 
qual classe instanciar. O Factory Method permite que uma classe adie a 
instanciação para subclasses. 
""" 

import  abc 


class Creator ( metaclass = abc . ABCMeta ) : 
    """     Declare o método fábrica, que retorna um objeto do tipo Produto.    
    O criador também pode definir uma implementação padrão do     
    método fábrica que retorna um objeto ConcretoProduto padrão.     
    Chame o método fábrica para criar um objeto Produto.     """
   
    def __init__(self):
        self.product = self._factory_method()

    @abc.abstractmethod
    def _factory_method(self):
        pass

    def some_operation(self):
        self.product.interface()

class ConcreteCreator1(Creator):
    """
    Substituir o método da fábrica para retornar uma instância de um
    ConcreteProduct1.
    """

    def _factory_method(self):
        return ConcreteProduct1()


class ConcreteCreator2(Creator):
    """
   Substituir o método da fábrica para retornar uma instância de um
    ConcreteProduct2.
    """

    def _factory_method(self):
        return ConcreteProduct2()


class Product(metaclass=abc.ABCMeta):
    """
    Defina a interface dos objetos que o método da fábrica cria.
    """

    @abc.abstractmethod
    def interface(self):
        pass


class ConcreteProduct1(Product):
    """
Implementar a interface do produto.    """

    def interface(self):
        pass


class ConcreteProduct2(Product):
    """  
    Implement the Product interface.
    Implementar a interface do produto.
    """
    def interface(self):
        pass
    

def main():
    concrete_creator = ConcreteCreator1()
    concrete_creator.product.interface()
    concrete_creator.some_operation()


if __name__ == "__main__":
    main()        
