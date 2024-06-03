import requests
import re

with open('data/addresses.txt', 'r', encoding='utf-8-sig') as file:
    addresses = [line.strip() for line in file]

headers = {
    "accept": "text/x-component",
    "accept-language": "en,en-US;q=0.9,ru;q=0.8",
    "content-type": "text/plain;charset=UTF-8",
    "next-action": "5aaed2a280e7b9ca6142950ffd5747c025a3de1b",
    "next-router-state-tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2F%22%2C%22refresh%22%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
    "priority": "u=1, i",
    "sec-ch-ua": "\"Chromium\";v=\"124\", \"Google Chrome\";v=\"124\", \"Not-A.Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "Referer": "https://check.kresko.link/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
}

url = "https://check.kresko.link/"
points_regex = re.compile(r'"points":(\d+)')

with open('data/result.txt', 'w', encoding='utf-8-sig') as result_file:
    for address in addresses:
        response = requests.post(url, headers=headers, data=f'["{address.lower()}"]')
        if response.status_code == 200:
            match = points_regex.search(response.text)
            if match:
                points = match.group(1)
                result_file.write(f'{address}: {points}\n')
            else:
                result_file.write(f'{address}: 0\n')
        else:
            print(f'Failed to fetch data for address {address}, status code: {response.status_code}')
            result_file.write(f'{address}: Request failed\n')
