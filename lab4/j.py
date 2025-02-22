import json

# Открываем и загружаем JSON-файл
with open("sample-data.json", "r") as file:
    data = json.load(file)

# Заголовок
print("Interface Status")
print("=" * 80)
print(f"{'DN':<50} {'Description':<20} {'Speed':<7} {'MTU':<6}")
print("-" * 80)

# Обрабатываем каждый интерфейс
for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    descr = attributes["descr"] if attributes["descr"] else ""
    speed = attributes["speed"]
    mtu = attributes["mtu"]

    # Выводим в требуемом формате
    print(f"{dn:<50} {descr:<20} {speed:<7} {mtu:<6}")
