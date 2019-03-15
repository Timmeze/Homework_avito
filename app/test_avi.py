from app.lib import create_ad, add_ad, search_dist, search_price


def test_create_ad():
    data = {
        'title': 'Ваз 2101',
        'price': 15_000,
        'district': 'kirov',
        'phone_numb': '+7987654321'
    }

    result = create_ad(data['title'], data['price'], data['district'], data['phone_numb'])

    assert data == result

def test_add_ad_to_empty_cont():
    cont = []
    ad = create_ad('Ваз 2101', 15_000, 'kirov', '+7987654321')
    add_ad(cont, ad)

    assert ad in cont

def test_add_ad_to_noempty_con():
    cont = [{'title': 'Ваз 2101', 'price': 15_000, 'district': 'kirov', 'phone numb': '+7987654321'}]

    ad_1 = create_ad('Ваз 2107', 85_000, 'avia', '+7987654312')
    add_ad(cont, ad_1)

    assert ad_1 in cont
    assert len(cont) == 2

def test_search_dict():
    cont = []

    ad_0 = create_ad('Ваз 2101', 15_000, 'kirov', '+7987654321')
    ad_1 = create_ad('Ваз 2107', 85_000, 'avia', '+7987654312')
    add_ad(cont, ad_1)
    add_ad(cont, ad_0)

    result = search_dist(cont, 'avia')

    assert ad_1 in result
    assert len(result) == 1

def test_search_price():
    cont = []

    ad_0 = create_ad('Ваз 2101', 15_000, 'kirov', '+7987654321')
    ad_1 = create_ad('Ваз 2107', 85_000, 'avia', '+7987654312')
    add_ad(cont, ad_1)
    add_ad(cont, ad_0)

    result = search_price(cont, 20_000)
    assert ad_1 in result
    assert len(result) == 1


