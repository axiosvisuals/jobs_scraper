import csv
from datetime import datetime
from jobspy import scrape_jobs

now = str(datetime.now())
filename = "jobs_" + now + ".csv"

jobs = scrape_jobs(
    site_name=["indeed"],
    #search_term="software engineer",
    #job_type="fulltime",
    location="New York, NY",
    distance=50,
    results_wanted=1000,
    hours_old=2, # (only Linkedin/Indeed is hour specific, others round up to days old)
    country_indeed='USA',  # only needed for indeed / glassdoor
    
    # linkedin_fetch_description=True # get full description , direct job url , company industry and job level (seniority level) for linkedin (slower)
    # proxies=["208.195.175.46:65095", "208.195.175.45:65095", "localhost"],
    
)
print(f"Found {len(jobs)} jobs")
print(jobs.head())
jobs.to_csv(filename, quoting=csv.QUOTE_NONNUMERIC, escapechar="\\", index=False) # to_excel