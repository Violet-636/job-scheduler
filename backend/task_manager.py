from collections import defaultdict
from typing import Dict, List
from models import Job


class TaskManager:
    def __init__(self):
        self.jobs = []

    def add_job(self, job: Job):
        self.jobs.append(job)

    def get_all(self) -> Dict[str, List[Job]]:
        jobs_by_status = defaultdict(list)

        for job in self.jobs:
            jobs_by_status[job.status].append(job)

        return dict(jobs_by_status)

    def get_jobs_by_status(self, status: str) -> List[Job]:
        return [job for job in self.jobs if job.status == status]