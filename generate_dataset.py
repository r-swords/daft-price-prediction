from daftlistings import  Location, SearchType, PropertyType, Facility, Daft
import csv


class Property:
    size = 0
    bedroom = 0
    bathroom = 0
    ber_rating = 0
    house_type = ''
    parking = 0
    alarm = 0
    oil = 0
    gas = 0
    wheelchair = 0
    cable_tv = 0
    antrim = 0
    armagh = 0
    carlow = 0
    cavan = 0
    clare = 0
    cork = 0
    derry = 0
    donegal = 0
    down = 0
    dublin = 0
    fermanagh = 0
    galway = 0
    kerry = 0
    kildare = 0
    kilkenny = 0
    laois = 0
    leitrim = 0
    limerick = 0
    longford = 0
    louth = 0
    mayo = 0
    meath = 0
    monaghan = 0
    offaly = 0
    roscommon = 0
    sligo = 0
    tipperary = 0
    tyrone = 0
    waterford = 0
    westmeath = 0
    wexford = 0
    wicklow = 0
    price = 0


def write(new_property):
    with open('dataset.csv', 'a') as f:
        w = csv.writer(f)
        w.writerow([new_property.size, new_property.bedroom, new_property.bathroom, new_property.house_type,
                    new_property.ber_rating, new_property.parking, new_property.alarm, new_property.oil,
                    new_property.gas, new_property.wheelchair, new_property.cable_tv, new_property.antrim,
                    new_property.armagh, new_property.carlow, new_property.cavan, new_property.clare, new_property.cork,
                    new_property.derry, new_property.donegal, new_property.down, new_property.dublin,
                    new_property.fermanagh, new_property.galway, new_property.kerry, new_property.kildare,
                    new_property.kilkenny, new_property.laois, new_property.leitrim, new_property.limerick,
                    new_property.longford, new_property.louth, new_property.mayo, new_property.meath,
                    new_property.monaghan, new_property.offaly, new_property.roscommon, new_property.sligo,
                    new_property.tipperary, new_property.tyrone, new_property.waterford, new_property.westmeath,
                    new_property.wexford, new_property.wicklow, new_property.price])


daft = Daft()
daft.set_search_type(SearchType.RESIDENTIAL_SALE)
listings = daft.search(max_pages=10)

daft = Daft()
daft.set_search_type(SearchType.RESIDENTIAL_SALE)
daft.set_facility(Facility.ALARM)
alarm_listings = daft.search()
alarm = set()
for i in alarm_listings:
    alarm.add(i.title)

daft = Daft()
daft.set_search_type(SearchType.RESIDENTIAL_SALE)
daft.set_facility(Facility.PARKING)
parking_listings = daft.search()
parking = set()
for i in parking_listings:
    parking.add(i.title)

daft = Daft()
daft.set_search_type(SearchType.RESIDENTIAL_SALE)
daft.set_facility(Facility.CENTRAL_HEATING_OIL)
oil_listings = daft.search()
oil = set()
for i in oil_listings:
    oil.add(i.title)

daft = Daft()
daft.set_search_type(SearchType.RESIDENTIAL_SALE)
daft.set_facility(Facility.CENTRAL_HEATING_GAS)
gas_listings = daft.search()
gas = set()
for i in gas_listings:
    gas.add(i.title)

daft = Daft()
daft.set_search_type(SearchType.RESIDENTIAL_SALE)
daft.set_facility(Facility.WHEELCHAIR_ACCESS)
wheelchair_listings = daft.search()
wheelchair = set()
for i in wheelchair_listings:
    wheelchair.add(i.title)

daft = Daft()
daft.set_search_type(SearchType.RESIDENTIAL_SALE)
daft.set_facility(Facility.WIRED_FOR_CABLE_TELEVISION)
cable_listings = daft.search()
cable = set()
for i in cable_listings:
    cable.add(i.title)

