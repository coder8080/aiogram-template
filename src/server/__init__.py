from aiohttp import web

from src.common.environment import get_str_env

POD_NAME = get_str_env("POD_NAME")


async def pod_name(request: web.Request):
    return web.json_response({"pod_name": POD_NAME})


async def start_site():
    app = web.Application()
    app.router.add_get("/pod_name", pod_name)

    runner = web.AppRunner(app)
    await runner.setup()

    site = web.TCPSite(runner, port=3000)
    await site.start()
