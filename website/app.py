from pathlib import Path

from .content import Content


BASE_PATH = Path(__file__).parent.absolute()
BASE_CONTENT_PATH = BASE_PATH / "content"


content = Content(BASE_CONTENT_PATH)


async def app(scope, receive, send):
    path = scope["path"]

    try:
        html = content[path]
    except KeyError:
        await send(
            {
                "type": "http.response.start",
                "status": 404,
                "headers": [(b"content-type", b"text/html")],
            }
        )
        await send({"type": "http.response.body", "body": "404".encode()})
    else:
        # HTML found
        await send(
            {
                "type": "http.response.start",
                "status": 200,
                "headers": [(b"content-type", b"text/html")],
            }
        )
        await send({"type": "http.response.body", "body": html.encode()})
