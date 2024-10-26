from fastapi import APIRouter, HTTPException
from utils.otp_generator import generateOTP
from utils.google_smtp import send_email
from utils.renderer import render_template
content_router = APIRouter()

@content_router.get("/forgot_pass")
async def send_reset_link(email_id: str, reset_link:str):
    render_data = {"reset_link":reset_link}
    rendered_data = render_template("forgot_pass.html", render_data)
    subject = "Password Reset Request"
    content = {
        "body" : rendered_data,
        "Subject": subject
    }
    send_email(email_id, content)
    raise HTTPException(status_code=200, detail="Reset link sent successfully!")