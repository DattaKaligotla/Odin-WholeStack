import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:odin/controllers/auth_controller.dart';
import 'package:odin/screens/landing.dart';
import 'package:odin/utils/constants.dart';
import 'package:firebase_core/firebase_core.dart'; // Add this import
import 'firebase_options.dart';
void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await firebaseInitialization.then((value) => {
        Get.put(AuthController()),
      });
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return GetMaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: const LandingPage(),
    );
  }
}
