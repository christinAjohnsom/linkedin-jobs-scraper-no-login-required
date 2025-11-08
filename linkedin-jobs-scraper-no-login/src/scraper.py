thonimport requests
from bs4 import BeautifulSoup
import json
import time
import os
from .extractors.linkedin_parser import LinkedInParser
from .outputs.exporters import Exporter

class JobScraper:
    def __init__(self, search_term, filters=None):
        self.search_term = search_term
        self.filters = filters if filters else {}
        self.base_url = "https://www.linkedin.com/jobs/search/"
        self.parser = LinkedInParser()
        self.exporter = Exporter()

    def build_url(self):
        params = {'keywords': self.search_term}
        params.update(self.filters)
        return f"{self.base_url}?{requests.compat.urlencode(params)}"

    def fetch_job_listings(self):
        url = self.build_url()
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception(f"Error fetching job listings: {response.status_code}")
        return response.text

    def parse_jobs(self, html):
        return self.parser.parse(html)

    def save_jobs(self, jobs):
        self.exporter.export(jobs)

    def run(self):
        html = self.fetch_job_listings()
        jobs = self.parse_jobs(html)
        self.save_jobs(jobs)

if __name__ == "__main__":
    scraper = JobScraper(search_term="Python", filters={"location": "United States", "employmentType": "full-time"})
    scraper.run()