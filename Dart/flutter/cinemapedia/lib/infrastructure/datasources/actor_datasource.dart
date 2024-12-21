import 'package:cinemapedia/config/constants/environment.dart';
import 'package:cinemapedia/domain/datasources/actor_datasource.dart';
import 'package:cinemapedia/domain/entities/actor.dart';
import 'package:cinemapedia/infrastructure/mappers/actor_mapper.dart';
import 'package:cinemapedia/infrastructure/models/moviedb/credits_response.dart';
import 'package:dio/dio.dart';

class ActorsDatasource extends ActorsDataSource {
  final _dio = Dio(
      BaseOptions(baseUrl: "https://api.themoviedb.org/3", queryParameters: {
    'api_key': Environment.movieDbKey,
    'language': 'en-US',
  }));

  List<Actor> _jsonToActor(List<Cast> cast) {
    List<Actor> actors =
        cast.map((cast) => ActorMapper.actorFromCreditsResponse(cast)).toList();
    return actors;
  }

  @override
  Future<List<Actor>> getActorsByMovieId(String movieId) async {
    try {
      final response = await _dio.get(
        "/movie/$movieId/credits",
      );

      final castResponse = CastResponse.fromJson(response.data);
      return _jsonToActor(castResponse.cast);
    } catch (error) {
      return [];
    }
  }
}
