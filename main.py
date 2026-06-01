from fastapi import FastAPI, Request

from database import (
    init_db,
    save_event,
    get_events
)

app = FastAPI()

init_db()


@app.get("/")
def home():

    return {
        "message": "Webhook Tracker Running"
    }


@app.post("/webhook")
async def github_webhook(request: Request):

    payload = await request.json()

    repo = payload.get(
        "repository",
        {}
    ).get(
        "full_name"
    )

    commits = payload.get(
        "commits",
        []
    )

    for commit in commits:

        author = commit["author"]["name"]

        message = commit["message"]

        save_event(
            repo,
            author,
            message
        )

        print(
            f"{repo} | {author} | {message}"
        )

    return {
        "status": "saved"
    }


@app.get("/events")
def events():

    data = get_events()

    return {
        "events": data
    }