
class StockService:
    def __init__(self, stock):
        self.stock = stock
    
    def reservar_para_orden(self, orden):
        for linea in orden.lineas:
            if not self.stock.hay_stock(linea.producto, linea.cantidad):
                raise Exception(f"no hay stock del producto{linea.producto}")
        for linea in orden.lineas:
            self.stock.quitar(linea.producto, linea.cantidad)
    def cancelar_orden(self, orden):
        for linea in orden.lineas:
            self.stock.agregar(linea.producto, linea.cantidad)