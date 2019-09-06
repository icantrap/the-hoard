## What It Is

Scrapes Roadside Attraction photos from Library of Congress site. [link](https://www.reddit.com/r/DataHoarder/comments/czmda0/12k_photos_of_american_roadside_attractions/)

Goes to each page, notes the URL, title, and marc record URL, and downlaods the four photo versions.

It's a [scrapy](https://doc.scrapy.org/en/1.7/index.html) project.

```bash
$ scrapy crawl roadside_attractions -o output.json
```

## Possibly Faulty Instructions

If you don't know python, then you can try this. If it doesn't work, you've got some work to do.

1. Install a python. There's a `.tool-versions` file in the repo root, if [asdf](https://github.com/asdf-vm/asdf) is your jam. I used PyPy 3.6, but I bet most versions of Python 3 would work.
1. Install pipenv. `pip install pipenv`
1. Install dependencies. `pipenv install`
1. Start a shell. `pipenv shell`
1. Run the scrapy project. `scrapy crawl roadside_attractions -o output.json`
1. It takes a long time, so leave it running. Type `exit` to leave the pipenv shell.