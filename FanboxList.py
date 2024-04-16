import json

# JSONファイルをUTF-8エンコーディングで読み込む
with open('fanbox.json', encoding='utf-8') as f:
    data = json.load(f)

# ステータスごとに名前を格納するための辞書を初期化
status_names = {"ELITE": [], "VIP": [], "Member": []}

# データをステータスごとに分類
for user_id, user_data in data.items():
    status = user_data["status"]
    name = user_data["name"]
    status_names[status].append(name)

# ステータスごとに名前を表示
for status, names in status_names.items():
    color = ""
    if status == "ELITE":
        color = "<color='blue'>"
    elif status == "VIP":
        color = "<color='yellow'>"
    elif status == "Member":
        color = "<color='red'>"
    print(f"{color}{status}</color>")
    print(", ".join(names))
    print()
