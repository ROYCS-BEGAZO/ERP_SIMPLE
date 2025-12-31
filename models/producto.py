class Producto:
    def __init__(self, nombre, precio, id):
        self.nombre = nombre
        self._precio = None
        self.id = id
        self.precio = precio
    @property
    def precio(self):
        return self._precio
    
    @precio.setter
    def precio(self, n_precio):
        if not n_precio > 0:
            raise ValueError("el precio no puede ser 0 o menos")
        self._precio = n_precio
