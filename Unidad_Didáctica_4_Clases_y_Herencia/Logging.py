import logging

def main():

    logFormatter = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

    logging.basicConfig(level=logging.DEBUG, filename="milog.log", filemode='a', format= logFormatter, datefmt='%d-%b-%y %H:%M:%S')
    logger = logging.getLogger()  # crear el objeto

    logger.warning('Estos se registrará en el archivo milog.log')
    logger.info('El administrador, ha iniciado sesisón')

    logger.debug('Esto es un ejemplo...')
    logger.error('Este es un mensaje de error')
    logger.critical('Este es un mensaje Critico')
    logger.warning('El administrador, ha cerrado su sesisón')


if __name__ == '__main__':
    main()

