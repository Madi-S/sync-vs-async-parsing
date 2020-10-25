import requests
import csv
from time import time


scraped_count = 0
LIMIT = 6150


def get_lines(url):
    r = requests.get(url)
    return r.text


def write_csv(data):
    with open('liveinternet_ajax_data.csv', 'a', newline='', encoding='utf-16') as f:
        order = ['Name', 'URL', 'Description', 'Traffic', 'Percent']
        writer = csv.DictWriter(f, fieldnames=order)
        writer.writerow(data)


def main():
    for i in range(1, LIMIT):
        url = f'https://www.liveinternet.ru/rating/ru//today.tsv?page={i}'
        print(f'Parsing {url}')
        response = get_lines(url)
        data = response.strip().split('\n')[1:]

        for row in data:
            columns = row.strip().split('\t')
            name = columns[0]
            url = columns[1].replace('/', '')
            description = columns[2]
            traffic = columns[3]
            percent = columns[4]

            data = {'Name': name,
                    'URL': url,
                    'Description': description,
                    'Traffic': traffic,
                    'Percent': percent}
            write_csv(data)


if __name__ == "__main__":
    start = time()
    main()
    finish = time()
    speed = LIMIT/(finish - start)
    print(finish - start)
    print(f'Speed: {speed} URLs/second')


# 2.8 URLs per second