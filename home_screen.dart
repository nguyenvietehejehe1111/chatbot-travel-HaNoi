import 'package:flutter/material.dart';
import 'chatbot_screen.dart';

class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text("Du lịch thông minh Hà Nội")),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Image.asset("assets/hanoi.jpg", height: 200),
            const SizedBox(height: 20),
            const Text(
              "Khám phá Hà Nội cùng Trợ lý AI!",
              style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
            ),
            const SizedBox(height: 20),
            ElevatedButton(
              onPressed: () {
                Navigator.push(context,
                    MaterialPageRoute(builder: (_) => ChatbotScreen()));
              },
              child: const Text("Bắt đầu trò chuyện với AI"),
            ),
          ],
        ),
      ),
    );
  }
}
