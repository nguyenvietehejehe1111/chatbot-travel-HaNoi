import 'package:flutter/material.dart';
import 'chatbot_screen.dart';

void main() {
  runApp(const TravelAIApp());
}

class TravelAIApp extends StatelessWidget {
  const TravelAIApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Travel AI Hanoi',
      theme: ThemeData(primarySwatch: Colors.green),
      home: const ChatbotScreen(), // Hiển thị ChatbotScreen làm màn hình chính
    );
  }
}