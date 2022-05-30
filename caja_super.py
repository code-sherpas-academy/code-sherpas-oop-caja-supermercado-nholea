class Producto():
    def __init__(self,codigo_barras, cantidad):
        self.codigo_barras = codigo_barras
        self.cantidad = cantidad

    
    def serialize(self):
        return {"codigo barras": self.codigo_barras, "cantidad":self.cantidad}

class Tarjeta():
    saldo = 1000

    def mostrar_saldo(self):
        return self.saldo


class CestaCompra():
    catalogo_productos = [{"nombre": "Mango", "codigo barras": "0264899654", "precio sin IVA": 0.85, "% IVA": 0.21},{"nombre": "Pan 100% Integral","codigo barras": "6544498263","precio sin IVA": 0.75, "% IVA": 0.21},{"nombre": "Salsa Soja", "codigo barras": "6621379525","precio sin IVA": 1.85, "% IVA": 0.21}]
    productos = []
    __precio_total = 0
    __precio_total_IVA = 0

    def __init__(self):
        self.__saldo = Tarjeta()

    def agregar_producto(self,producto):
        producto_found = [x for x in self.catalogo_productos if x["codigo barras"] == producto.codigo_barras]
        if (len(producto_found) > 0):
            producto_agregado = {"nombre": producto_found[0]["nombre"], "cantidad": producto.cantidad, "precio sin IVA" : producto_found[0]["precio sin IVA"] * producto.cantidad,  "precio con IVA": (producto_found[0]["precio sin IVA"] * producto.cantidad * producto_found[0]["% IVA"]) + (producto_found[0]["precio sin IVA"] * producto.cantidad)}
            self.productos.append(producto_agregado)
            return f"""
            Producto : {producto_agregado["nombre"]}
            Cantidad : {producto_agregado["cantidad"]}
            Precio sin IVA : {producto_agregado["precio sin IVA"]}
            Precio con IVA : {producto_agregado["precio con IVA"]}

            """
    def importe_total(self):
        precios_sin_IVa= [producto["precio sin IVA"] for producto in self.productos]
        self.__precio_total = sum(precios_sin_IVa)
        return f"Importe total de la compra (sin % IVA aplicado): {round(self.__precio_total,2)}"

    def importe_total_IVA(self):
        precios_IVA = [producto["precio con IVA"] for producto in self.productos]
        self.__precio_total_IVA = sum(precios_IVA)
        return f"Importe total de la compra (% IVA aplicado): {round(self.__precio_total_IVA,2)}"

    def cargo_importe_tarjeta(self):
        if self.__precio_total_IVA > 0 and self.__saldo.saldo> 0:
            self.__saldo.saldo -= self.__precio_total_IVA
            return "Pago cargado con éxito en la cuenta"
        return "No se ha podido realizar el cargo de la compra"


if __name__ == "__main__":
    ticket = CestaCompra()
    print(ticket.agregar_producto(Producto("6544498263",4)))
    print(ticket.agregar_producto(Producto("0264899654", 2)))
    print(ticket.importe_total())
    print(ticket.importe_total_IVA())
    print(ticket.cargo_importe_tarjeta())
   





    