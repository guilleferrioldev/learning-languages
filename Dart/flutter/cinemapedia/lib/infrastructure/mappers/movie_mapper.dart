import 'package:cinemapedia/domain/entities/movie.dart';
import 'package:cinemapedia/infrastructure/models/moviedb/movie_moviedb.dart';

class MovieMapper {
  static Movie movieFromMovieDb(MovieFromMovieDb movieFromMovieDb) {
    return Movie(
      adult: movieFromMovieDb.adult,
      backdropPath: (movieFromMovieDb.backdropPath != '')
          ? 'https://image.tmdb.org/t/p/original${movieFromMovieDb.backdropPath}'
          : 'https://ih1.redbubble.net/image.4905811447.8675/flat,750x,075,f-pad,750x1000,f8f8f8.jpg',
      genreIds: movieFromMovieDb.genreIds.map((e) => e.toString()).toList(),
      id: movieFromMovieDb.id,
      originalLanguage: movieFromMovieDb.originalLanguage,
      originalTitle: movieFromMovieDb.originalTitle,
      overview: movieFromMovieDb.overview,
      popularity: movieFromMovieDb.popularity,
      posterPath: (movieFromMovieDb.posterPath != '')
          ? 'https://image.tmdb.org/t/p/original${movieFromMovieDb.posterPath}'
          : 'no-poster',
      releaseDate: movieFromMovieDb.releaseDate,
      title: movieFromMovieDb.title,
      video: movieFromMovieDb.video,
      voteAverage: movieFromMovieDb.voteAverage,
      voteCount: movieFromMovieDb.voteCount,
    );
  }
}
