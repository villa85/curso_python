from funtions import mis_funciones as mf

archivo = open('datos\\articulo.txt', encoding="utf8")
articulo = archivo.read()

cantidad_palablas_antes = len(mf.split_cadena(articulo)) # 2. Contar cuantas palabras tiene el texto antes de preprocesarlo
todo_minusculas = mf.texto_en_minusculas(articulo) # 3. Convertir el texto Normalizado a minúsculas
texto_no_signos = mf.elimina_signos_puntuacion(todo_minusculas) # 4 Identificar, mostrar y eliminar signos de puntuación
mostrar_signos_del_texto = mf.elimina_repetidos(mf.elimina_signos_puntuacion(todo_minusculas, signos = True))

# print(mf.normalize(texto_no_signos, find = True), end= " \n \n ")
texto_sin_tildes = mf.normalize(texto_no_signos)
texto_sin_numeros = mf.extrae_numeros(texto_sin_tildes)
numeros = mf.extrae_numeros(texto_sin_tildes, number = True)
texto_sin_numeros = mf.extrae_numeros(texto_sin_tildes)
print(f"{numeros}")
print(f"{texto_sin_numeros}")