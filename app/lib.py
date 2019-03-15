def create_ad(title, price, district, phone_numb):
    district_list = {'avia', 'mosk', 'novo-savin', 'kirov', 'privol', 'vahit'}
    district_clear = district.lower().strip()
    if district_clear in district_list:
        return {
        'title' : title,
        'price' : price,
        'district' : district,
        'phone_numb' : phone_numb
    }
    else:
        return print('Некорректно указан район')

def add_ad(container, ad):
    container.append(ad)
    return container

def search_dist (container, district):
    district_clear = district.strip().lower()
    result = []
    for ad in container:
        if district_clear in ad['district']:
            result.append(ad)
            continue
    return result

def search_price (container, price):
    result = []
    for ad in container:
        if price <= ad['price']:
            result.append(ad)
            continue
    return result
