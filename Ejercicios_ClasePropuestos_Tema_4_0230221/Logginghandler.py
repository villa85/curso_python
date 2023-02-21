import logging

logger = logging.getLogger('Ejemplo de LOG')

# Todos los mensajes de niveles superiores a DEBUG se guardan en el fichero
fh = logging.FileHandler('debug.log') # Archivo
fh.setLevel(logging.DEBUG)

# Todos los mensajes de ERROR o CRITICAL se mostrarán en la consola
ch = logging.StreamHandler()  # Consola
ch.setLevel(logging.ERROR)

#formato de los mensajes
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# Creamos los objetos
logger.addHandler(fh)
logger.addHandler(ch)

# Código de nuestra aplicación
logger.debug('mensaje debug')
logger.info('mensaje info')
logger.warning('mensaje warning')
logger.error('mensaje error')
logger.critical('mensaje critical')