with open('dataset.csv', 'a') as f:
    w = csv.writer(f)
    w.writerow(['Size', 'Bedrooms', 'Bathrooms', 'House_Type', 'Ber_rating', 'parking', 'alarm', 'oil_heating', 'gas_heating', 'wheelchair', 'cable_tv', 'Antrim', 'Armagh', 'Carlow', 'Cavan', 'Clare', 'Cork', 'Derry', 'Donegal', 'Down', 'Dublin', 'Fermanagh', 'Galway', 'Kerry', 'Kildare', 'Kilkenny', 'Laois', 'Leitrim', 'Limerick', 'Longford', 'Louth', 'Mayo', 'Meath', 'Monaghan', 'Offaly', 'Roscommon', 'Sligo', 'Tipperary', 'Tyrone', 'Waterford', 'Westmeath', 'Wexford', 'Wicklow', 'price'])

for i in listings:
    if i.price == "Price on Application":
        continue
    try:
        new_property = Property()
        new_property.size = i.size_meters_squared
        new_property.bathroom = int(i.bathrooms[0])
        new_property.bedroom = int(i.bedrooms[0])
        new_property.ber_rating = ord(i.ber[0]) - 64
        new_property.house_type = i._result['propertyType']
        if i.title in alarm:
            new_property.alarm = 1
        if i.title in parking:
            new_property.parking = 1
        if i.title in oil:
            new_property.oil = 1
        if i.title in gas:
            new_property.gas = 1
        if i.title in wheelchair:
            new_property.wheelchair = 1
        if i.title in cable:
            new_property.cable_tv = 1
        if 'Co. Antrim' in i.title:
            new_property.antrim = 1
        elif 'Co. Armagh' in i.title:
            new_property.armagh = 1
        elif 'Co. Carlow' in i.title:
            new_property.carlow = 1
        elif 'Co. Cavan' in i.title:
            new_property.cavan = 1
        elif 'Co. Clare' in i.title:
            new_property.clare = 1
        elif 'Co. Cork' in i.title:
            new_property.cork = 1
        elif 'Co. Derry' in i.title:
            new_property.derry = 1
        elif 'Co. Donegal' in i.title:
            new_property.donegal = 1
        elif 'Co. Down' in i.title:
            new_property.down = 1
        elif 'Co. Dublin' in i.title or ('Dublin ' in i.title and not 'Dublin Road' in i.title):
            new_property.dublin = 1
        elif 'Co. Fermanagh' in i.title:
            new_property.fermanagh = 1
        elif 'Co. Galway' in i.title:
            new_property.galway = 1
        elif 'Co. Kerry' in i.title:
            new_property.kerry = 1
        elif 'Co. Kildare' in i.title:
            new_property.kildare = 1
        elif 'Co. Kilkenny' in i.title:
            new_property.kilkenny = 1
        elif 'Co. Laois' in i.title:
            new_property.laois = 1
        elif 'Co. Leitrim' in i.title:
            new_property.leitrim = 1
        elif 'Co. Limerick' in i.title:
            new_property.limerick = 1
        elif 'Co. Longford' in i.title:
            new_property.longford = 1
        elif 'Co. Louth' in i.title:
            new_property.louth = 1
        elif 'Co. Mayo' in i.title:
            new_property.mayo = 1
        elif 'Co. Meath' in i.title:
            new_property.meath = 1
        elif 'Co. Monaghan' in i.title:
            new_property.monaghan = 1
        elif 'Co. Offaly' in i.title:
            new_property.offaly = 1
        elif 'Co. Roscommon' in i.title:
            new_property.roscommon = 1
        elif 'Co. Sligo' in i.title:
            new_property.sligo = 1
        elif 'Co. Tipperary' in i.title:
            new_property.tipperary = 1
        elif 'Co. Tyrone' in i.title:
            new_property.tyrone = 1
        elif 'Co. Waterford' in i.title:
            new_property.waterford = 1
        elif 'Co. Westmeath' in i.title:
            new_property.westmeath = 1
        elif 'Co. Wexford' in i.title:
            new_property.wexford = 1
        elif 'Co. Wicklow' in i.title:
            new_property.wicklow = 1
        else:
            print(i.title)
            continue
        new_property.price = int(i.price[1:].replace(',',''))
        write(new_property)
    except Exception as e:
        print(e)
        continue