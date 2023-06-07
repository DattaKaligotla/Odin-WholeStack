// settings_page.dart
import 'package:flutter/material.dart';
import 'package:odin/styles/app_colors.dart';

class SettingsPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Settings', style: TextStyle(color: Colors.white)),
        backgroundColor: AppColors.blue,
      ),
      body: Center(
        child: Text('Settings Page'),
      ),
    );
  }
}
