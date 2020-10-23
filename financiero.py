from clases import BankDeras, Ingreso, Egreso

print("Inicio aplicación")
print("Gracias por usar la applicación de finanzas bankDeras. \n")

bankObj = BankDeras()

registroIng = 0
registroEg = 0


def iniciarCuenta():
    bankObj.iniciarCuenta()
    print(bankObj.obtenerSaldo())


def registrarIngreso():
    cantidadIngresada = float(input("Monto: "))
    ingreso = Ingreso("ingreso", cantidadIngresada)
    bankObj.registrarIngreso(ingreso)
    print(f"saldo: {bankObj.obtenerSaldo()}")


def registrarEgreso():
    cantidadEgresada = float(input("Monto: "))
    egreso = Egreso("Egreso", cantidadEgresada)
    bankObj.registrarEgreso(egreso)
    print(f"saldo: {bankObj.obtenerSaldo()}")

def reporteIngresos():
    bankObj.reporteIng()

def reporteEgresos():
    bankObj.reporteEg()

def reporteOperaciones():
    bankObj.reporteIng()
    bankObj.reporteEg()

def obtenerSaldo():
    print(f"saldo: {bankObj.obtenerSaldo()}")

while True:
    print("Menu: \n")
    print("0 - salir")
    print("1 - iniciar cuenta")
    print("2 - registrar ingreso")
    print("3 - registrar egreso")
    print("4 - generar reporte ingresos")
    print("5 - generar reporte egresos")
    print("6 - generar reporte operaciones (ingresos y egresos")
    print("7 - generar reporte del saldo de la cuenta")
    option = int(input("opcion: "))

    if option == 0:
        break
    elif option == 1:
        iniciarCuenta()
    elif option == 2:
        registarIngreso()
    elif option == 3:
        registrarEgreso()
    elif option == 4:
        reporteIngresos()
    elif option == 5:
        reporteEgresos()
    elif option == 6:
        reporteOperaciones()
    elif option == 7:
        obtenerSaldo()


