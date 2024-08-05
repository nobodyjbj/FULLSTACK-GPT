from fastapi import Body, FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field

app = FastAPI(
    title="Ttolo six numbers Giver",
    description="Get a real six number made by Ttolo.",
    servers=[
        {
            "url": "https://ingredients-sampling-specifics-positioning.trycloudflare.com",
        },
    ],
)


class SixNumbers(BaseModel):
    numbers: str = Field(
        description="The six number that Ttolo made.",
    )
    date: str = Field(
        description="The Date when Ttolo made the six number.",
    )


@app.get(
    "/numbers",
    summary="Returns a random number by Ttolo",
    description="Upon receiving a GET request this endpoint will return a number made by Ttolo himself.",
    response_description="The Object that contains the six numbers made by Ttolo and the date when the six numbers was made.",
    response_model=SixNumbers,
    openapi_extra={
        "x-openai-isConsequential": False,
    },
)
def get_quote(request: Request):
    print(request.headers)
    return {
        "numbers": "1, 2, 3, 4, 5, 6",
        "date": "2024-08-02",
    }


user_token_db = {"ttolo": "ttolo"}


@app.get(
    "/authorize",
    response_class=HTMLResponse,
)
def handle_authorize(client_id: str, redirect_uri: str, state: str):
    return f"""
    <html>
        <head>
            <title>Ttolo Log In</title>
        </head>
        <body>
            <h1>Log Into Ttolo</h1>
            <a href="{redirect_uri}?code=ABCDEF&state={state}">Authorize Nicolacus Maximus GPT</a>
        </body>
    </html>
    """


@app.post("/token")
def handle_token(code=Form(...)):
    return {
        "access_token": user_token_db[code],
    }
