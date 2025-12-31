class OrdenVenta:
    def __init__(self, id, cliente):
        self.id = id
        self.cliente = cliente
        self.lineas = []
        self.estado = "draft"
    
    def total(self):
        return sum(linea.subtotal() for linea in self.lineas)
