import 'package:cinemapedia/domain/entities/movie.dart';
import 'package:cinemapedia/presentation/providers/provider.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

final movieInfoProvider =
    StateNotifierProvider<MovieMapNotifier, Map<String, Movie>>((ref) {
  final getMovie = ref.watch(moviesRepositoryProvider).getMovieById;
  return MovieMapNotifier(getMovie: getMovie);
});

typedef GetMovieCallback = Future<Movie> Function(String id);

class MovieMapNotifier extends StateNotifier<Map<String, Movie>> {
  final GetMovieCallback getMovie;
  MovieMapNotifier({
    required this.getMovie,
  }) : super({});

  Future<void> loadMovie(String id) async {
    if (state.containsKey(id)) return;
    final movie = await getMovie(id);
    state = {...state, id: movie};
  }
}
