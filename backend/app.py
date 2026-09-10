from models import EmailJob, DataProcessingJob
from task_manager import TaskManager
from executor import Executor


def build_jobs():
    return [
        EmailJob(
            1,
            "student1@example.com"
        ),
        DataProcessingJob(
            2,
            "sales.csv"
        ),
        EmailJob(
            3,
            "manager@example.com"
        ),
        DataProcessingJob(
            4,
            "customers.csv"
        )
    ]


if __name__ == "__main__":
    jobs = build_jobs()

    manager = TaskManager()

    for job in jobs:
        manager.add_job(job)

    executor = Executor(jobs)
    executor.run()

    print("\nJob summary:")

    for status, status_jobs in manager.get_all().items():
        print(f"{status}: {len(status_jobs)} job(s)")

        for job in status_jobs:
            print(
                f"  Job {job.job_id}: "
                f"{job.description}"
            )