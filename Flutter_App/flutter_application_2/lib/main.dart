import 'package:flutter/material.dart';

void main() { 
  runApp(const MyApp());
  }

class MyApp extends StatelessWidget {
  const MyApp ({super.key});

  @override
  Widget build(BuildContext context) {
    // const title = "목록";
    String text = "Hi";

    return Text(text);

    // return MaterialApp(title: title,
    //   home: Scaffold(
    //     appBar: AppBar(
    //       title: const Text(title)),
    //       body: ListView(children: const <Widget>
    //       [
    //         ListTile(leading: Icon(Icons.map), title: Text("지도")),
    //         ListTile(leading: Icon(Icons.photo_album), title: Text("앨범")),
    //         ListTile(leading: Icon(Icons.phone), title: Text("전화"))
    //       ]
    //     )
    //   )
    // );
  }
}