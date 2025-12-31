class LineaVenta:
    def __init__(self, producto, cantidad:int):
        self.producto = producto
        self.cantidad = cantidad
    
    def subtotal(self):
        return self.cantidad * self.producto.precio


