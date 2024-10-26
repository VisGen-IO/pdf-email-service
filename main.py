from fastapi import FastAPI
import uvicorn
from routes.email_tigger.send_otp import otp_router
from routes.email_tigger.send_content import content_router
app = FastAPI()

app.include_router(otp_router)
app.include_router(content_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8500, reload=True)