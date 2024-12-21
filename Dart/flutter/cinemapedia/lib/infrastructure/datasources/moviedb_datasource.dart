import 'package:cinemapedia/infrastructure/mappers/movie_mapper.dart';
import 'package:cinemapedia/infrastructure/models/moviedb/movie_details.dart';
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
    try {
      final response = await _dio.get(
        "/movie/now_playing",
        queryParameters: {
          'page': page,
        },
      );

      return _jsonToMovie(response.data);
    } catch (error) {
      return [];
    }
  }

  @override
  Future<List<Movie>> getPopular({int page = 1}) async {
    try {
      final response = await _dio.get(
        '/movie/popular',
        queryParameters: {
          'page': page,
        },
      );

      return _jsonToMovie(response.data);
    } catch (error) {
      return [];
    }
  }

  @override
  Future<List<Movie>> getTopRated({int page = 1}) async {
    try {
      final response = await _dio.get(
        '/movie/top_rated',
        queryParameters: {
          'page': page,
        },
      );

      return _jsonToMovie(response.data);
    } catch (error) {
      return [];
    }
  }

  @override
  Future<List<Movie>> getUpcoming({int page = 1}) async {
    try {
      final response = await _dio.get(
        '/movie/upcoming',
        queryParameters: {
          'page': page,
        },
      );

      return _jsonToMovie(response.data);
    } catch (error) {
      return [];
    }
  }

  @override
  Future<Movie> getMovieById(String id) async {
    try {
      final response = await _dio.get(
        "/movie/$id",
      );

      if (response.statusCode != 200) {
        throw Exception('Error getting movie by id');
      }

      final movieDetails = MovieDetails.fromJson(response.data);

      return MovieMapper.movieFromMovieDetails(movieDetails);
    } catch (error) {
      throw Exception('Error getting movie by id');
    }
  }

  @override
  Future<List<Movie>> searchMovies(String query, {int page = 1}) async {
    try {
      if (query.isEmpty) return [];

      final response = await _dio.get(
        '/search/movie',
        queryParameters: {
          'query': query,
          'page': page,
        },
      );

      return _jsonToMovie(response.data);
    } catch (error) {
      return [];
    }
  }
}
