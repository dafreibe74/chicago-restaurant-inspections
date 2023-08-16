import pandas as pd

data = {
    'Neighborhood': [
        'Albany Park', 'Archer Heights', 'Armour Square', 'Ashburn', 'Auburn Gresham', 'Austin', 'Avalon Park', 'Avondale',
        'Belmont Cragin', 'Beverly', 'Bridgeport', 'Brighton Park', 'Burnside', 'Calumet Heights', 'Chatham', 'Chicago Lawn',
        'Clearing', 'Douglas', 'Dunning', 'East Garfield Park', 'East Side', 'Edgewater', 'Edison Park', 'Englewood',
        'Forest Glen', 'Fuller Park', 'Gage Park', 'Garfield Ridge', 'Grand Boulevard', 'Greater Grand Crossing', 'Hegewisch',
        'Hermosa', 'Humboldt Park', 'Hyde Park', 'Irving Park', 'Jefferson Park', 'Kenwood', 'Lakeview', 'Lincoln Park',
        'Lincoln Square', 'Little Village', 'Logan Square', 'Loop', 'Lower West Side', 'McKinley Park', 'Montclare',
        'Morgan Park', 'Mount Greenwood', 'Near North Side', 'Near South Side', 'Near West Side', 'New City', 'North Center',
        'North Lawndale', 'North Park', 'Norwood Park', 'Oakland', 'O\'Hare', 'Portage Park', 'Pullman', 'Riverdale',
        'Rogers Park', 'Roseland', 'South Chicago', 'South Deering', 'South Lawndale', 'South Shore', 'The Loop', 'Uptown',
        'Washington Heights', 'Washington Park', 'West Elsdon', 'West Englewood', 'West Garfield Park', 'West Lawn',
        'West Pullman', 'West Ridge', 'West Town', 'Woodlawn'
    ],
    'Zip Code': [
        '60625', '60632', '60616', '60620', '60619', '60644', '60619', '60618',
        '60639', '60643', '60608', '60609', '60628', '60617', '60620', '60629',
        '60638', '60653', '60634', '60624', '60617', '60633', '60640', '60630',
        '60621', '60646', '60609', '60652', '60637', '60628', '60629', '60634',
        '60639', '60615', '60641', '60625', '60614', '60625', '60659', '60608',
        '60647', '60607', '60624', '60618', '60608', '60609', '60643', '60657',
        '60614', '60615', '60610', '60605', '60612', '60608', '60653', '60639',
        '60613', '60641', '60623', '60645', '60617', '60621', '60608', '60620',
        '60632', '60652', '60624', '60638', '60628', '60649', '60620', '60605',
        '60640', '60620', '60636', '60637', '60624', '60629', '60620', '60609',
        '60641', '60636', '60651'
    ]
}

neighborhoods_df = pd.DataFrame(data)
print(neighborhoods_df)

eighborhoods_df.to_csv('chicago_neighborhoods.csv', index=False)