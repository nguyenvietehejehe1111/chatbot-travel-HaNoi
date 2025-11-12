from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os
import requests

# Load biến môi trường từ .env
load_dotenv()

app = Flask(__name__)
CORS(app)  # Bật CORS cho tất cả domain

# Lấy thông tin từ .env
API_KEY = os.getenv("GOOGLE_API_KEY")
PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT")
LOCATION = os.getenv("GOOGLE_CLOUD_LOCATION", "global")
MODEL = os.getenv("MODEL", "gemini-2.5-flash")

SYSTEM_PROMPT = """
Bạn là trợ lý AI du lịch của thành phố Hà Nội. 
Bạn chỉ trả lời các câu hỏi liên quan đến du lịch, văn hóa, lịch sử, ẩm thực, địa điểm tham quan tại Hà Nội.
Nếu người dùng hỏi về chủ đề khác, hãy trả lời ngắn gọn rằng bạn chỉ cung cấp thông tin về du lịch Hà Nội.
"""

@app.route("/ask", methods=["POST"])
def ask():
    user_message = request.json.get("message", "").strip()
    if not user_message:
        return jsonify({"error": "Thiếu message"}), 400

    body = {
        "systemInstruction": {"role": "system", "parts": [{"text": SYSTEM_PROMPT}]},
        "contents": [{"role": "user", "parts": [{"text": user_message}]}],
        "generationConfig": {"temperature": 0.7, "maxOutputTokens": 512}
    }

    url = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={API_KEY}"

    try:
        resp = requests.post(url, json=body, timeout=10)
    except Exception as e:
        print("Lỗi gọi Gemini API:", e)
        return jsonify({"error": "Không thể gọi Gemini API", "details": str(e)}), 500

    # Debug: in JSON trả về
    try:
        resp_json = resp.json()
        print("Gemini full response:", resp_json)
    except Exception as e:
        print("Lỗi parse JSON từ Gemini:", e)
        return jsonify({"error": "Không parse được JSON từ Gemini", "details": str(e), "raw": resp.text}), 500

    # Parse an toàn
    try:
        candidates = resp_json.get("candidates")
        if not candidates or len(candidates) == 0:
            return jsonify({"error": "Gemini API trả về không có candidates", "raw": resp_json}), 500

        parts = candidates[0].get("content", {}).get("parts", [])
        reply = "".join([p.get("text", "") for p in parts])
        if not reply:
            reply = "Gemini trả về nội dung trống"
    except Exception as e:
        print("Lỗi parsing content:", e)
        return jsonify({"error": "Không parse được nội dung trả về", "details": str(e), "raw": resp_json}), 500

    return jsonify({"reply": reply})

if __name__ == "__main__":
    # Chạy trên tất cả IP, port 5000, debug True
    print("Flask server đang chạy trên 0.0.0.0:5000")
    app.run(host="0.0.0.0", port=5000, debug=True)
