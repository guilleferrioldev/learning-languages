import 'package:cinemapedia/domain/entities/movie.dart';
import 'package:cinemapedia/infrastructure/models/moviedb/movie_details.dart';
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
          : 'https://www.movienewz.com/img/films/poster-holder.jpg',
      releaseDate: movieFromMovieDb.releaseDate,
      title: movieFromMovieDb.title,
      video: movieFromMovieDb.video,
      voteAverage: movieFromMovieDb.voteAverage,
      voteCount: movieFromMovieDb.voteCount,
    );
  }

  static Movie movieFromMovieDetails(MovieDetails movieDetails) {
    return Movie(
      adult: movieDetails.adult,
      backdropPath: (movieDetails.backdropPath != '')
          ? 'https://image.tmdb.org/t/p/original${movieDetails.backdropPath}'
          : 'https://ih1.redbubble.net/image.4905811447.8675/flat,750x,075,f-pad,750x1000,f8f8f8.jpg',
      genreIds: movieDetails.genres.map((e) => e.name).toList(),
      id: movieDetails.id,
      originalLanguage: movieDetails.originalLanguage,
      originalTitle: movieDetails.originalTitle,
      overview: movieDetails.overview,
      popularity: movieDetails.popularity,
      posterPath: (movieDetails.posterPath != '')
          ? 'https://image.tmdb.org/t/p/original${movieDetails.posterPath}'
          : 'no-poster',
      releaseDate: movieDetails.releaseDate,
      title: movieDetails.title,
      video: movieDetails.video,
      voteAverage: movieDetails.voteAverage,
      voteCount: movieDetails.voteCount,
    );
  }
}
