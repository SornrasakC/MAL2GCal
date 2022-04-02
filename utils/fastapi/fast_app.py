from fastapi import FastAPI

app = FastAPI()

@app.get("/oauth")
async def oauth(code):
    # print(code)
    with open('data/mal_auth_code.txt', 'w', encoding='utf-8') as f:
        f.write(code)

    return {"message": "Done, you can close this tab."}
