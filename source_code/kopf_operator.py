import kopf

LOCK: asyncio.Lock

@kopf.on.startup()
async def startup_fn(logger, **kwargs):
    global LOCK
    LOCK = asyncio.Lock()
    print("Hello World!")

if __name__ == '__main__':
    kopf.run()

