import json
def json_response(data, status=200):
    body = json.dumps(data).encode("utf-8")
    return {
        "status": status,
        "headers": [
            (b"content-type", b"application/json"),
            (b"content-length", str(len(body)).encode("utf-8")),
        ],
        "body": body,
    }
async def app(scope, receive, send):
    if scope["type"] != "http":
        return

    method = scope["method"]
    path = scope["path"]
    # Wait for the HTTP request event
    await receive()
    if method == "GET" and path == "/":
        response = json_response({
            "message": "Hello from raw ASGI"
        })

    elif method == "GET" and path == "/users":
        response = json_response({
            "users": [
                {"id": 1, "name": "Alice"},
                {"id": 2, "name": "Bob"},
            ]
        })

    elif method == "GET" and path == "/health":
        response = json_response({
            "status": "ok"
        })

    else:
        response = json_response(
            {"error": "Not Found"},
            status=404,
        )

    # Start HTTP response
    await send({
        "type": "http.response.start",
        "status": response["status"],
        "headers": response["headers"],
    })

    # Send response body
    await send({
        "type": "http.response.body",
        "body": response["body"],
    })