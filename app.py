import kopf

@kopf.on.startup()
def startup_handler(logger, **kwargs):
    logger.info("Hello World!")

