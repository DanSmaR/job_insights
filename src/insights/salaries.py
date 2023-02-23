from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    jobs_data = read(path)
    max_salaries = list(map(lambda job: job["max_salary"], jobs_data))
    valid_max_salaries = [
        max_salary
        for max_salary in max_salaries
        if max_salary and max_salary.isdigit()
    ]
    max_salaries_converted_to_int = list(
        map(lambda salary: int(salary), valid_max_salaries)
    )
    return max(max_salaries_converted_to_int)


def get_min_salary(path: str) -> int:
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    jobs_data = read(path)
    min_salaries = list(map(lambda job: job["min_salary"], jobs_data))
    valid_min_salaries = [
        min_salary
        for min_salary in min_salaries
        if min_salary and min_salary.isdigit()
    ]
    min_salaries_converted_to_int = list(
        map(lambda salary: int(salary), valid_min_salaries)
    )
    return min(min_salaries_converted_to_int)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    if (job.get("min_salary", False) is False) or (
        job.get("max_salary", False) is False
    ):
        raise ValueError
    try:
        int_max_salary = int(job["max_salary"])
        int_min_salary = int(job["min_salary"])
        int_salary = int(salary)
    except TypeError:
        raise ValueError
    if int_min_salary > int_max_salary:
        raise ValueError
    return int_min_salary <= int_salary <= int_max_salary


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    def check_salary_matches(job: Dict) -> bool:
        try:
            return matches_salary_range(job, salary)
        except ValueError:
            return False
    return [
        job
        for job in jobs
        if check_salary_matches(job)
    ]
