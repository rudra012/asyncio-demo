import asyncio


@asyncio.coroutine
def bug():
    raise Exception("not consumed")


loop = asyncio.get_event_loop()
task = asyncio.ensure_future(bug())
try:
    loop.run_until_complete(task)
except Exception:
    print("exception consumed")
