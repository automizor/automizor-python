from automizor import exceptions, job


def test_job_singleton():
    job1 = job.Job()
    job2 = job.Job()
    assert job1 is job2
