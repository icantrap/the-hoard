import scrapy
from library_of_congress.items import LibraryOfCongressItem

class RoadsideAttractionsSpider(scrapy.Spider):
  name = 'roadside_attractions'
  start_urls = ['https://www.loc.gov/pictures/search/?q=mrg&sp=1&st=gallery']

  def parse(self, response):
    first_page_url = response.css('table tr td.first p a')[0].attrib['href']
    yield response.follow(first_page_url, callback=self.parse_page)

  def parse_page(self, response):
    title = response.css('title::text').get().strip()
    marc_url = response.css('a#item_marc').attrib['href']
    urls = map(lambda anchor: anchor.attrib['href'], response.css('a'))
    targets = filter(lambda url: 'jpg' in url or 'tif' in url, urls)
    target_urls = list(map(lambda target: response.urljoin(target), targets))

    yield LibraryOfCongressItem(title=title, url=response.url, marc_url=marc_url, file_urls=target_urls)

    next_page_url = response.css('.images a').pop().attrib['href']
    yield response.follow(next_page_url, callback=self.parse_page)
