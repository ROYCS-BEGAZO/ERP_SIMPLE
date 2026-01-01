from services.venta_service import VentaService
from services.stock_service import StockService
from models.producto import Producto
from models.cliente import Cliente
from models.stock import Stock


p1 = Producto('laptop', 3000, "0001")
p2 = Producto('mouse', 500, "0002")
p3 = Producto('parlante', 100, "0003")
p4 = Producto('monitor', 700, "0004")
p5 = Producto('fuente', 240, "0005")
c1 = Cliente('samuel', "77777")
stoc = Stock()
stock_service = StockService(stock=stoc)
venta = VentaService()
stoc.agregar(p1, 10)
stoc.agregar(p2, 4)
stoc.agregar(p3, 6)
stoc.agregar(p4, 7)
stoc.agregar(p5, 2)
orden = venta.crear_orden('2344', c1)
venta.agregar_producto(orden, p1, 4)
print(stoc.cantidades)
venta.confirmar(orden, stock_service)
print(stoc.cantidades)
print(orden.total())
