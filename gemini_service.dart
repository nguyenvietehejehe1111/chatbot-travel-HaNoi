import 'dart:convert';
import 'package:http/http.dart' as http;

class GeminiService {
  final String baseUrl = "http://127.0.0.1:5000"; // URL Flask server
  final String endpoint = "/ask";

  Future<String> ask(String message) async {
    final url = Uri.parse(baseUrl + endpoint);
    try {
      final response = await http.post(
        url,
        headers: {"Content-Type": "application/json"},
        body: jsonEncode({"message": message}),
      );

      if (response.statusCode == 200) {
        final data = jsonDecode(response.body);
        return data["reply"] ?? "Không có phản hồi";
      } else {
        return "Lỗi: Server trả về ${response.statusCode}";
      }
    } catch (e) {
      return "Lỗi kết nối server: $e";
    }
  }
}
