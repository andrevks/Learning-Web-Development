import json
import time
import os
import glob

def merge(leftArr, rightArr):
    mergedArr = []
    while len(leftArr) > 0 and len(rightArr) > 0:
        if leftArr[0]  < rightArr[0]:
            mergedArr.append(leftArr[0])
            del leftArr[0]
        else:
            mergedArr.append(rightArr[0])
            del rightArr[0]

    while len(leftArr) > 0:
        mergedArr.append(leftArr[0])
        del leftArr[0]

    while len(rightArr) > 0:
        mergedArr.append(rightArr[0])
        del rightArr[0]

    # print(f'\nAfter merging: {mergedArr}\n')
    return mergedArr


def mergeSort(arr):
    # print(f'\narr: {arr}')
    arrLength = len(arr)
    if arrLength == 1:
        return arr

    mid = int((arrLength - 1) / 2)
    leftArr = arr[0:mid+1]
    rightArr = arr[mid+1:]
    # print(f'leftArr before: {leftArr}')
    # print(f'rightArr before: {rightArr}')

    leftArr = mergeSort(leftArr)
    rightArr = mergeSort(rightArr)

    return merge(leftArr, rightArr)


def get_recent_file(type):
    # list_of_files = glob.glob(f'.\\dataWarehouse\\{type}\\*.json')
    list_of_files = glob.glob(f'src\\dataWarehouse\\{type}\\*.json')

    latest_file = max(list_of_files, key=os.path.getctime)
    return latest_file

def transform():
    orderedNumbers = []
    try:
        filename = get_recent_file('extracted')
        with open(filename, 'r') as inputFile:
            numbersExtracted = json.load(inputFile)


        print(f'----Before Transforming-----')
        count = 0
        # O(n)
        for number in numbersExtracted:
            count += 1
        print(f'Numbers Extracted: {count}')

        print('>> initiating Transformation...\n')

        startTime = time.time()
        orderedNumbers = mergeSort(numbersExtracted)
        executionTime = str((time.time() - startTime))
        print('Success')
        print("\n-----------------------------------")
        print(f'\nOrdered Numbers: {orderedNumbers}')
        print("\n-----------------------------------")
        print(f" Took {executionTime} s to TRANSFORM")
        print("-----------------------------------\n")
        day = filename.split('extractedNumbers',1)[1]
        savedFileName = f'src\\dataWarehouse\\transformed\\transformedNumbers{day}'
        print(f'savedFileName: {savedFileName}')

        json_transformedNumbers = json.dumps(orderedNumbers, indent=4)
        with open(savedFileName, 'w') as outfile:
            outfile.write(json_transformedNumbers)
            # json.dump(orderedNumbers , outfile , indent=4)


    except Exception as ex:
        print(f'Error in Tranforming: {ex}')


