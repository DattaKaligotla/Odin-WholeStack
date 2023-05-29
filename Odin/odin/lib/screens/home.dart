import 'package:flutter/material.dart';
import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:intl/intl.dart';
import 'package:odin/styles/app_colors.dart';
import 'package:animations/animations.dart';

class HomePage extends StatefulWidget {
  const HomePage({Key? key}) : super(key: key);

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  final List<String> _categories = ['entertainment', 'financial', 'poli', 'sports', 'tech', 'world'];
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
                      duration: Duration(milliseconds: 500),
                      margin: EdgeInsets.symmetric(horizontal: 10),
                      padding: EdgeInsets.symmetric(horizontal: 20, vertical: 10),
                      decoration: BoxDecoration(
                        color: _currentCategory == _categories[index] ? AppColors.blue : AppColors.whiteshade,
                        borderRadius: BorderRadius.circular(20),
                        boxShadow: [
                          BoxShadow(
                            color: _currentCategory == _categories[index] ? Colors.blue.withOpacity(0.5) : Colors.grey.withOpacity(0.5),
                            spreadRadius: 2,
                            blurRadius: 3,
                            offset: Offset(0, 3),
                          ),
                        ],
                      ),
                      child: Text(
                        _categories[index].toUpperCase(),
                        style: TextStyle(color: _currentCategory == _categories[index] ? Colors.white : AppColors.blackshade, fontWeight: FontWeight.bold),
                      ),
                    ),
                  );
                },
              ),
            ),
            Expanded(
              child: StreamBuilder<QuerySnapshot>(
                stream: _newsStream,
                builder: (BuildContext context, AsyncSnapshot<QuerySnapshot> snapshot) {
                  if (snapshot.hasError) {
                    return Text('Something went wrong');
                  }

                  if (snapshot.connectionState == ConnectionState.waiting) {
                    return CircularProgressIndicator();
                  }

                  return PageTransitionSwitcher(
                    duration: const Duration(milliseconds: 800),
                    reverse: false,
                    transitionBuilder: (
                      Widget child,
                      Animation<double> animation,
                      Animation<double> secondaryAnimation,
                    ) {
                      return SharedAxisTransition(
                        child: child,
                        animation: animation,
                        secondaryAnimation: secondaryAnimation,
                        transitionType: SharedAxisTransitionType.vertical,
                      );
                    },
                    child: ListView.builder(
                      itemCount: snapshot.data!.docs.length,
                      itemBuilder: (BuildContext context, int index) {
                        Map<String, dynamic> data = snapshot.data!.docs[index].data() as Map<String, dynamic>;
                        return OpenContainer(
                          closedElevation: 3.0,
                          closedShape: RoundedRectangleBorder(
                            borderRadius: BorderRadius.circular(10),
                          ),
                          closedColor: AppColors.whiteshade,
                          transitionDuration: Duration(milliseconds: 600),
                          transitionType: ContainerTransitionType.fadeThrough,
                          openBuilder: (_, __) => ArticlePage(data),
                          closedBuilder: (_, __) {
                            return ListTile(
                              title: Text(data['title']),
                              subtitle: Text(DateFormat.yMMMd().format(DateTime.fromMillisecondsSinceEpoch(data['date']))),
                              trailing: Icon(Icons.arrow_forward_ios),
                            );
                          },
                        );
                      },
                    ),
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

class ArticlePage extends StatelessWidget {
  final Map<String, dynamic> data;

  ArticlePage(this.data);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(data['title']),
        backgroundColor: AppColors.blue,
      ),
      body: SafeArea(
        child: Padding(
          padding: EdgeInsets.all(16.0),
          child: SingleChildScrollView(
            child: Hero(
              tag: 'article-${data['id']}',
              child: Material(
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(
                      data['title'],
                      style: TextStyle(color: AppColors.blackshade, fontSize: 24, fontWeight: FontWeight.bold),
                    ),
                    SizedBox(height: 10),
                    Text(
                      DateFormat.yMMMd().format(DateTime.fromMillisecondsSinceEpoch(data['date'])),
                      style: TextStyle(color: AppColors.grayshade, fontSize: 16),
                    ),
                    SizedBox(height: 20),
                    Text(
                      data['article'],
                      style: TextStyle(color: AppColors.blackshade, fontSize: 18),
                    ),
                  ],
                ),
              ),
            ),
          ),
        ),
      ),
    );
  }
}
