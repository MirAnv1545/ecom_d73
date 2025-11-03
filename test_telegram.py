import requests

# 🧠 Mana bu joylarga o'zingizning ma'lumotlaringizni kiriting:
TOKEN = "8407894917:AAFjwaoiGonv1LS98SImkKwS6ZIcOBIyDN8"
CHAT_ID = "962349453"

def test_telegram():
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": "✅ Telegram test from Django project"
    }

    try:
        response = requests.post(url, json=data)
        print("Status code:", response.status_code)
        print("Response text:", response.text)
    except Exception as e:
        print("❌ Connection error:", e)


if __name__ == "__main__":
    test_telegram()
