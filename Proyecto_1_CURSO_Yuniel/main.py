from funtions import mis_funciones as mf

archivo = open('datos\\articulo.txt', encoding="utf8")
articulo = archivo.read()

file = open('datos\\stopwords_español.txt', encoding="utf8") # 1. Leer el archivo texto
stop_words = file.read()

cantidad_palablas_antes = len(mf.split_cadena(articulo)) # 2. Contar cuantas palabras tiene el texto antes de preprocesarlo

todo_minusculas = mf.texto_en_minusculas(articulo) # 3. Convertir el texto Normalizado a minúsculas
texto_no_signos = mf.elimina_signos_puntuacion(todo_minusculas) # 4 Identificar, mostrar y eliminar signos de puntuación
mostrar_signos_del_texto = mf.elimina_repetidos(mf.elimina_signos_puntuacion(todo_minusculas, signos = True))

# print(mf.normalize(texto_no_signos, find = True), end= " \n \n ")
texto_sin_tildes = mf.normalize(texto_no_signos)
texto_sin_numeros = mf.extrae_numeros(texto_sin_tildes)
numeros = mf.extrae_numeros(texto_sin_tildes, number = True)
texto_sin_numeros = mf.extrae_numeros(texto_sin_tildes)
palabras_mayusculas = mf.extrae_mayusculas(articulo)
siglas = mf.extrae_mayusculas(articulo, siglas= True)
# print(palabras_mayusculas)
# print(siglas)
texto_sin_tildes_stop_words = mf.normalize(stop_words)
texto_filtrado_no_stop_words = mf.elimina_stop_words(texto_sin_numeros, texto_sin_tildes_stop_words)
print(texto_filtrado_no_stop_words)
# print(cantidad_palablas_antes)
# print(len(texto_filtrado_no_stop_words))
# print(stop_words)

