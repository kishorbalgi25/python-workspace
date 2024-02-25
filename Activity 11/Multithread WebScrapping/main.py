import threading
import requests
from bs4 import BeautifulSoup

class ScraperThread(threading.Thread):
    def __init__(self, url):
        super(ScraperThread, self).__init__()
        self.url = url
        self.data = None

    def run(self):
        try:
            response = requests.get(self.url,verify=False)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                
                head = soup.find("title")
                self.data = head          
            else:
                print(f"Failed to scrape {self.url}. Status code: {response.status_code}")
        except Exception as e:
            print(f"Error scraping {self.url}: {e}")

def main():
    urls = [
        "https://www.flipkart.com/search?q=iphone+15",
        "https://www.apple.com/in/iphone-15/",
    ]

    threads = []
    for url in urls:
        thread = ScraperThread(url)
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    # Process the data scraped by each thread
    for thread in threads:
        if thread.data is not None:
            print(f"Data scraped from {thread.url}: {thread.data}")
        else:
            print(f"No data scraped from {thread.url}")

if __name__ == "__main__":
    main()
