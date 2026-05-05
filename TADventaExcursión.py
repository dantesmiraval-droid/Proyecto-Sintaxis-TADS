#Crea una venta vacía con el formato de los tipos de datos que el usuario va a registrar
def crearVenta():
    venta = [0,"","","","",0.0,None]
    return venta

#Ingreso de valores a la estructura de "venta"
def cargarVenta (venta, codigo, nombreServicio, tipoActividad, operadorTuristico, planPago, importe, fechaHora):
    venta[0] = codigo
    venta[1] = nombreServicio
    venta[2] = tipoActividad
    venta[3] = operadorTuristico
    venta[4] = planPago
    venta[5] = importe
    venta[6] = fechaHora

#Salidas de información
def verCodigo(venta):               #imprime el código de venta
    return venta[0]

def verNombreServicio(venta):       #imprime el nombre del servicio de la venta
    return venta[1]

def verTipoActividad(venta):        #imprime el tipo de actividad de la venta
    return venta[2]

def verOperadorTurismo(venta):      #imprime el operador turístico de la venta
    return venta[3]

def verPlanPago(venta):             #imprime el plan de pago o la forma de pago de la venta
    return venta[4]

def verImporte (venta):             #imprime el importe de la venta
    return venta[5]

def verFechaHora(venta):            #imprime la fecha y la hora de la venta
    return venta[6]

#Procesamiento de datos 
def asignarVenta (venta1, venta2):  #copia los datos de la venta1 a la venta2
    venta2[0] = venta1[0]
    venta2[1] = venta1[1]
    venta2[2] = venta1[2]
    venta2[3] = venta1[3]
    venta2[4] = venta1[4]
    venta2[5] = venta1[5]
    venta2[6] = venta1[6]

def cambiarCodigo(venta, nuevoCodigo):                  #modifica el codigo de una venta
    venta[0] = nuevoCodigo

def cambiarNombreServicio(venta, nuevoNombre):          #modifica el nombre del servicio de una venta
    venta[1] = nuevoNombre

def cambiarTipoActividad(venta,nuevoTipo):              #modifica del tipo de actividad que se le asignó a la venta
    venta[2] = nuevoTipo

def cambiarOperadorTurismo(venta, nuevoOperador):       #modifica del operador de turismo asignado referente a la venta
    venta[3] = nuevoOperador

def cambiarPlanPago (venta, nuevoPlan):                 #modifica el plan de pago elegido para la venta
    venta[4] = nuevoPlan

def cambiarImporte(venta, nuevoImporte):                #modifica el monto total/importe de la venta
    venta[5] = nuevoImporte

def cambiarFechaHora(venta, nuevoFecha):                #modifica la fecha y hora en que se realizó la venta 
    venta[6] = nuevoFecha