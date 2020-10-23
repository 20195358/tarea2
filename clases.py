class BankDeras:
    def __init__(self):
        self.saldo = 0
        self.listaIngresos = []
        self.listaEgresos = []

    def obtenerSaldo(self):
        return self.saldo

    def registrarIngreso(self, ingreso):
        self.listaIngresos.append(ingreso)
        self.actualizarSaldo()
    
    def registrarEgreso(self, egreso):
        self.listaEgresos.append(egreso)
        self.actualizarSaldo()

    def actualizarSaldo(self):
        totalIngreso = self.obtenerTotalIngresos()
        totalEgreso = self.obtenerTotalEgresos()
        self.saldo = totalIngreso - totalEgreso

    def obtenerTotalIngresos(self):
        resultado = 0.0
        for ingreso in self.listaIngresos:
            resultado += ingreso.cantidad
        return resultado

    def obtenerTotalEgresos(self):
        resultado = 0.0
        for egreso in self.listaEgresos:
            resultado += egreso.cantidad
        return resultado

    def reporteIng(self):
        resultado = "Lista de ingresos: "
        for x in self.listaIngresos:
            resultado += "\n * {}".format(x)
            return resultado
            
    def reporteEg(self):
        resultado = "Lista de egresos: "
        for x in self.listaEgresos:
            resultado += "\n * {}".format(x)
            return resultado

class Ingreso:
    def __init__(self, titulo, cantidad):
        self.titulo = titulo
        self.cantidad = cantidad


class Egreso:
    def __init__(self, titulo, cantidad):
        self.titulo = titulo
        self.cantidad = cantidad
