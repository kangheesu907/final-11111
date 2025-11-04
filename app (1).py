from fastapi import FastAPI, Form
from fastapi.responses import JSONResponse
from openai import OpenAI

app = FastAPI()
client = OpenAI()

@app.post("/chat/")
async def chat(message: str = Form(...)):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "당신은 고객 응대 전문 상담사입니다. 친근하고 공감 어린 말투로 응답하세요."
            },
            {
                "role": "user",
                "content": message
            }
        ]
    )
    return JSONResponse({"reply": response.choices[0].message["content"]})
