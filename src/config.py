import os

WHATSAPP_NUMBER = os.getenv("WHATSAPP_NUMBER")
MESSAGE = ( "Bom dia namorada")

SEND_HOUR = 6
SEND_MINUTE = 58

CHROME_PROFILE_PATH = os.getenv(
    "CHROME_PROFILE_PATH",
    "/opt/whatsapp-bot/chrome/profile"
)

print("DEBUG CONFIG:")
print("WHATSAPP_NUMBER =", WHATSAPP_NUMBER)
print("CHROME_PROFILE_PATH =", CHROME_PROFILE_PATH)
print("SEND_HOUR =", SEND_HOUR)
print("SEND_MINUTE =", SEND_MINUTE)
