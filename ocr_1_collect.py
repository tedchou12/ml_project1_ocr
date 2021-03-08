import requests
import random

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


counter = 0

while counter < 100 :
    random.shuffle(digits)
    number = str(digits[0]) + str(digits[1]) + str(digits[2]) + str(digits[3]) + str(digits[4]) + str(digits[5])

    with open('data/' + str(number) + '.jpg', 'wb') as handle:
        response = requests.get('https://afrts.forest.gov.tw/ValidateCode.ashx?id=' + str(number), stream=True)

        if not response.ok:
            print(response)

        for block in response.iter_content(1024):
            if not block:
                break

            handle.write(block)


    counter += 1
