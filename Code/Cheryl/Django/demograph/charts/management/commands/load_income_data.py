from django.core.management.base import BaseCommand
import json
import requests
from charts.models import IncomeLevel, Gender, EducationLevel, IncomeData


def get_json(url):
    # print('loading ' + url + '...')
    return json.loads(requests.get(url).text)

class Command(BaseCommand):

    def handle(self, *args, **options):

        # for year in [2015, 2016]
        year = 2015
        variables = 'NAME,B17003_004E,B17003_005E,B17003_006E,B17003_007E,B17003_009E,B17003_010E,B17003_011E,B17003_012E,B17003_015E,B17003_016E,B17003_017E,B17003_018E,B17003_020E,B17003_021E,B17003_022E,B17003_023E'
        geography = 'county:*'
        dataset_name = '/acs1'
        url = f'https://api.census.gov/data/{year}{dataset_name}?get={variables}&for={geography}'

        # print(url)
        # return


        subsets = [
            {'IncomeLevel': 'Below Poverty', 'Gender': 'Male', 'EducationLevel': 'Less than hs', 'column_name': 'B17003_004E'},
            {'IncomeLevel': 'Below Poverty', 'Gender': 'Male', 'EducationLevel': 'hs', 'column_name': 'B17003_005E'},
            {'IncomeLevel': 'Below Poverty', 'Gender': 'Male', 'EducationLevel': 'some college', 'column_name': 'B17003_006E'},
            {'IncomeLevel': 'Below Poverty', 'Gender': 'Male', 'EducationLevel': 'college',
             'column_name': 'B17003_007E'},

            {'IncomeLevel': 'Below Poverty', 'Gender': 'Female', 'EducationLevel': 'Less than hs',
             'column_name': 'B17003_009E'},
            {'IncomeLevel': 'Below Poverty', 'Gender': 'Female', 'EducationLevel': 'hs', 'column_name': 'B17003_010E'},
            {'IncomeLevel': 'Below Poverty', 'Gender': 'Female', 'EducationLevel': 'some college',
             'column_name': 'B17003_011E'},
            {'IncomeLevel': 'Below Poverty', 'Gender': 'Female', 'EducationLevel': 'college',
             'column_name': 'B17003_012E'},

            {'IncomeLevel': 'At or Above Poverty', 'Gender': 'Male', 'EducationLevel': 'Less than hs',
             'column_name': 'B17003_015E'},
            {'IncomeLevel': 'At or Above Poverty', 'Gender': 'Male', 'EducationLevel': 'hs', 'column_name': 'B17003_016E'},
            {'IncomeLevel': 'At or Above Poverty', 'Gender': 'Male', 'EducationLevel': 'some college',
             'column_name': 'B17003_017E'},
            {'IncomeLevel': 'At or Above Poverty', 'Gender': 'Male', 'EducationLevel': 'college',
             'column_name': 'B17003_018E'},

            {'IncomeLevel': 'Below Poverty', 'Gender': 'Female', 'EducationLevel': 'Less than hs',
             'column_name': 'B17003_020E'},
            {'IncomeLevel': 'Below Poverty', 'Gender': 'Female', 'EducationLevel': 'hs', 'column_name': 'B17003_021E'},
            {'IncomeLevel': 'Below Poverty', 'Gender': 'Female', 'EducationLevel': 'some college',
             'column_name': 'B17003_022E'},
            {'IncomeLevel': 'Below Poverty', 'Gender': 'Female', 'EducationLevel': 'college',
             'column_name': 'B17003_023E'},

        ]


        data_in = get_json(url)


        headers = data_in[0]
        data_in = data_in[1:]
        data_out = []
        for row_in in data_in:
            row_out = {}
            for i, header in enumerate(headers):
                row_out[header] = row_in[i]
            data_out.append(row_out)

        for row in data_out:
            # print(f"{row['NAME']} Men above poverty level with college per county: {row['B17003_018E']}")
            print(row)

            for subset in subsets:
                income_level = IncomeLevel.objects.get_or_create(name=subset['IncomeLevel'])
                gender = Gender.objects.get_or_create(name=subset['Gender'])
                education_level = EducationLevel.objects.get_or_create(name=subset['EducationLevel'])
                county =
                year =
                population = int(row[subset['column_name']])
                income_data = IncomeData(education_level=education_level[0], gender=gender[0], income_level=income_level[0], population=population)
                income_data.save()


            #if education_level[1] == True:
            #    education_level[0].save()

