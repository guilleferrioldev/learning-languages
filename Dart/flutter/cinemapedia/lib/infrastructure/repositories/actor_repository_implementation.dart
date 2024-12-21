import 'package:cinemapedia/domain/datasources/actor_datasource.dart';
import 'package:cinemapedia/domain/entities/actor.dart';
import 'package:cinemapedia/domain/repositories/actor_repository.dart';

class ActorsRepositoryImplementation extends ActorsRepository {
  final ActorsDataSource datasource;
  ActorsRepositoryImplementation(this.datasource);

  @override
  Future<List<Actor>> getActorsByMovieId(String movieId) async {
    return datasource.getActorsByMovieId(movieId);
  }
}
