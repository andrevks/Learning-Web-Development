import json


if __name__ == '__main__':
    day = '21-Dec-2021'
    filename = f'extractedNumbers-{day}.json'
    orderedNumbers = []
    try:
        with open(filename, 'r') as outfile:
            file = json.load(outfile)
        print(f'Before Transforming: ')
        count = 0
        # O(n)
        for number in file:
            print(number)
            count += 1


        print(f'Indexes: {count}')
    except Exception as ex:
        print(f'Error in creating file: {ex}')
