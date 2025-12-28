import razorpay
from dotenv import load_dotenv
import os

client = razorpay.client(
    auth=(
        os.getenv("RAZORPAY_KEY_ID"),
        os.getenv("RAZORPAY_SECRET")
    )
    
)