from django.db import models
#from django.contrib.postgres.fields import JSONField
import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
from django.db.models import JSONField

def json_data_model():
    url = "https://www.worldometers.info/coronavirus/"

    result_dict = {}
    country_dict = {}
    world_status_dict = {}

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    soup = re.sub(r'<.*?>', lambda g: g.group(0).upper(), str(soup))

    df = pd.read_html(soup)
    df = df[0]

    df = df.rename(
        columns={
            'Country,Other': 'CountryName'
        }
    )
    df_country_column = df['CountryName'][7:230]
    df.set_index('CountryName', inplace=True)

    df['RecoveryRate'] = df['TotalRecovered'] / df['TotalCases']

    df.fillna({'Population': 1}, inplace=True)
    df['PercentageOfPopulationInfected'] = df['TotalCases'] / df['Population'] * 100

    df1 = df[['TotalCases', 'ActiveCases', 'TotalDeaths', 'RecoveryRate', 'PercentageOfPopulationInfected']][7:230]

    df1.fillna(0, inplace=True)
    for country in df_country_column:
        temp_dict = {}
        if country == 'World':
            temp_dict['Total Cases'] = int(df1.loc[country].TotalCases)
            temp_dict['Active Cases'] = int(df1.loc[country].ActiveCases)
            temp_dict['Total Deaths'] = int(df1.loc[country].TotalDeaths)
            temp_dict['Recovery Rate'] = df1.loc[country].RecoveryRate
            temp_dict['Percentage of Population Infected'] = df1.loc[country].PercentageOfPopulationInfected
            world_status_dict[country] = temp_dict
        else:
            # temp_dict['Country Name'] = country
            temp_dict['Total Cases'] = int(df1.loc[country].TotalCases)
            temp_dict['Active Cases'] = int(df1.loc[country].ActiveCases)
            temp_dict['Total Deaths'] = int(df1.loc[country].TotalDeaths)
            temp_dict['Recovery Rate'] = df1.loc[country].RecoveryRate
            temp_dict['Percentage of Population Infected'] = df1.loc[country].PercentageOfPopulationInfected
            country_dict[country] = temp_dict

    result_dict["Entire World Status"] = world_status_dict
    result_dict["Individual Country Status"] = country_dict

    return result_dict


class CoronaModel(models.Model):
    j_data = JSONField()

json_data = json_data_model()
j_data_obj = CoronaModel(j_data = json_data)