import json
import re
import pandas as pd
import scrapy
from scrapy.http import HtmlResponse
from bs4 import BeautifulSoup as bs


REGEX = "(http|ftp|https)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?"
# source https://stackoverflow.com/questions/6038061/regular-expression-to-find-urls-within-a-string


class ScrapeBajajFinserv(scrapy.Spider):
    name = "scraper"
    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"
    }
    
    scraped = {}

    def __del__(self):
        with open(r"C:\Users\KIIT\OneDrive\Documents\scraper\scraper\scraped-data.json", "w") as f:
            json.dump(self.scraped, f)

    def start_requests(self):
        links = {
        "https://www.bajajfinservmarkets.in/insurance/travel-insurance.html",
        "https://www.bajajallianz.com/motor-insurance/car-insurance-online.html",
        "https://www.bajajallianz.com/motor-insurance/two-wheeler-insurance-online.html",
        "https://www.bajajallianz.com/motor-insurance/long-term-two-wheeler-insurance.html",
        "https://www.bajajallianz.com/motor-insurance/third-party-car-insurance-online.html",
        "https://www.bajajallianz.com/motor-insurance/two-wheeler-insurance-third-party.html",
        "https://www.bajajallianz.com/motor-insurance/commercial-vehicle-insurance.html",
        "https://www.bajajfinservmarkets.in/insurance/cyber-security.html",
        "https://www.bajajfinservmarkets.in/insurance/health-insurance.html",
        "https://www.bajajallianz.com/health-insurance-plans/family-health-insurance-india.html",
        "https://www.bajajallianz.com/health-insurance-plans/health-insurance-infinity-plan.html",
        "https://www.bajajallianz.com/health-insurance-plans/arogya-sanjeevani-standard-health-insurance-policy.html",
        "https://www.bajajallianz.com/health-insurance-plans/corona-kavach-policy.html",
        "https://www.bajajallianz.com/health-insurance-plans/top-up-health-insurance.html",
        "https://www.bajajallianz.com/health-insurance-plans/criti-care.html",
        "https://www.bajajallianz.com/health-insurance-plans/critical-Illness-insurance.html",
        "https://www.bajajallianz.com/health-insurance-plans/individual-international-accident-insurance.html",
        "https://www.bajajallianz.com/health-insurance-plans/health-insurance-for-senior-citizens.html",
        "https://www.bajajallianz.com/health-insurance-plans/m-care-health-insurance-policy.html",
        "https://www.bajajallianz.com/health-insurance-plans/saral-suraksha-bima-policy.html",
        "https://www.bajajallianz.com/travel-insurance-online/individual-travel-insurance.html",
        "https://www.bajajallianz.com/travel-insurance-online/family-travel-insurance.html",
        "https://www.bajajallianz.com/travel-insurance-online/student-travel-insurance.html",
        "https://www.bajajallianz.com/travel-insurance-online/travel-ace-plan.html",
        "https://www.bajajallianz.com/travel-insurance-online/bharat-bhraman-domestic-travel-insurance.html",
        "https://www.bajajallianz.com/travel-insurance-online/travel-asia-insurance.html",
        "https://www.bajajallianz.com/travel-insurance-online/senior-citizen-travel-insurance.html",
        "https://www.bajajallianz.com/travel-insurance-online/corporate-travel-insurance.html",
        "https://www.bajajallianz.com/home-insurance/my-home-insurance.html",
        "https://www.bajajallianz.com/home-insurance/householder-policy.html",
        "https://www.bajajallianz.com/commercial-insurance/property-insurance.html",
        "https://www.bajajallianz.com/commercial-insurance/marine-insurance.html",
        "https://www.bajajallianz.com/commercial-insurance/liability-insurance.html",
        "https://www.bajajallianz.com/commercial-insurance/financial-lines-insurance.html",
        "https://www.bajajallianz.com/commercial-insurance/engineering-insurance.html",
        "https://www.bajajallianz.com/commercial-insurance/employee-benefits-insurance.html",
        "https://www.bajajfinservmarkets.in/insurance/motor-insurance.html",
        "https://www.bajajfinservmarkets.in/insurance/ulip.html",
        "https://www.bajajfinservmarkets.in/insurance/term-life.html",
        "https://www.bajajfinservmarkets.in/insurance/home-insurance.html",
        "https://www.bajajfinservmarkets.in/insurance/term-insurance-plans.html",
        "https://www.bajajfinservmarkets.in/insurance/two-wheeler-insurance.html",
        "https://www.bajajfinservmarkets.in/insurance/pradhan-mantri-fasal-bima-yojana-pmfby.html",
        "https://www.bajajfinservmarkets.in/insurance/compound-interest-calculator.html",
        "https://www.bajajfinservmarkets.in/insurance/human-life-value-calculator-hlv.html",
        "https://www.bajajfinservmarkets.in/insurance/car-insurance.html",
        "https://www.bajajfinservmarkets.in/insurance/endowment-policy.html",
        "https://www.bajajfinservmarkets.in/insurance/types-of-insurance.html",
        "https://www.bajajfinservmarkets.in/insurance/sachet.html"
        }
        for link in links:
            sitemapLink = link.split(".html")[0] + "/sitemap.xml"
            yield scrapy.Request(url=sitemapLink, callback=self.parseSitemap)
        for link in links:
            yield scrapy.Request(url=link, callback=self.parse)
        for link in links:
            yield scrapy.Request(url=link, callback=self.parse_priority)

    def parseSitemap(self, response):
        sitemapLinks = re.findall(
            "(http|ftp|https)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?",
            str(response.body),
        )
        for link in sitemapLinks:
            link = list(link)
            link = link[0] + "://" + link[1] + link[2]
            if "sitemap.org" not in link:
                yield scrapy.Request(url=link, callback=self.parse)

    def parse_priority(self, response):
        content = response.xpath("//div[contains(@class, 'parawithrte')]//*")
        headerContentScraped = {}
        lastH2 = None
        webpageScraped = ""
        webtextScraped = ""
        payload = {}
        for tag in content:
            if tag.xpath("name()").get() == "h2":
                lastH2 = bs(tag.get(), "html.parser").find(text=True)
                webpageScraped = ""
                webtextScraped = ""
            else:
                if lastH2:
                    if lastH2 in headerContentScraped:
                        #if lastH2 == payload["heading"]:
                         webpageScraped = webpageScraped + tag.get().strip().replace(
                             "  ", ""
                         )
                         webtextScraped = webtextScraped + " ".join(
                             bs(
                                tag.get().strip().replace("  ", ""), "html.parser"
                            ).findAll(text=True)
                         ).replace("\n", "")
                    else:
                        webpageScraped = tag.get().strip().replace("  ", "")
                        webtextScraped = " ".join(
                            bs(
                                tag.get().strip().replace("  ", ""), "html.parser"
                            ).findAll(text=True)
                        ).replace("\n", "")
            headerContentScraped[lastH2] = {
                "html": "HTML CONTENT",
                "text": webtextScraped,
            }
        for heading in headerContentScraped:
            if heading:
                payload = {
                    "heading": heading,
                    "html": headerContentScraped[heading]["html"],
                    "text": headerContentScraped[heading]["text"],
                    "source": response.url,
                }
                # Uncomment to dump data to json
                self.scraped[len(self.scraped)] = payload
                #with open("scraped-data.json", "w") as f:
                  #json.dump(content, f)
                return

    def parse(self, response):

        content = response.xpath("//div[contains(@class, 'parawithrte')]//*")
        headerContentScraped = {}
        lastH2 = None
        webpageScraped = ""
        webtextScraped = ""
        payload  = {}
        for tag in content:
            if tag.xpath("name()").get() == "h2":
                lastH2 = bs(tag.get(), "html.parser").find(text=True)
                webpageScraped = ""
                webtextScraped = ""
            else:
                if lastH2:
                    if lastH2 in headerContentScraped:
                      #if lastH2 == payload["heading"]:
                        webpageScraped = webpageScraped + tag.get().strip().replace(
                            "  ", ""
                        )
                        webtextScraped = webtextScraped + " ".join(
                            bs(
                                tag.get().strip().replace("  ", ""), "html.parser"
                            ).findAll(text=True)
                        ).replace("\n", "")
                    else:
                        webpageScraped = tag.get().strip().replace("  ", "")
                        webtextScraped = " ".join(
                            bs(
                                tag.get().strip().replace("  ", ""), "html.parser"
                            ).findAll(text=True)
                        ).replace("\n", "")
            headerContentScraped[lastH2] = {
                # can scrape html content if required
                #"html": webpageScraped,
                "html": "HTML CONTENT",
                "text": webtextScraped,
            }
        for heading in headerContentScraped:
            if heading:
                payload = {
                    "heading": heading,
                    "html": headerContentScraped[heading]["html"],
                    "text": headerContentScraped[heading]["text"],
                    "source": response.url,
                }
                # Uncomment to dump data to json
                
                self.scraped[len(self.scraped)] = payload
            #with open("scraped-data.json", "w") as f:
                  #json.dump(content, f)

pObj=pd.read_json(r"C:\Users\KIIT\OneDrive\Documents\scraper\scraper\scraped-data.json",orient='index')
csvDataset=pObj.to_csv('dataset,csv',index=False)
# print(csvDataset)