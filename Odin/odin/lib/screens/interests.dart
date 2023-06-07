import 'package:flutter/material.dart';
import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:get/get.dart';
import 'package:odin/styles/app_colors.dart';
import 'package:odin/screens/home.dart';

class InterestsScreen extends StatefulWidget {
  final String uid;

  InterestsScreen({required this.uid});

  @override
  _InterestsScreenState createState() => _InterestsScreenState();
}

class _InterestsScreenState extends State<InterestsScreen> {
  final List<String> _interests = ['baseball', 'superheroes', 'rappers', 'pop', 'kpop', 'nfl', 'soccer', 'nba', 'fashion', 'anime', 'disney', 'celebrities'];
  final List<bool> _selectedInterests = List.generate(12, (index) => false);

  void saveInterests() async {
    List<String> selectedInterests = [];
    for (int i = 0; i < _interests.length; i++) {
      if (_selectedInterests[i]) {
        selectedInterests.add(_interests[i]);
      }
    }

    // Create a user document in Firestore with the selected interests
    await FirebaseFirestore.instance.collection('users').doc(widget.uid).set({
      'interests': selectedInterests,
    });

    Get.offAll(() => HomePage());
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Choose Interests'),
        backgroundColor: AppColors.blue,
      ),
      body: Padding(
        padding: EdgeInsets.all(8), // reduced padding
        child: Column(
          children: <Widget>[
            Expanded(
              child: GridView.count(
                crossAxisCount: 3, // increased crossAxisCount
                crossAxisSpacing: 4, // reduced spacing
                mainAxisSpacing: 2, // further reduced main axis spacing
                children: List.generate(_interests.length, (index) {
                  return FilterChip(
                    label: Text(_interests[index]),
                    selected: _selectedInterests[index],
                    onSelected: (bool value) {
                      setState(() {
                        _selectedInterests[index] = value;
                      });
                    },
                    labelStyle: TextStyle(
                      color: _selectedInterests[index] ? Colors.white : Colors.black,
                    ),
                    selectedColor: AppColors.blue,
                  );
                }),
              ),
            ),
            ElevatedButton(
              onPressed: saveInterests,
              style: ElevatedButton.styleFrom(
                primary: AppColors.blue,
                shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(15),
                ),
                padding: EdgeInsets.all(15),
              ),
              child: Text('Submit'),
            ),
          ],
        ),
      ),
    );
  }
}
