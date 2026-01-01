import requests
import pandas as pd
import time
import re

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


def get_steam_store_data(appid):
    try:
        url = f"https://store.steampowered.com/api/appdetails?appids={appid}"
        data = requests.get(url).json()

        if not data.get(str(appid), {}).get("success"):
            return None

        d = data[str(appid)]["data"]
        categories = d.get("categories", [])
        tags = [c["description"] for c in categories]

        return {
            "appid": appid,
            "steam_name": d.get("name"),
            "is_free": d.get("is_free"),
            "price": d.get("price_overview", {}).get("final"),
            "metacritic_score": d.get("metacritic", {}).get("score"),
            "tags": tags,
        }
    except:
        return None


def get_tags_from_steamspy(appid):
    try:
        url = f"https://steamspy.com/api.php?request=appdetails&appid={appid}"
        data = requests.get(url).json()

        if "tags" not in data:
            return {"great": 0, "story": 0, "atmo": 0}

        tags = [t.lower() for t in data["tags"].keys()]

        return {
            "great": int("great soundtrack" in tags),
            "story": int("story rich" in tags),
            "atmo": int("atmospheric" in tags),
        }
    except:
        return {"great": 0, "story": 0, "atmo": 0}
