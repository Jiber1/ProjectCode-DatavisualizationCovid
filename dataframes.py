import pandas as pd


def createdf_date(month, day):
    filter = ['Admin2', 'Lat', 'Long_', 'Last_Update', 'Confirmed', 'Deaths', 'Recovered', 'Active', 'Incidence_Rate', 'Case-Fatality_Ratio']
    
    addressMonth = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/'
    addressMonth = addressMonth + month
    addressDay = addressMonth + "-"
    addressDay = addressDay + day
    
    link = addressDay + "-2020.csv"

    try:
        df = pd.read_csv(link)

        df = df.query('Province_State == "Illinois"')
        df = df.query('Country_Region == "US"')

        df = df.rename(columns = {"Incident_Rate":"Incidence_Rate"})
        df = df.rename(columns = {"Case_Fatality_Ratio":"Case-Fatality_Ratio"})
        df = df[filter]

    except IOError:
        df = 0
        print("No data found for that date")
    
    return df

def createdf():
    filter = ['Admin2', 'Lat', 'Long_', 'Last_Update', 'Confirmed', 'Deaths', 'Recovered', 'Active', 'Incidence_Rate', 'Case-Fatality_Ratio']

    for i in range(7,12):
        for j in range(31):
            tempAddressMonth = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/'

            if i + 1 < 10:
                tempAddressMonth = tempAddressMonth + "0" + str(i+1)
            else:
                tempAddressMonth = tempAddressMonth + str(i+1)

            tempAddressDay = tempAddressMonth + "-"

            if j + 1 < 10:
                tempAddressDay = tempAddressDay + "0" + str(j+1)
            else:
                tempAddressDay = tempAddressDay + str(j+1)
            
            tempAddressDay = tempAddressDay + "-2020.csv"

            try:
                temp_df = pd.read_csv(tempAddressDay)

                temp_df = temp_df.query('Province_State == "Illinois"')
                temp_df = temp_df.query('Country_Region == "US"')

                temp_df = temp_df.rename(columns = {"Incident_Rate":"Incidence_Rate"})
                temp_df = temp_df.rename(columns = {"Case_Fatality_Ratio":"Case-Fatality_Ratio"})
                temp_df = temp_df[filter]
                if i == 7 and j == 0:
                    df = temp_df
                else:
                    df = pd.concat([df,temp_df])
                print("Data for " + str(i + 1) + "/" + str(j + 1) + " added")
            except IOError:
                i = i
                j = j

    print("Done creating dataframes")
    return df

def create_countydf(stat, county):
    tempAdd = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_" + stat + "_US.csv"
    
    df = pd.read_csv(tempAdd)
    df = df.query('Province_State == "Illinois"')
    df = df.query('Admin2 == "' + county + '"')
    df = df.rename(columns = {"Incident_Rate":"Incidence_Rate"})
    df = df.rename(columns = {"Case_Fatality_Ratio":"Case-Fatality_Ratio"})
    if (stat == 'confirmed'):
        df = df.drop(labels = ['UID', 'iso2', 'iso3', 'code3', 'FIPS', 'Admin2', 'Province_State', 'Country_Region', 'Lat', 'Long_', 'Combined_Key'], axis=1)
    elif (stat == 'deaths'):
        df = df.drop(labels = ['UID', 'iso2', 'iso3', 'code3', 'FIPS', 'Admin2', 'Province_State', 'Country_Region', 'Lat', 'Long_', 'Combined_Key', 'Population'], axis=1)

    return df