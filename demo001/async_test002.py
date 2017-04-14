import asyncio
import datetime


@asyncio.coroutine
def bug():
    raise Exception("not consumed")


@asyncio.coroutine
def handle_exception():
    try:
        yield from bug()
    except Exception:
        print("exception consumed: {0}".format(datetime.datetime.now()))


loop = asyncio.get_event_loop()
asyncio.ensure_future(handle_exception())
loop.run_forever()
loop.close()
