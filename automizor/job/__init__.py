from ._job import JSON, Job


def get_context() -> dict:
    """
    Retrieves the context of the current job, which contains necessary information
    for job execution.

    Returns:
        A dictionary with the job's context.

    Raises:
        AutomizorJobError: If retrieving the job context fails.
    """

    job = Job()
    return job.get_context()


def set_result(name: str, value: JSON):
    """
    Saves the result of the job execution to a local JSON file (`output/result.json`).
    The `Automizor Agent` uploads this file to the `Automizor Platform` after the job.

    Parameters:
        name: The key under which to store the result.
        value: The result value, must be JSON serializable.

    Note: Errors during file operations will raise unhandled exceptions.
    """

    job = Job()
    return job.set_result(name, value)


__all__ = [
    "get_context",
    "set_result",
]
