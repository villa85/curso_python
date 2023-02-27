from funtions import mis_funciones as mf
import sys
import re

try:
    s_weets_file = 'sentweets_esp.txt'
    file_s = open("datos\\"+s_weets_file, encoding="utf8") # PASO 11 CONTROL DE EXCEPCIONES
    sentweets = file_s.read(10000)
    file_s.close()
except IOError as error:
    print('Problema con el fichero: {}.  {}'.format(file_s, error) )
except:  # si es un error diferente a IOError
    print("Error inesperado:", sys.exc_info()[0])
    raise

try:
    positive_file = 'positive_lex.txt'
    positive_s = open("datos\\"+positive_file, encoding="utf8") # PASO 11 CONTROL DE EXCEPCIONES
    positive = positive_s.read()
    positive_s.close()
except IOError as error:
    print('Problema con el fichero: {}.  {}'.format(positive_s, error) )
except:  # si es un error diferente a IOError
    print("Error inesperado:", sys.exc_info()[0])
    raise

try:
    negative_file = 'negative_lex.txt'
    negative_s = open("datos\\"+negative_file, encoding="utf8") # PASO 11 CONTROL DE EXCEPCIONES
    negative = negative_s.read()
    negative_s.close()
except IOError as error:
    print('Problema con el fichero: {}.  {}'.format(negative_s, error) )
except:  # si es un error diferente a IOError
    print("Error inesperado:", sys.exc_info()[0])
    raise



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

txt_minusculas = mf.texto_en_minusculas(sentweets)
texto_sin_signos = mf.elimina_signos_puntuacion(txt_minusculas)
texto_sin_letras_acent_sentweets = mf.letras_acentuadas(texto_sin_signos)
texto_s_sin_numeros = mf.extrae_numeros(texto_sin_letras_acent_sentweets)
texto_sin_tildes_stop_words = mf.letras_acentuadas(stop_words)
texto_sentweets_filtrado_no_stop_words = mf.elimina_stop_words(texto_s_sin_numeros, texto_sin_tildes_stop_words)

print(texto_sentweets_filtrado_no_stop_words)

# positive_sin_acentos = mf.letras_acentuadas(positive)
# negative_sin_acentos = mf.letras_acentuadas(negative)
# lista_negativas = mf.normaliza(negative_sin_acentos)
# lista_positivas = mf.normaliza(positive_sin_acentos)

# lista_conteo_palabras = mf.contar_palabras(texto_sentweets_filtrado_no_stop_words)

# lista_total_positivas = mf.calculo_puntuacion_palabras(lista_positivas, lista_conteo_palabras)
# lista_total_negativas = mf.calculo_puntuacion_palabras(lista_negativas, lista_conteo_palabras)
# total_puntos_positivos = mf.total_puntuacion(lista_total_positivas)
# total_puntos_negativos = mf.total_puntuacion(lista_total_negativas)

# print(total_puntos_positivos)
# print(total_puntos_negativos)
# print(lista_total_negativas)

# for i in lista_positivas:
#     for j in lista_conteo_palabras:
#         if i[0] == j[0]:
#             lista_total_positivas.append((i[0], i[1]*j[1]))
# print(lista_total_positivas)

# print(lista_conteo_palabras)
# texto_sin_url = mf.extraer_url(sentweets)
# texto_sin_usuarios = mf.extraer_usuarios(sentweets)
# print(lista_positivas)