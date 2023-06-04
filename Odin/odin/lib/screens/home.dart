import 'package:flutter/material.dart';
import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:intl/intl.dart';
import 'package:odin/styles/app_colors.dart';
import 'package:animations/animations.dart';
import 'package:google_fonts/google_fonts.dart';

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

  final _pageController = PageController(viewportFraction: 0.85);

  void _changeCategory(String newCategory) {
    setState(() {
      _currentCategory = newCategory;
      _newsStream = FirebaseFirestore.instance
          .collection(newCategory)
          .orderBy('date', descending: true)
          .snapshots();
    });
  }

  Widget _buildTopicLabel(String topic) {
    return Container(
      padding: EdgeInsets.symmetric(horizontal: 10, vertical: 5),
      decoration: BoxDecoration(
        color: Colors.blue,
        borderRadius: BorderRadius.circular(20),
        border: Border.all(color: Colors.white, width: 2),
      ),
      child: Text(
        topic,
        style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold),
      ),
    );
  }

  String _getFormattedTopic(String topic) {
    // Map topic to actual topic names
    switch (topic) {
      case 'kpop_stars':
        return 'Kpop';
      case 'nfl_teams':
        return 'NFL Teams';
      case 'soccer_clubs':
        return 'Soccer Clubs';
      case 'nba_teams':
        return 'NBA Teams';
      case 'fashion_brands':
        return 'Fashion Brands';
      case 'famous_anime':
        return 'Famous Anime';
      case 'famous_influencers':
        return 'Famous Influencers';
      case 'disney_characters':
        return 'Disney Characters';
      default:
        // Capitalize other topics
        return topic[0].toUpperCase() + topic.substring(1);
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(
          'Odin News',
          style: GoogleFonts.poppins(
            textStyle: TextStyle(fontSize: 24, fontWeight: FontWeight.w600),
          ),
        ),
        backgroundColor: AppColors.blue,
      ),
      body: SafeArea(
        child: Padding(
          padding: const EdgeInsets.symmetric(vertical: 20.0),
          child: Column(
            children: [
              Container(
                height: 50,
                child: ListView.builder(
                  scrollDirection: Axis.horizontal,
                  itemCount: _categories.length,
                  itemBuilder: (context, index) {
                    return Padding(
                      padding: const EdgeInsets.symmetric(horizontal: 10.0),
                      child: GestureDetector(
                        onTap: () => _changeCategory(_categories[index]),
                        child: AnimatedContainer(
                          duration: Duration(milliseconds: 500),
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
                      ),
                    );
                  },
                ),
              ),
              SizedBox(height: 20.0),
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

                    final articles = snapshot.data!.docs
                        .map((doc) => doc.data()! as Map<String, dynamic>)
                        .toList();

                    articles.sort((a, b) => (b['date'] as int).compareTo(a['date'] as int));

                    return PageView.builder(
                      controller: _pageController,
                      scrollDirection: Axis.vertical,
                      itemCount: articles.length,
                      itemBuilder: (BuildContext context, int index) {
                        Map<String, dynamic> data = articles[index];

                        final dateTime = DateTime.fromMillisecondsSinceEpoch((data['date'] as int) * 1000);
                        final formattedDate = DateFormat.yMMMd().format(dateTime);
                        final formattedTime = DateFormat.jm().format(dateTime);

                        final topic = data['topic'] as String;
                        final formattedTopic = _getFormattedTopic(topic);

                        return OpenContainer(
                          transitionType: ContainerTransitionType.fadeThrough,
                          transitionDuration: Duration(milliseconds: 500),
                          openBuilder: (_, __) => ArticlePage(data),
                          closedBuilder: (_, openContainer) => GestureDetector(
                            onTap: openContainer,
                            child: Card(
                              margin: EdgeInsets.symmetric(vertical: 10),
                              child: ListTile(
                                title: Text(
                                  data['title'],
                                  style: GoogleFonts.poppins(
                                    textStyle: TextStyle(fontSize: 18, fontWeight: FontWeight.w500),
                                  ),
                                ),
                                subtitle: Column(
                                  crossAxisAlignment: CrossAxisAlignment.start,
                                  children: [
                                    SizedBox(height: 5),
                                    _buildTopicLabel(formattedTopic), // Display formatted topic with label outline
                                    SizedBox(height: 5),
                                    Text(
                                      '${formattedDate} ${formattedTime}',
                                      style: GoogleFonts.poppins(
                                        textStyle: TextStyle(fontSize: 14),
                                      ),
                                    ),
                                  ],
                                ),
                                trailing: Icon(Icons.arrow_forward_ios),
                              ),
                            ),
                          ),
                        );
                      },
                    );
                  },
                ),
              ),
            ],
          ),
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
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  data['title'],
                  style: GoogleFonts.poppins(
                    textStyle: TextStyle(color: AppColors.blackshade, fontSize: 24, fontWeight: FontWeight.w600),
                  ),
                ),
                SizedBox(height: 10),
                Text(
                  DateFormat.yMMMd().format(DateTime.fromMillisecondsSinceEpoch((data['date'] as int) * 1000)),
                  style: GoogleFonts.poppins(
                    textStyle: TextStyle(color: AppColors.greyshade, fontSize: 16),
                  ),
                ),
                SizedBox(height: 20),
                Text(
                  data['article'],
                  style: GoogleFonts.poppins(
                    textStyle: TextStyle(color: AppColors.blackshade, fontSize: 18),
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
