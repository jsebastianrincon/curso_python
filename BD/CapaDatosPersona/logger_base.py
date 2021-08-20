import logging as log

# Handler es un manejador de envio de informacion
log.basicConfig(level=log.DEBUG,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler('capa_datos.log'),
                    log.StreamHandler()
                ])

if __name__ == '__main__':
    log.debug("Mensaje a nivel debug")
    log.info("Mensaje a nivel de info")
    log.warning("Mensaje a nivel de Warning")
    log.error("Mensaje a nivek de error")
    log.critical("Mensaje a nivel de critico")
