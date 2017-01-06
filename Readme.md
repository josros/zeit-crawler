# zeit-crawler

This [Scrapy](https://scrapy.org/) crawler retrieves latest articles from [zeit-online](http://www.zeit.de/index).
In its pipeline, it drops irrelevant articles and performs an article based word count.

Finally, it exports article information structured as shown in the following json:

```json
{
  "body": [
    "<article content>"
  ],
  "dates": [
    "2017-01-04T09:07:51+01:00"
  ],
  "tags": [
    "Arbeitszeit",
    "<more tags>"
  ],
  "wordcount": {
    "verkürzen": 1,
    "arbeitsministerin": 2,
    "rückkehr": 2
  },
  "subheaders": [
    "Varianten zum Achtstundentag"
  ],
  "summary": [
    "\n                Ein Anspruch auf Teilzeit besteht bereits, nicht jedoch das Recht auf Rückkehr in den Fulltime-Job. Die Arbeitsministerin will das ermöglichen – unter Bedingungen.\n            "
  ],
  "header": [
    "Nahles plant Recht auf befristete Teilzeit"
  ],
  "link": "http://www.zeit.de/wirtschaft/2017-01/andrea-nahles-teilzeit-befristet-rueckkehr-vollzeit-arbeitszeiten",
  "kicker": [
    "Arbeitszeiten"
  ]
}
```

# Executive Summary

## Prerequisites

  Install and configure [Scrapy](https://scrapy.org/) as shown [here](https://doc.scrapy.org/en/latest/intro/install.html).

## Run crawler

Run:
`
scrapy crawl zeit
`
