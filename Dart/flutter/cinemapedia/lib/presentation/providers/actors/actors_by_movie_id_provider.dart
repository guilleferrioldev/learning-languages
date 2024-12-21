import 'package:cinemapedia/domain/entities/actor.dart';
import 'package:cinemapedia/presentation/providers/actors/actors_repository_provider.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

final actorsByMovieIdProvider =
    StateNotifierProvider<ActorsByMovieMapNotifier, Map<String, List<Actor>>>(
        (ref) {
  final getActorsByMovieId =
      ref.watch(actorsRepositoryProvider).getActorsByMovieId;
  return ActorsByMovieMapNotifier(getActors: getActorsByMovieId);
});

typedef GetActorsCallback = Future<List<Actor>> Function(String id);

class ActorsByMovieMapNotifier extends StateNotifier<Map<String, List<Actor>>> {
  final GetActorsCallback getActors;
  ActorsByMovieMapNotifier({
    required this.getActors,
  }) : super({});

  Future<void> loadActors(String id) async {
    if (state.containsKey(id)) return;
    final List<Actor> actors = await getActors(id);
    state = {...state, id: actors};
  }
}
