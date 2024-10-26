from fastapi import APIRouter, HTTPException
from utils.otp_generator import generateOTP
from utils.google_smtp import send_email
from utils.renderer import render_template
otp_router = APIRouter()

@otp_router.get("/send_otp")
async def send_otp(email_id: str):
    otp = generateOTP()
    render_data = {"otp":otp}
    rendered_data = render_template("send_otp.html", render_data)
    subject = "Verification OTP"
    content = {
        "body" : rendered_data,
        "Subject": subject
    }
    send_email(email_id, content)
    raise HTTPException(status_code=200, detail="OTP sent successfully!")