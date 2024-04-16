import json

# JSONデータ
json_data = '''
'''

# JSONデータを辞書に変換
data = json.loads(json_data)

# ステータスごとに名前を格納するための辞書を初期化
status_names = {"Member": [], "VIP": [], "ELITE": []}

# データをステータスごとに分類
for user_id, user_data in data.items():
    status = user_data["status"]
    name = user_data["name"]
    status_names[status].append(name)

# ステータスごとに名前を表示
for status, names in status_names.items():
    print(f"{status}: ", end="")
    print(", ".join(names))
    print()
