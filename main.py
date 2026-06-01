from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Webhook server running"}


@app.post("/webhook")
async def github_webhook(request: Request):

    payload = await request.json()

    print("\n========== GITHUB WEBHOOK ==========")

    print(payload)

    return {"status": "received"}