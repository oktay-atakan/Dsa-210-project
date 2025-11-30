import requests
import pandas as pd

def get_rawg_data(api_key, pages=5):
    games = []
    for page in range(1, pages + 1):
        url = f"https://api.rawg.io/api/games?key={api_key}&dates=2015-01-01,2024-12-31&page={page}"
        resp = requests.get(url).json()

        for g in resp["results"]:
            games.append({
                "id": g["id"],
                "name": g["name"],
                "released": g["released"],
                "metacritic": g.get("metacritic"),
                "rating": g["rating"],
                "ratings_count": g["ratings_count"],
                "genres": ", ".join([x["name"] for x in g["genres"]])
            })
    return pd.DataFrame(games)
