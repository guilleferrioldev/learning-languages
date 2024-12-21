import 'package:cinemapedia/domain/repositories/actor_repository.dart';
import 'package:cinemapedia/infrastructure/datasources/actor_datasource.dart';
import 'package:cinemapedia/infrastructure/repositories/actor_repository_implementation.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

final actorsRepositoryProvider = Provider<ActorsRepository>(
    (ref) => ActorsRepositoryImplementation(ActorsDatasource()));
