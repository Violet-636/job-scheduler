class JobExecutionError(Exception):
    def __init__(self, job_id, message="Job execution failed"):
        self.job_id = job_id
        super().__init__(message)