from funtions import mis_funciones as mf
import sys

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
print(txt_minusculas)