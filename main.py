from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Webhook server running"}


@app.post("/webhook")
async def github_webhook(request: Request):

    body = await request.body()

    print("\n========== REQUEST RECEIVED ==========")

    if not body:
        print("Empty body received")
        return {"status": "received"}

    payload = await request.json()

    event = request.headers.get("X-GitHub-Event")

    print("GitHub Event:", event)
    print(payload)

    return {"status": "received"}