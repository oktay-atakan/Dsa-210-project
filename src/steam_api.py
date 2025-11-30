import requests
import pandas as pd

def get_steam_data(appid_list):
    results = []
    for appid in appid_list:
        try:
            url = f"https://store.steampowered.com/api/appdetails?appids={appid}"
            data = requests.get(url).json()
            info = data[str(appid)]["data"]
            genres = info.get("genres", [])
            tags = [g["description"] for g in genres]
            has_great = "Great Soundtrack" in tags

            results.append({
                "steam_appid": appid,
                "has_great_soundtrack": has_great,
                "price": info.get("price_overview", {}).get("final_formatted"),
                "metacritic_score": info.get("metacritic", {}).get("score"),
                "tags": tags
            })
        except:
            continue
    return pd.DataFrame(results)
