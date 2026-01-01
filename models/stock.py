class Stock:
    def __init__(self):
        self.cantidades = {}
    
    def agregar(self, producto, cantidad):
        self.cantidades[producto.id] = self.cantidades.get(producto.id, 0) + cantidad
        print(self.cantidades)
    def hay_stock(self, producto, cantidad):
        return self.cantidades.get(producto.id, 0) >= cantidad
    
    def quitar(self, producto, cantidad):
        if not self.hay_stock(producto, cantidad):
            raise Exception("no hay stock")
        self.cantidades[producto.id] -= cantidad


