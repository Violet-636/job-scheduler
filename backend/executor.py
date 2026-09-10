import threading
import time
import random
from datetime import datetime
from typing import List

from errors import JobExecutionError
from models import Job


class Executor:
    def __init__(self, jobs: List[Job]):
        self.jobs = jobs

    def _ts(self):
        return datetime.now().strftime("%H:%M:%S")

    def run_job(self, job: Job):
        try:
            print(f"[{self._ts()}] Starting job {job.job_id}")

            time.sleep(random.uniform(1, 3))

            if random.random() < 0.2:
                raise JobExecutionError(job.job_id)

            job.execute()
            job.mark_done()

            print(f"[{self._ts()}] Completed job {job.job_id}")

        except JobExecutionError as error:
            job.status = "failed"
            print(
                f"[{self._ts()}] Job {error.job_id} failed: {error}"
            )

    def run(self):
        threads = []

        for job in self.jobs:
            thread = threading.Thread(
                target=self.run_job,
                args=(job,)
            )
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()