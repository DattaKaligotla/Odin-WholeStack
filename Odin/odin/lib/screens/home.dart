import 'package:flutter/material.dart';
import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:intl/intl.dart';
import 'package:odin/styles/app_colors.dart';

class HomePage extends StatefulWidget {
  const HomePage({Key? key}) : super(key: key);

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  final List<String> _categories = ['entertainment', 'financial', 'poli', 'sports', 'tech', 'world'];
  final Map<String, Color> _categoryColors = {
    'entertainment': Colors.grey[700]!,
    'financial': Colors.grey[600]!,
    'poli': Colors.grey[500]!,
    'sports': Colors.grey[400]!,
    'tech': Colors.grey[300]!,
    'world': Colors.grey[200]!,
  };
  String _currentCategory = 'entertainment';
  Stream<QuerySnapshot> _newsStream = FirebaseFirestore.instance
      .collection('entertainment')
      .orderBy('date', descending: true)
      .snapshots();

  void _changeCategory(String newCategory) {
    setState(() {
      _currentCategory = newCategory;
      _newsStream = FirebaseFirestore.instance
          .collection(newCategory)
          .orderBy('date', descending: true)
          .snapshots();
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Odin News'),
        backgroundColor: AppColors.blue,
      ),
      body: SafeArea(
        child: Column(
          children: [
            Container(
              height: 50,
              child: ListView.builder(
                scrollDirection: Axis.horizontal,
                itemCount: _categories.length,
                itemBuilder: (context, index) {
                  return GestureDetector(
                    onTap: () => _changeCategory(_categories[index]),
                    child: AnimatedContainer(
                      duration: Duration(milliseconds: 200),
                      margin: EdgeInsets.symmetric(horizontal: 10),
                      padding: EdgeInsets.symmetric(horizontal: 20, vertical: 10),
                      decoration: BoxDecoration(
                        gradient: LinearGradient(colors: [_categoryColors[_categories[index]]!, _categoryColors[_categories[index]]!.withOpacity(0.6)]),
                        borderRadius: BorderRadius.circular(20),
                      ),
                      child: Text(
                        _categories[index].toUpperCase(),
                        style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold),
                      ),
                    ),
                  );
                },
              ),
            ),
            Expanded(
              child: StreamBuilder<QuerySnapshot>(
                stream: _newsStream,
                builder: (BuildContext context, AsyncSnapshot<QuerySnapshot> snapshot)
{
                  if (snapshot.hasError) {
                    return Text('Something went wrong');
                  }

                  if (snapshot.connectionState == ConnectionState.waiting) {
                    return CircularProgressIndicator();
                  }

                  return ListView.builder(
                    itemCount: snapshot.data!.docs.length,
                    itemBuilder: (BuildContext context, int index) {
                      Map<String, dynamic> data = snapshot.data!.docs[index].data()! as Map<String, dynamic>;
                      return ExpansionTile(
                        title: Text(
                          data['title'],
                          style: TextStyle(fontWeight: FontWeight.bold, fontSize: 24),
                        ),
                        children: [
                          SingleChildScrollView( // Added this
                            child: Padding(
                              padding: const EdgeInsets.symmetric(horizontal: 16.0),
                              child: Column(
                                crossAxisAlignment: CrossAxisAlignment.start,
                                children: [
                                  Text(
                                    data['topic'],
                                    style: TextStyle(color: Colors.grey, fontSize: 20),
                                  ),
                                  SizedBox(height: 10),
                                  Text(
                                    DateFormat.yMMMd().format(DateTime.fromMillisecondsSinceEpoch(data['date'])),
                                    style: TextStyle(color: Colors.grey, fontSize: 18),
                                  ),
                                  SizedBox(height: 20),
                                  Text(
                                    data['article'],
                                    style: TextStyle(fontSize: 18),
                                  ),
                                  SizedBox(height: 20),
                                  Container(
                                    width: double.infinity,
                                    child: ElevatedButton(
                                      style: ButtonStyle(
                                        backgroundColor: MaterialStateProperty.all(Colors.grey[800]),
                                      ),
                                      onPressed: () {}, // Add appropriate functionality for the button here
                                      child: Text('Read More'),
                                    ),
                                  ),
                                  SizedBox(height: 20),
                                ],
                              ),
                            ),
                          ),
                        ],
                      );
                    },
                  );

                },
              ),
            ),
          ],
        ),
      ),
    );
  }
}
