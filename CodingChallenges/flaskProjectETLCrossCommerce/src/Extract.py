import requests
import json
from requests.exceptions import HTTPError, Timeout
import time
import datetime
if __name__ == '__main__':
    extractedNumbers = []
    startTime = time.time()
    try:
        pageNumber = 1
        while True:
            resp = requests.get(f'http://challenge.dienekes.com.br/api/numbers?page={pageNumber}')
            # print(resp)
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
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Timeout:
        print('The request timed out')
    except Exception as err:
        print(f'Other errors occurred: {err}')
    else:
        executionTime = str((time.time() - startTime))
        print('Success')
        print(f'List of extracted numbers: {extractedNumbers}')
        dt_data = datetime.datetime.now()
        day = str(dt_data.strftime("%d-%b-%Y"))

        try:
            with open(f'extractedNumbers-{day}.json', 'w') as outfile:
                json.dump(extractedNumbers, outfile, indent=4)
        except Exception as ex:
            print(f'Error in creating file: {ex}')

        print("\n-----------------------------------")
        print(f" Took {executionTime} s to EXTRACT")
        print("-----------------------------------\n")




