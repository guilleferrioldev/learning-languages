import 'package:cinemapedia/domain/entities/actor.dart';
import 'package:cinemapedia/infrastructure/models/moviedb/credits_response.dart';

class ActorMapper {
  static Actor actorFromCreditsResponse(Cast cast) {
    return Actor(
      id: cast.id,
      name: cast.name,
      profilePath: cast.profilePath != null
          ? 'https://image.tmdb.org/t/p/original${cast.profilePath}'
          : 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSNnXQRA1v4fRDDiE9qTJZFPOXw0UJFCKM_LA&s',
      character: cast.character,
    );
  }
}
