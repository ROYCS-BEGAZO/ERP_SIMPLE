from services.venta_service import VentaService
from models.producto import Producto
from models.cliente import Cliente
p1 = Producto('laptop', 3000, "0001")
p2 = Producto('mouse', 500, "0002")
p3 = Producto('parlante', 100, "0003")
p4 = Producto('monitor', 700, "0004")
p5 = Producto('fuente', 240, "0005")
c1 = Cliente('samuel', "77777")
venta = VentaService()
orden = venta.crear_orden('2344', c1)
venta.agregar_producto(orden, p1, 4)
venta.confirmar(orden)
