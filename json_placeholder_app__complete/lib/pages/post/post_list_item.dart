



import 'package:flutter/material.dart';

import '../../models/post.dart';

// элемент списка
class PostListItem extends StatelessWidget {

  final Post post;

  PostListItem(this.post);

  Widget build(BuildContext context) {
    return Container(
        decoration: BoxDecoration(
            borderRadius: BorderRadius.all(Radius.circular(10)),
            border: Border.all(color: Colors.brown.withOpacity(0.5), width: 0.3)
        ),
        margin: EdgeInsets.only(bottom: 10),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            Container(
              decoration: BoxDecoration(
                borderRadius: BorderRadius.only(topLeft: Radius.circular(15), topRight: Radius.circular(15)),
                color: Theme.of(context).primaryColor,
              ),
              padding: EdgeInsets.all(10),
              child: Text(
                post.title!,
                textAlign: TextAlign.left,
                style: Theme.of(context).textTheme.headline6!.copyWith(color: Colors.white),),
            ),
            Container(
              child: Text(
                post.body!,
                style: Theme.of(context).textTheme.bodyText2,
              ),
              padding: EdgeInsets.all(10),
            ),
          ],
        )
    );
  }
}