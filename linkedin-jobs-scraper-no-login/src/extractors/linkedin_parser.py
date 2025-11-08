thonfrom bs4 import BeautifulSoup
import json

class LinkedInParser:
    def parse(self, html):
        soup = BeautifulSoup(html, "html.parser")
        job_elements = soup.find_all('li', {'class': 'job-result-card'})
        jobs = []

        for job in job_elements:
            job_data = {}
            job_data['job_title'] = job.find('h3').get_text(strip=True)
            job_data['company_name'] = job.find('h4').get_text(strip=True)
            job_data['location'] = job.find('span', {'class': 'job-result-card__location'}).get_text(strip=True)
            job_data['job_url'] = job.find('a')['href']
            job_data['apply_url'] = job_data['job_url']  # LinkedIn's easy apply link is often the same as job URL

            jobs.append(job_data)

        return jobs