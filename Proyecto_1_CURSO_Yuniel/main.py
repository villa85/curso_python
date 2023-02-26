from funtions import mis_funciones as mf
import sys

archivo = open('datos\\articulo.txt', encoding="utf8")
articulo = archivo.read()

file = open('datos\\stopwords_español.txt', encoding="utf8") # 1. Leer el archivo texto
stop_words = file.read()

cantidad_palablas_antes = len(mf.split_cadena(articulo)) # 2. Contar cuantas palabras tiene el texto antes de preprocesarlo

todo_minusculas = mf.texto_en_minusculas(articulo) # 3. Convertir el texto Normalizado a minúsculas
texto_no_signos = mf.elimina_signos_puntuacion(todo_minusculas)
solo_signos = mf.elimina_signos_puntuacion(todo_minusculas, signos = True)

letras_acentuadas = mf.letras_acentuadas(texto_no_signos , find = True)
texto_sin_letras_acentuadas = mf.letras_acentuadas(texto_no_signos)

numeros = mf.extrae_numeros(texto_sin_letras_acentuadas, number = True)
texto_sin_numeros = mf.extrae_numeros(texto_sin_letras_acentuadas)


try:
    r_file = 'stopwords_español.txt'
    file = open("datos\\"+r_file, encoding="utf8") # PASO 11 CONTROL DE EXCEPCIONES
    stop_words = file.read()
    file.close()
except IOError as error:
    print('Problema con el fichero: {}.  {}'.format(r_file, error) )
except:  # si es un error diferente a IOError
    print("Error inesperado:", sys.exc_info()[0])
    raise

texto_sin_tildes_stop_words = mf.letras_acentuadas(stop_words) # quita las tildes del las stop_words
texto_filtrado_no_stop_words = mf.elimina_stop_words(texto_sin_numeros, texto_sin_tildes_stop_words) # devuelve el texto filtrado sin stop words
cantidad_palablas = len(mf.split_cadena(texto_filtrado_no_stop_words))


try:
    s_weets_file = 'sentweets_esp.txt'
    file_s = open("datos\\"+s_weets_file, encoding="utf8") # PASO 11 CONTROL DE EXCEPCIONES 
    sentweets = file_s.read()
    file_s.close()
except IOError as error:
    print('Problema con el fichero: {}.  {}'.format(file_s, error) )
except:  # si es un error diferente a IOError
    print("Error inesperado:", sys.exc_info()[0])
    raise

txt_minusculas = mf.texto_en_minusculas(sentweets)
texto_sin_signos = mf.elimina_signos_puntuacion(txt_minusculas)
signos = mf.elimina_repetidos(mf.elimina_signos_puntuacion(txt_minusculas, signos = True))

letras_acent_sentweets = mf.letras_acentuadas(texto_sin_signos , find = True)
texto_sin_letras_acent_sentweets = mf.letras_acentuadas(texto_sin_signos)

numeros_s = mf.extrae_numeros(texto_sin_letras_acent_sentweets, number = True)
texto_s_sin_numeros = mf.extrae_numeros(texto_sin_letras_acent_sentweets)

siglas_s = mf.extrae_mayusculas(sentweets, siglas= True)

texto_sin_tildes_stop_words = mf.letras_acentuadas(stop_words) # quita las tildes del las stop_words
texto_filtrado_no_stop_words = mf.elimina_stop_words(texto_s_sin_numeros, texto_sin_tildes_stop_words) # devuelve el texto filtrado sin stop words
# print(texto_filtrado_no_stop_words)
print("texto_filtrado_no_stop_words")


# mostrar_signos_del_texto = mf.elimina_repetidos(mf.elimina_signos_puntuacion(todo_minusculas, signos = True))

# # print(mf.normalize(texto_no_signos, find = True), end= " \n \n ")
# texto_sin_tildes = mf.normalize(texto_no_signos)
# texto_sin_numeros = mf.extrae_numeros(texto_sin_tildes)
# numeros = mf.extrae_numeros(texto_sin_tildes, number = True)
# texto_sin_numeros = mf.extrae_numeros(texto_sin_tildes)
# palabras_mayusculas = mf.extrae_mayusculas(articulo)
# siglas = mf.extrae_mayusculas(articulo, siglas= True)
# texto_sin_tildes_stop_words = mf.normalize(stop_words)
# texto_filtrado_no_stop_words = mf.elimina_stop_words(texto_sin_numeros, texto_sin_tildes_stop_words)
# # cant = mf.contar_palabras(texto_filtrado_no_stop_words)
# # print(cant)
# # print(siglas)
# texto_sin_tildes = mf.normalize(todo_minusculas)
# tuplas_cantidad = mf.contar_palabras(texto_filtrado_no_stop_words)

# try:
#     s_weets_file = 'sentweets_esp.txt'
#     file_s = open("datos\\"+s_weets_file, encoding="utf8") # PASO 11 CONTROL DE EXCEPCIONES
#     sentweets = file_s.read()
#     file_s.close()
# except IOError as error:
#     print('Problema con el fichero: {}.  {}'.format(file_s, error) )
# except:  # si es un error diferente a IOError
#     print("Error inesperado:", sys.exc_info()[0])
#     raise

# txt_minusculas = mf.texto_en_minusculas(sentweets)
# # texto_sin_signos = mf.elimina_signos_puntuacion(txt_minusculas, signos = True)
# # no_signos_repetidos = mf.elimina_repetidos(texto_sin_signos)
# texto_sin_signos = mf.elimina_signos_puntuacion(txt_minusculas)
# signos = mf.elimina_repetidos(mf.elimina_signos_puntuacion(txt_minusculas, signos = True))
# print(texto_sin_signos)
# # print(cantidad_palablas_antes)
# # print(len(texto_filtrado_no_stop_words))
# # print(stop_words)
