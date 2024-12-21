import 'package:animate_do/animate_do.dart';
import 'package:cinemapedia/config/helpers/helpers.dart';
import 'package:cinemapedia/domain/entities/movie.dart';
import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';

class MoviesHorizontalListview extends StatefulWidget {
  final List<Movie> movies;
  final String? title;
  final String? subTitle;
  final VoidCallback? loadNextPage;

  const MoviesHorizontalListview(
      {super.key,
      required this.movies,
      this.title,
      this.subTitle,
      this.loadNextPage});

  @override
  State<MoviesHorizontalListview> createState() =>
      _MoviesHorizontalListviewState();
}

class _MoviesHorizontalListviewState extends State<MoviesHorizontalListview> {
  final ScrollController _scrollController = ScrollController();

  @override
  void initState() {
    super.initState();

    _scrollController.addListener(() {
      if (widget.loadNextPage == null) return;

      if ((_scrollController.position.pixels + 200) >=
          _scrollController.position.maxScrollExtent) {
        widget.loadNextPage!();
      }
    });
  }

  @override
  void dispose() {
    super.dispose();
    _scrollController.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return SizedBox(
        height: 350,
        child: Column(children: [
          if (widget.title != null)
            _Title(title: widget.title, subTitle: widget.subTitle),
          Expanded(
              child: ListView.builder(
            controller: _scrollController,
            itemCount: widget.movies.length,
            scrollDirection: Axis.horizontal,
            physics: const BouncingScrollPhysics(),
            itemBuilder: (context, index) {
              return FadeInRight(
                child: _Slide(
                  movie: widget.movies[index],
                ),
              );
            },
          ))
        ]));
  }
}

class _Title extends StatelessWidget {
  final String? title;
  final String? subTitle;
  const _Title({this.title, this.subTitle});

  @override
  Widget build(BuildContext context) {
    final titleStyle = Theme.of(context).textTheme.titleLarge;

    return Container(
        padding: const EdgeInsets.only(top: 10),
        margin: const EdgeInsets.symmetric(horizontal: 10),
        child: Row(
          children: [
            if (title != null)
              Text(
                title!,
                style: titleStyle,
              ),
            const Spacer(),
            if (subTitle != null)
              FilledButton.tonal(
                  style:
                      const ButtonStyle(visualDensity: VisualDensity.compact),
                  onPressed: () {},
                  child: Text(subTitle!))
          ],
        ));
  }
}

class _Slide extends StatelessWidget {
  final Movie movie;
  const _Slide({required this.movie});

  @override
  Widget build(BuildContext context) {
    final titleStyle = Theme.of(context).textTheme;

    return Container(
      margin: const EdgeInsets.symmetric(horizontal: 8),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          //*Image
          SizedBox(
            width: 150,
            child: ClipRRect(
                borderRadius: BorderRadius.circular(20),
                // TODO: Add image loading
                child: Center(
                  child: ElevatedButton(
                      onPressed: () {
                        context.push('/movie/${movie.id}');
                      },
                      child: const Text("Tap to see more")),
                )),
          ),

          const SizedBox(height: 5),

          //*Title
          SizedBox(
              width: 150,
              child: Text(
                movie.title,
                style: titleStyle.titleSmall,
              )),

          //*Rating
          SizedBox(
            width: 150,
            child: Row(
              children: [
                Icon(Icons.star_half_outlined, color: Colors.yellow.shade800),
                const SizedBox(width: 3),
                Text(movie.voteAverage.toStringAsFixed(1),
                    style: titleStyle.bodyMedium
                        ?.copyWith(color: Colors.yellow.shade800)),
                const Spacer(),
                Text(HumanFormats.number(movie.popularity),
                    style: titleStyle.bodySmall)
              ],
            ),
          )
        ],
      ),
    );
  }
}

// Image.network(movie.posterPath, width: 150, fit: BoxFit.cover,
//                       loadingBuilder: (context, child, loadingProgress) {
//                 if (loadingProgress != null) {
//                   return const Padding(
//                     padding: EdgeInsets.all(8.0),
//                     child: Center(
//                       child: CircularProgressIndicator(
//                         strokeWidth: 2,
//                       ),
//                     ),
//                   );
//                 }

//                 return FadeIn(child: child);