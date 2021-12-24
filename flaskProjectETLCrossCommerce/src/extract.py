import requests
import json
from requests.exceptions import HTTPError, Timeout
import time
import datetime

def extract():
    extractedNumbers = []
    startTime = time.time()
    try:
        pageNumber = 9999
        while True:
            url = f'http://challenge.dienekes.com.br/api/numbers?page={pageNumber}'
            resp = requests.get(url)
            numbers = resp.json()
            if 'numbers' in numbers:
                numbers = resp.json()['numbers']
                if not numbers:
                    break
                extractedNumbers.extend(numbers)

            print(f'PAGE={pageNumber} {numbers}')
            # dict_numbers = {pageNumber: numbers}
            # extratedNumbers.append(dict_numbers)
            pageNumber += 1

        executionTime = str((time.time() - startTime))
        print('Success')
        extractedNumbers = [10000,99999,2222,4000]
        print(f'List of extracted numbers: {extractedNumbers}')
        dt_data = datetime.datetime.now()
        day = str(dt_data.strftime("%d-%b-%Y"))
        filename = f'src\\dataWarehouse\\extracted\\extractedNumbers-{day}.json'

        try:
            with open(filename , 'w') as outfile:
                json.dump(extractedNumbers , outfile , indent=4)
        except Exception as ex:
            print(f'Error in creating file: {ex}')

        print("\n-----------------------------------")
        print(f" Took {executionTime} s to EXTRACT")
        print("-----------------------------------\n")

    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Timeout:
        print('The request timed out')
    except Exception as err:
        print(f'Other errors occurred: {err}')




