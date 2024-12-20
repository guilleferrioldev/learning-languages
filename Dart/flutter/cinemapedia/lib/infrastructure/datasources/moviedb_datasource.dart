import 'package:cinemapedia/infrastructure/mappers/movie_mapper.dart';
import 'package:dio/dio.dart';

import 'package:cinemapedia/config/constants/environment.dart';
import 'package:cinemapedia/domain/datasources/movies_datasource.dart';
import 'package:cinemapedia/domain/entities/movie.dart';
import 'package:cinemapedia/infrastructure/models/moviedb/moviedb_response.dart';

class MoviedbDatasource extends MoviesDataSource {
  final _dio = Dio(
      BaseOptions(baseUrl: "https://api.themoviedb.org/3", queryParameters: {
    'api_key': Environment.movieDbKey,
    'language': 'en-US',
  }));

  List<Movie> _jsonToMovie(Map<String, dynamic> json) {
    final movieDbResponse = MovieDbResponse.fromJson(json);

    final List<Movie> movies = movieDbResponse.results
        .where((movieDb) => movieDb.posterPath != 'no-poster')
        .map((movieDb) => MovieMapper.movieFromMovieDb(movieDb))
        .toList();
    return movies;
  }

  @override
  Future<List<Movie>> getNewPlaying({int page = 1}) async {
    final response = await _dio.get(
      "/movie/now_playing",
      queryParameters: {
        'page': page,
      },
    );

    return _jsonToMovie(response.data);
  }

  @override
  Future<List<Movie>> getPopular({int page = 1}) async {
    final response = await _dio.get(
      '/movie/popular',
      queryParameters: {
        'language': 'en-US',
      },
    );

    return _jsonToMovie(response.data);
  }

  @override
  Future<List<Movie>> getTopRated({int page = 1}) async {
    final response = await _dio.get(
      '/movie/top_rated',
      queryParameters: {
        'language': 'en-US',
      },
    );

    return _jsonToMovie(response.data);
  }

  @override
  Future<List<Movie>> getUpcoming({int page = 1}) async {
    final response = await _dio.get(
      '/movie/upcoming',
      queryParameters: {
        'language': 'en-US',
      },
    );

    return _jsonToMovie(response.data);
  }
}
