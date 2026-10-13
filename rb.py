import requests

PLACE_ID = "71895508397153"  # replace with your map's place ID
PING_THRESHOLD = 80    # your "trashole" cutoff in ms

url = f"https://games.roblox.com/v1/games/{PLACE_ID}/servers/Public?&sort=descending&limit=10"

servers = []
cursor = None
while True:
    response = requests.get(url + (f"&cursor={cursor}" if cursor else ""))
    data = response.json()
    for server in data.get("data", []):
        ping = server.get("ping")  # may or may not exist
        ply = server.get("playing")
        print(ping , ply)
        cap = server.get("maxPlayers")
        if ping is not None and ping < PING_THRESHOLD and ply < cap:
            servers.append({
                "id": server["id"],
                "ping": ping,
                "playerCount": ply
            })
    if len(servers) >= 1:
        break
    cursor = data.get("nextPageCursor")
    if not cursor:
        break
servers.sort(key=lambda x: x["playerCount"])
print(servers)
print("Servers under threshold:")
for s in servers:
    print(s)
