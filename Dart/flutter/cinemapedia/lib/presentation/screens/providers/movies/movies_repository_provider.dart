import 'package:flutter_riverpod/flutter_riverpod.dart';

import 'package:cinemapedia/infrastructure/datasources/moviedb_datasource.dart';
import 'package:cinemapedia/domain/repositories/movies_repository.dart';
import 'package:cinemapedia/infrastructure/repositories/movies_repository_implementation.dart';

final moviesRepositoryProvider = Provider<MoviesRepository>(
    (ref) => MoviesRepositoryImplementation(MoviedbDatasource()));
