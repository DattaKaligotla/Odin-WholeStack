import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:flutter/material.dart';
import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter_masked_text2/flutter_masked_text2.dart';
import 'package:get/get.dart';
import 'package:odin/screens/home.dart';
import 'package:odin/screens/interests.dart';
import 'package:odin/styles/app_colors.dart';
import 'package:odin/widgets/custom_button.dart';

class OTPScreen extends StatefulWidget {
  final String phoneNumber;

  OTPScreen({required this.phoneNumber});

  @override
  _OTPScreenState createState() => _OTPScreenState();
}

class _OTPScreenState extends State<OTPScreen> {
  final FirebaseAuth _auth = FirebaseAuth.instance;
  late String _verificationId;
  final _codeController = MaskedTextController(mask: '000000');

  @override
  void initState() {
    super.initState();
    _verifyPhone();
  }

  void _verifyPhone() async {
    await _auth.verifyPhoneNumber(
      phoneNumber: widget.phoneNumber,
      verificationCompleted: (PhoneAuthCredential credential) async {
        await _auth.signInWithCredential(credential);

        String uid = _auth.currentUser!.uid;
        var userDoc = await FirebaseFirestore.instance.collection('users').doc(uid).get();
        if (userDoc.exists) {
          Get.offAll(() => HomePage());
        } else {
          Get.offAll(() => InterestsScreen(uid: uid));
        }
      },
      verificationFailed: (FirebaseAuthException e) {
        if (e.code == 'invalid-phone-number') {
          print('The provided phone number is not valid.');
        }
      },
      codeSent: (String verificationId, int? resendToken) {
        setState(() {
          _verificationId = verificationId;
        });
      },
      codeAutoRetrievalTimeout: (String verificationId) {
        setState(() {
          _verificationId = verificationId;
        });
      },
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Enter OTP'),
        backgroundColor: AppColors.blue,
      ),
      body: Container(
        color: AppColors.whiteshade,
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Padding(
              padding: EdgeInsets.all(32),
              child: TextField(
                controller: _codeController,
                decoration: InputDecoration(
                  hintText: 'Enter OTP',
                  contentPadding: EdgeInsets.all(15),
                  border: OutlineInputBorder(
                    borderRadius: BorderRadius.circular(15),
                  ),
                ),
                keyboardType: TextInputType.number,
                textAlign: TextAlign.center,
              ),
            ),
            SizedBox(height: 10),
            Container(
              margin: EdgeInsets.all(32),
              width: double.infinity,
              child: ElevatedButton(
                onPressed: () async {
                  final credential = PhoneAuthProvider.credential(
                    verificationId: _verificationId,
                    smsCode: _codeController.text.trim(),
                  );
                  await _auth.signInWithCredential(credential);

                  String uid = _auth.currentUser!.uid;
                  var userDoc = await FirebaseFirestore.instance.collection('users').doc(uid).get();
                  if (userDoc.exists) {
                    Get.offAll(() => HomePage());
                  } else {
                    Get.offAll(() => InterestsScreen(uid: uid));
                  }
                },
                style: ElevatedButton.styleFrom(
                  primary: AppColors.blue,
                  shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(15),
                  ),
                  padding: EdgeInsets.all(15),
                ),
                child: Text('Verify'),
              ),
            ),
          ],
        ),
      ),
    );
  }
}