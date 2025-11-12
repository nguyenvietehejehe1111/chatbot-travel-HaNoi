<img width="2410" height="2187" alt="image" src="https://github.com/user-attachments/assets/44453c69-80c4-4159-b786-af7da7b15dbe" /> <img width="225" height="225" alt="image" src="https://github.com/user-attachments/assets/b4c7088d-e8a9-49a2-bee9-8372d587a20d" />


 ỨNG DỤNG CHAT AI DU LỊCH HÀ NỘI
(Flask Backend + Google Gemini API + Flutter Frontend)
 Giới thiệu

Đây là ứng dụng Chat AI Du lịch Hà Nội, cho phép người dùng đặt câu hỏi liên quan đến địa điểm, ẩm thực, văn hóa, lịch trình du lịch tại Hà Nội, và nhận câu trả lời tự động bằng AI Gemini của Google.

Ứng dụng gồm 2 phần:

Frontend (Flutter App): Giao diện chat thân thiện, gửi câu hỏi đến server Flask.

Backend (Flask Server): Xử lý yêu cầu, gửi dữ liệu đến Google Gemini API, nhận kết quả và trả về cho ứng dụng.

 Kiến trúc hệ thống

Hệ thống hoạt động theo mô hình sau:

Người dùng nhập câu hỏi trong ứng dụng Flutter.

Ứng dụng gửi request đến Flask Server qua endpoint /ask.

Flask Server gọi Gemini API (qua requests.post) để lấy câu trả lời AI.

Kết quả được trả về cho Flutter và hiển thị lên giao diện.

 Sơ đồ kiến trúc tổng quát:


 Công nghệ sử dụng
Thành phần	Công nghệ
Ngôn ngữ	Python (Flask), Dart (Flutter)
AI Model	Google Gemini 1.5 Pro API
API Endpoint	https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-pro-latest:generateContent
Công cụ	Google Cloud Console, VS Code, Flask-CORS
 Cài đặt & Chạy thử
1️ Tạo API Key Gemini

Truy cập Google AI Studio
.

Đăng nhập bằng tài khoản Google.

Chọn Create API Key, sao chép lại API Key.

Dán vào file .env hoặc thêm trực tiếp trong server.py:

GEMINI_API_KEY = "YOUR_API_KEY"

2️ Cài đặt backend Flask
pip install flask flask-cors requests
python server.py


Server chạy tại: http://127.0.0.1:5000/ask

3️ Cấu trúc file server.py (ví dụ rút gọn)
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests, os

app = Flask(__name__)
CORS(app)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY") or "YOUR_API_KEY"
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-pro-latest:generateContent"

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    question = data.get("question", "")
    try:
        resp = requests.post(
            f"{API_URL}?key={GEMINI_API_KEY}",
            json={"contents": [{"parts": [{"text": question}]}]}
        )
        resp_json = resp.json()
        reply = resp_json["candidates"][0]["content"]["parts"][0]["text"]
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)

4️ Cấu trúc dự án Flutter (Frontend)
/lib
 ├── main.dart
 ├── screens/
 │    └── chat_screen.dart
 └── services/
      └── api_service.dart


Ví dụ đoạn gọi API trong Flutter:

final response = await http.post(
  Uri.parse('http://127.0.0.1:5000/ask'),
  headers: {'Content-Type': 'application/json'},
  body: jsonEncode({'question': userInput}),
);

💬 Ví dụ câu hỏi
Câu hỏi	Kết quả mẫu
“Ăn gì ngon ở phố cổ Hà Nội?”	“Bạn có thể thử phở Bát Đàn, bún chả Hàng Mành, cà phê Giảng…”
“Gợi ý lịch trình 1 ngày khám phá Hà Nội”	“Sáng: thăm Lăng Bác - Văn Miếu, Trưa: ăn bún chả, Chiều: Hồ Gươm - phố cổ…”
 Tác giả & Ghi chú

Tác giả: Việt Nguyễn

Công nghệ AI: Google Gemini 1.5 Pro

Mục tiêu: Ứng dụng mô phỏng ChatGPT, tập trung trả lời về du lịch Hà Nội.
