## What It Is

Scrapes Roadside Attraction photos from Library of Congress site. [link](https://www.reddit.com/r/DataHoarder/comments/czmda0/12k_photos_of_american_roadside_attractions/)

Goes to each page, notes the URL, title, and marc record URL, and downlaods the four photo versions.

It's a [scrapy](https://doc.scrapy.org/en/1.7/index.html) project.

```bash
$ scrapy crawl roadside_attractions -o output.json
```

**WARNING**. This script will take and estimated 7 days to run and consume 2 TB of disk space for images.