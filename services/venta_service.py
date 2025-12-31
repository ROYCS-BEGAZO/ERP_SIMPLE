from models.orden_venta import OrdenVenta
from models.linea_venta import LineaVenta
class VentaService:
    
    def crear_orden(self,id, cliente):
        return OrdenVenta(id, cliente)
    
    def agregar_producto(self, orden, producto, cantidad):
        if orden.estado != "draft":
            raise Exception("no se puede modificar la orden")
        orden.lineas.append(LineaVenta(producto, cantidad))
    
    def confirmar(self, orden):
        if not orden.lineas:
            raise Exception("orden vacia")
        orden.estado = "confirmado"
