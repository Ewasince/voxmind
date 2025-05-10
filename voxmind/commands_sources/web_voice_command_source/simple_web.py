import asyncio
from pathlib import Path

from fastapi import FastAPI
from starlette.responses import HTMLResponse
from starlette.staticfiles import StaticFiles


class SimpleWebWrapper:
    def __init__(self, app: FastAPI ):
        self._app = app
        self._setup_endpoints()
        self._received_queue = asyncio.Queue()

    async def next_utterance(self):
        return await self._received_queue.get()

    def _setup_endpoints(self):
        current_dir = Path(__file__).resolve().parent
        webapi_dir = current_dir / "webapi_client"

        self._app.mount("/", StaticFiles(directory=webapi_dir, html=True), name="webapi_client")
        self._app.get("/sendRawTxt")(self._send_raw_txt)
        # self._app.get("/", response_class=HTMLResponse)(self._main_page)


    async def _send_raw_txt(self, rawtxt: str, returnFormat: str = "none"):
        await self._received_queue.put(rawtxt)
        return "принято"
