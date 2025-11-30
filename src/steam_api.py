import requests
import pandas as pd
import time
import re

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

def get_steam_id_by_name(name):
    try:
        query = name.replace(" ", "%20")
        url = f"https://steamcommunity.com/actions/SearchApps/{query}"
        data = requests.get(url).json()

        if len(data) == 0:
            return None

        return data[0]["appid"]
    except:
        return None


rawg_df["steam_id"] = rawg_df["name"].apply(get_steam_id_by_name)
rawg_df = rawg_df.dropna(subset=["steam_id"])
rawg_df["steam_id"] = rawg_df["steam_id"].astype(int)

def get_steam_store_data(appid):
    url = f"https://store.steampowered.com/api/appdetails?appids={appid}"
    data = requests.get(url).json()

    if not data.get(str(appid), {}).get("success"):
        return None

    d = data[str(appid)]["data"]

    tags = d.get("categories", [])
    tag_names = [t["description"] for t in tags]

    return {
        "appid": appid,
        "steam_name": d.get("name"),
        "is_free": d.get("is_free"),
        "price": d.get("price_overview", {}).get("final", None),
        "metacritic_score": d.get("metacritic", {}).get("score"),
        "tags": ", ".join(tag_names),
        "has_great_soundtrack": 1 if "Great Soundtrack" in tag_names else 0
    }


steam_data = []

for appid in rawg_df["steam_id"]:
    d = get_steam_store_data(appid)
    if d:
        steam_data.append(d)
    time.sleep(0.2)

steam_df = pd.DataFrame(steam_data)

def get_tags_from_steamspy(appid):
    try:
        url = f"https://steamspy.com/api.php?request=appdetails&appid={appid}"
        data = requests.get(url).json()

        if "tags" not in data:
            return {
                "great": 0,
                "story": 0,
                "atmo": 0
            }

        tags = [t.lower() for t in data["tags"].keys()]

        return {
            "great": 1 if "great soundtrack" in tags else 0,
            "story": 1 if "story rich" in tags else 0,
            "atmo": 1 if "atmospheric" in tags else 0
        }

    except:
        return {
            "great": 0,
            "story": 0,
            "atmo": 0
        }



results = df["appid"].apply(get_tags_from_steamspy)

df["has_great_soundtrack"] = results.apply(lambda x: x["great"])
df["has_story_rich"]      = results.apply(lambda x: x["story"])
df["has_atmospheric"]     = results.apply(lambda x: x["atmo"])

df.to_csv("final_games_extended.csv", index=False)

df.head()
