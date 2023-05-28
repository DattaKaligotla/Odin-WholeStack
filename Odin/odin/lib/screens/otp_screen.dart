import 'package:flutter/material.dart';
import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter_masked_text2/flutter_masked_text2.dart';
import 'package:odin/screens/home.dart';
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
      },
      verificationFailed: (FirebaseAuthException e) {
        print(e);
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

  void _validateOtpAndLogin() async {
    try {
      final credential = PhoneAuthProvider.credential(
        verificationId: _verificationId,
        smsCode: _codeController.text.trim(),
      );
      final UserCredential userCredential = await _auth.signInWithCredential(credential);

      if (userCredential.user != null) {
        Navigator.pushAndRemoveUntil(
          context,
          MaterialPageRoute(builder: (context) => HomePage()),
          (Route<dynamic> route) => false,
        );
      }
    } on FirebaseAuthException catch (e) {
      print(e);
    }
  }
  final List<TextEditingController> _codeControllers = List<TextEditingController>.generate(6, (index) => TextEditingController());
  // Initialize the FocusNode for each digit
  final List<FocusNode> _focusNodes = List<FocusNode>.generate(6, (index) => FocusNode());

  // Function to focus on the next field
  void nextField(String value, FocusNode focusNode) {
    if (value.length == 1) {
      focusNode.requestFocus();
    }
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
                onPressed: _validateOtpAndLogin,
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
