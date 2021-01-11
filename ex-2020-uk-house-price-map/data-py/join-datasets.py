import pandas as pd
price_data = pd.read_csv('./England-annual-price-change-by-local-authority-2020-01.csv', encoding='latin1')

import json
with open('lad.json') as json_file:
    shp_data = json.load(json_file)
    
    count = 0
    errors = []

    for i in range(len(shp_data['features'])):
        name = shp_data['features'][i]['properties']['LAD13NM']
        if sum(price_data['Local authorities'] == name) == 1:
            price = price_data[price_data['Local authorities'] == name]['January 2020'].values[0].strip('£')
            shp_data['features'][i]['properties']['price'] = int(price)
            count += 1
        else:
            shp_data['features'][i]['properties']['price'] = 0
            errors.append(name)

with open('data.json', 'w') as outfile:
    json.dump(shp_data, outfile)            

print('{} - joined; saved to data.json'.format(count))
print('errors: {}'.format(errors))