import 'package:cinemapedia/domain/datasources/movies_datasource.dart';
import 'package:cinemapedia/domain/entities/movie.dart';
import 'package:cinemapedia/domain/repositories/movies_repository.dart';

class MoviesRepositoryImplementation extends MoviesRepository {
  final MoviesDataSource datasource;
  MoviesRepositoryImplementation(this.datasource);

  @override
  Future<List<Movie>> getNewPlaying({int page = 1}) async {
    return datasource.getNewPlaying(page: page);
  }

  @override
  Future<List<Movie>> getPopular({int page = 1}) async {
    return datasource.getPopular(page: page);
  }

  @override
  Future<List<Movie>> getTopRated({int page = 1}) async {
    return datasource.getTopRated(page: page);
  }

  @override
  Future<List<Movie>> getUpcoming({int page = 1}) async {
    return datasource.getUpcoming(page: page);
  }
}
