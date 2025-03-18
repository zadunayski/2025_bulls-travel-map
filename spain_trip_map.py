#!/usr/bin/env python
# coding: utf-8

# In[11]:


import folium

# Определяем словарь locations с данными о маршруте
locations = {
    "Барселона": {
        "coords": [41.3851, 2.1734],
        "days": 0,
        "departure_day": 1,
        "departure_time": "до полудня",
        "arrival_day": 11,
        "arrival_time": "днём",
        "budget": 0,
        "transport": """
        🚄 Поезд в Сан-Себастьян (€50–€100) в 0-й день.<br>
        🛫 Прилетаем из Лиссабона на 11-й день путешествия.
        """
    },
    "Сан-Себастьян": {
        "coords": [43.3208, -1.9822],
        "days": 2,
        "arrival_day": 1,
        "arrival_time": "днём",
        "departure_day": 3,
        "departure_time": "до 11 утра",
        "activities": [
            "🍽️ Гастрономический тур по пинчос-барам.",
            "🏖️ Пляж Ла-Конча.",
            "🌅 Прогулка по набережной.",
            "🚶 Хайк на гору Ургуль с видом на бухту."
        ],
        "food": "🍣 Попробовать пинчос в баре Gandarias.",
        "budget": 300,
        "transport": "🚄 Поезд из Барселоны (€50–€100).<br>🚗 Взять авто в Сан-Себастьяне (около €60/день)."
    },
    "Бильбао": {
        "coords": [43.2630, -2.9350],
        "days": 1,
        "arrival_day": 3,
        "arrival_time": "утром",
        "departure_day": 4,
        "departure_time": "до 11 утра",
        "activities": [
            "🖼️ Посещение музея Гуггенхайма.",
            "🌆 Старый город и рынок Рибера."
        ],
        "food": "🍷 Попробовать баскское вино 'Txakoli' и тапасы.",
        "budget": 180,
        "transport": "🚗 На авто из Сан-Себастьяна (около €60/день)."
    },
    "Овьедо": {
        "coords": [43.3614, -5.8593],
        "days": 1,
        "arrival_day": 4,
        "arrival_time": "днём",
        "departure_day": 5,
        "departure_time": "до 11 утра",
        "activities": [
            "🍺 Дегустация сидра в баре.",
            "🏰 Осмотр собора Святого Сальвадора.",
            "🏞️ Легкий хайк в Пикос-де-Европа."
        ],
        "food": "🍏 Попробовать сидр и 'Fabada Asturiana' (фасоль с мясом).",
        "budget": 120,
        "transport": "🚗 На авто из Бильбао (около 2 часов)."
    },
    "Порту": {
        "coords": [41.1496, -8.6110],
        "days": 2,
        "arrival_day": 5,
        "arrival_time": "вечером",
        "departure_day": 7,
        "departure_time": "до 11 утра",
        "activities": [
            "🍷 Дегустация портвейна.",
            "🚤 Прогулка по реке Дору.",
            "🎶 Концерт фаду в Рибейре."
        ],
        "food": "🍤 Попробовать Francesinha (сэндвич с мясом и соусом).",
        "budget": 250,
        "transport": "🚗 Сдать авто в Порту.<br>🛵 Взять макси-скутер в Порту (€30/день)."
    },
    "Авеиро": {
        "coords": [40.6405, -8.6538],
        "days": 1,
        "arrival_day": 7,
        "arrival_time": "днём",
        "departure_day": 8,
        "departure_time": "до 11 утра",
        "activities": [
            "🛶 Прогулка по каналам на молисейро (традиционной лодке).",
            "🏠 Посещение старого города с яркими домиками."
        ],
        "food": "🍬 Попробовать 'Ovos Moles' (десерт из яичных желтков и сахара).",
        "budget": 100,
        "transport": "🛵 На скутере из Порту."
    },
    "Назаре": {
        "coords": [39.6012, -9.0707],
        "days": 1,
        "arrival_day": 8,
        "arrival_time": "утром",
        "departure_day": 9,
        "departure_time": "до 11 утра",
        "activities": [
            "🌊 Наблюдение за гигантскими волнами.",
            "🏄 Посмотреть на серферов у утёса.",
            "🌅 Хайк по утёсам с видом на океан."
        ],
        "food": "🐙 Попробовать свежего осьминога на гриле.",
        "budget": 150,
        "transport": "🛵 На скутере из Авеиро (около 2 часов)."
    },
    "Лиссабон": {
        "coords": [38.7169, -9.1399],
        "days": 2,
        "arrival_day": 10,
        "arrival_time": "днём",
        "departure_day": 11,
        "departure_time": "любое время",
        "activities": [
            "🎶 Фаду в районе Альфама.",
            "🚶 Прогулка по Байрру-Алту.",
            "🍤 Ужин с морепродуктами."
        ],
        "food": "🥐 Попробовать пастель-де-ната в Pasteis de Belem.",
        "budget": 200,
        "transport": "🛵 Сдать макси-скутер в Лиссабоне.<br>🛫 Улетаем домой в Барселону."
    }
}

# Создание карты
map_route = folium.Map(location=[41.3851, 2.1734], zoom_start=6)

# Добавление маркеров с полным описанием
cumulative_budget = 0
for city, data in locations.items():
    cumulative_budget += data["budget"]
    description = f"""
    <b>{city}</b><br>
    🗓️ Здесь проведем {data["days"]} дней<br>
    🚀 Прибытие на {data["arrival_day"]}-й день ({data["arrival_time"]})<br>
    🏃‍♂️ Отъезд на {data["departure_day"]}-й день ({data["departure_time"]})<br>
    {"<br>".join(data.get("activities", []))}<br>
    🍽️ {data.get("food", "-")}<br>
    💰 Бюджет: €{data["budget"]} / €{cumulative_budget} всего<br>
    🚗 {data.get("transport", "-")}
    """
    folium.Marker(location=data["coords"], popup=folium.Popup(description, max_width=400)).add_to(map_route)

# Линия маршрута
coords = [data["coords"] for data in locations.values()]
folium.PolyLine(coords, color='blue', weight=2.5, opacity=1).add_to(map_route)

# Сохранение карты
map_route.save("route_map.html")


# In[ ]:





# In[ ]:




