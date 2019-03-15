from app.lib import create_ad, add_ad, search_dist, search_price

bike_ad = create_ad(
    'Велосипед б/у',
    5_000,
    'avia',
    '+79566745883'
)

ps_ad = create_ad(
    'Игровая приставка',
    15_000,
    'avia',
    '+79566745883'
)

flat_ad = create_ad(
    '1-комнатная квартира',
    2_500_000,
    'kirov',
    '+79566745883'
)

avito = []

add_ad(avito, bike_ad)
add_ad(avito, ps_ad)
add_ad(avito, flat_ad)

print(search_dist(avito, 'avia'))
print(search_price(avito, 16000))