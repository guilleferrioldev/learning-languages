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
}
