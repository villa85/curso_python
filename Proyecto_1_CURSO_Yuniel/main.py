from funtions import mis_funciones as mf

archivo = open('datos\\articulo.txt', encoding="utf8")
articulo = archivo.read()

cantidad_palablas_antes = len(mf.split_cadena(articulo)) # 2. Contar cuantas palabras tiene el texto antes de preprocesarlo
todo_minusculas = mf.texto_en_minusculas(articulo) # 3. Convertir el texto Normalizado a minúsculas
texto_no_signos = mf.elimina_signos_puntuacion(todo_minusculas) # 4 Identificar, mostrar y eliminar signos de puntuación
mostrar_signos_del_texto = mf.elimina_repetidos(mf.elimina_signos_puntuacion(todo_minusculas, signos = True))

print(mostrar_signos_del_texto)