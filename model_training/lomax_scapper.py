import requests
from bs4 import BeautifulSoup
import threading
import json
import os

file_lock = threading.Lock()

write_to_iterations = 10
# def write_to_file(fileName: str, fileWriteMethod: str, output: str):
#     with open(fileName, fileWriteMethod, encoding='utf-8') as f:
#         f.write(json.dumps(output, indent=4))


def scrape_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'lxml')
        description_element = soup.find(
            'div', class_='productdesc-content')  # description element
        title_element = soup.select(
            "div.d-inline-block.float-left.order-2.order-lg-1")  # title element
        if description_element and title_element:
            description = description_element.get_text()
            title = title_element[0].contents[1].get_text()

            data = {
                "prompt": str(title.strip()),
                "completion": f" {description.strip()}"
            }

            return data


def scrape_sitemap(sitemap_url):
    response = requests.get(sitemap_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'lxml')
        urls = soup.find_all('loc')
        titles = soup.find_all("image:title")
        # threads = []
        print(f"Found {len(urls)} urls and {len(titles)} titles")

        json_output = []
        failed_urls = []

        with open("product-4-sitemap.jsonl", "a", encoding='utf-8') as f:
            for i, url in enumerate(urls):
                try:
                    url = url.get_text()
                    data = scrape_url(url)
                    if data:
                        json_output.append(data)
                    if (i+1) % write_to_iterations == 0:
                        print(
                            f"Writing to file, iteration {i}. {round(((i/len(urls))*100), 2)}% finished")
                        for d in json_output:
                            f.write(json.dumps(d) + "\n")

                        json_output = []

                except:
                    print("Failed for " + url)
                    failed_urls.append(url)
                    continue
                # t = threading.Thread(target=scrape_url, args=(url,))
                # threads.append(t)
                # t.start()

            # for thread in threads:
            #     thread.join()
        f.close()


# sitemap_url = input("Enter URL for sitemap: ")
sitemap_url = "https://www.lomax.dk/static/sitemap/dk/products3_sitemap.xml"
striped_url = stripped = sitemap_url.rsplit('/', 1)[-1].replace('.xml', '')

scrape_sitemap(sitemap_url)

# with open('output_https://www.lomax.dk/static/sitemap/dk/products4_sitemap.xml.jsonl', 'a', encoding='utf-8') as f:
#     f.write(json.dumps(json_output, indent=4))

# with open(f"failed_urls_https://www.lomax.dk/static/sitemap/dk/products4_sitemap.xml.jsonl", "a", encoding="utf-8") as f:
#     f.write(json.dumps(failed_urls, indent=4))

print("Finished")
