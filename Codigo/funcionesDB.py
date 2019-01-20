import sqlite3

'''
Buscar en la base de datos
Necesita la conexion con base de datos, tabla a buscar, y si es necesario una condicion.
Si la condicion no se especifica, regresara todos los campos.
Regresa el resutado de la busqueda en forma de lista 
'''
def buscar_bd(bd, tabla, condicion='1=1'):
	cursor = bd.cursor();
	sentencia = "SELECT * FROM "+tabla+" WHERE "+ condicion +";"
	cursor.execute( sentencia )
	resultado = cursor.fetchall()

	return resultado


'''
Verificar contrasenia de usuario
Utlizamos la funcion buscar_bd() para buscar al usuario.
Si el resultado es 0, entonces no se encuentra el usuario en la base de datos
En caso de que exista, se verifica si las contrasenias son iguales.
'''
def verificarCredenciales(bd, usuario, contrasenia):
	resultado = buscar_bd(bd, "user", "username='"+ usuario +"'" )
	if( len( resultado) == 0 ):
		return "El usuario no existe"
	else:
		usuario = resultado[0]
		if( str(usuario[3]) == contrasenia ):
			return "Inicio de sesion exitoso"
		else:
			return "La contrasenia esta incorrecta"
