from fastapi import FastAPI, HTTPException, Path, Query
from models import GenreURLChoices, BandBase, BandCreate, BandWithId
import uvicorn
from typing import Annotated

app = FastAPI()

BANDS = [
    {'id': 1, 'name': 'The Kinks', 'genre': 'Rock'},
    {'id': 2, 'name': 'Aphex Twin', 'genre': 'Electronic'},
    {'id': 3, 'name': 'Black Sabbath', 'genre': 'Metal', 'albums': [
        {'title': 'Master of Reality', 'released_date': '1971-07-21'}
    ]},
    {'id': 4, 'name': 'Wa-Tang Clan', 'genre': 'Hip_hop'}
]

@app.get('/bands')
async def get_bands(
    genre: GenreURLChoices | None = None,
    q: Annotated[str | None, Query(max_length=10)] = None,
) -> list[BandWithId]:
    band_list = [BandWithId(**b) for b in BANDS]

    if genre:
        band_list = [b for b in band_list if b.genre.value.lower() == genre.value]

    if q:
        band_list = [
            b for b in band_list if q.lower() in b.name.lower()
        ]


    return band_list

@app.get('/bands/{band_id}')
async def get_band_from_id(band_id: Annotated[int, Path(title="The band ID")]) -> BandWithId:
    band = next((BandWithId(**b) for b in BANDS if b['id'] == band_id), None)
    if band is None:
        raise HTTPException(status_code=404, detail="Band not found")
    return band

@app.post("/bands")
async def create_bands(band_data: BandCreate) -> BandWithId:
    id = BANDS[-1]['id'] + 1
    band = (BandWithId(id=id, **band_data.model_dump())).model_dump()
    BANDS.append(band)
    return band

try:
    uvicorn.run(app, host="127.0.0.1", port=8000)
except KeyboardInterrupt:
    print("Se ha interrumpido la ejecución del programa.")