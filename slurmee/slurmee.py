"""
A list of slurm environment variables can be found under
https://slurm.schedmd.com/sbatch.html#SECTION_OUTPUT-ENVIRONMENT-VARIABLES
"""

import os
from typing import Optional, Dict


def get_job_id() -> Optional[int]:
    """ Gets the job id.

    Returns:
        job_id: The job id if running in slurm else `None`
    """
    return _to_int(os.getenv("SLURM_JOB_ID"))


def get_job_name() -> Optional[str]:
    """ Gets the job name.

    Returns:
        job_name: The job name if running in slurm else `None`
    """
    return os.getenv("SLURM_JOB_NAME")


def get_submit_dir() -> Optional[str]:
    """ Gets the submission directory (the directory from with `srun` or
    `sbatch` was executed.

    Returns:
        submit_dir: The submission directory name if running in slurm else `None`
    """
    return os.getenv("SLURM_SUBMIT_DIR")


def get_job_nodelist() -> Optional[str]:
    """ Gets the list of nodes allocated for this job.

    The list of nodes allocated to a job is presented in a compact notation, in which
    square brackets (i.e. [ and ]) are used to delimit lists and/or ranges of numeric
    values, e.g. `compute-b24-[1-3,5-9],compute-b25-[1,4,8]`. This compact form saves
    space in the environment and in displays, but is often not the most useful in
    scripts, where a fully expanded list might be more convenient. The `scontrol`
    command or the `py-hostlist` Python package can be used for conversion.    `

    Returns:
        node_list: List of nodes allocated for this job if running in slurm else `None`
    """
    return os.getenv("SLURM_JOB_NODELIST")


def get_submit_host() -> Optional[str]:
    """ Gets the name of the submission host.

    Returns:
        submit_host: The submission host name if running in slurm else `None`
    """
    return os.getenv("SLURM_SUBMIT_HOST")


def get_job_num_nodes() -> Optional[int]:
    """ Gets the number of nodes allocated this job.

    Returns:
        num_nodes: Number of nodes allocated this job if running in slurm else `None`
    """
    return _to_int(os.getenv("SLURM_JOB_NUM_NODES"))


def get_cpus_on_node() -> Optional[int]:
    """ Gets the number of CPUs for this node.

    Returns:
        cpus_on_node: The number of CPUs on the allocated node if running in slurm else `None`.
    """
    return _to_int(os.getenv("SLURM_CPUS_ON_NODE"))


def get_ntasks() -> Optional[int]:
    """ Get the number of tasks per node.

    Returns:
        ntasks: The number of tasks per node if running in slurm else `None`.
    """
    return _to_int(os.getenv("SLURM_NTASKS"))


def get_nodeid() -> Optional[int]:
    """ Gets the node id.

    The node id is an index to node running on relative to nodes assigned to job.

    Returns:
        nodeid: The node id if running in slurm else `None`.
    """

    return _to_int(os.getenv("SLURM_NODEID"))


def get_job_array_info() -> Optional[Dict[str, int]]:
    """ Get job array information.

    Refer to https://slurm.schedmd.com/job_array.html for interpreting the returned values.

    Returns:
        job_array_info: A dict with job array information if running in slurm and inside a job array else `None`.
    :return:
    """
    d = {
        "array_job_id": "SLURM_ARRAY_JOB_ID",
        "task_id": "SLURM_ARRAY_TASK_ID",
        "task_count": "SLURM_ARRAY_TASK_COUNT",
        "task_max": "SLURM_ARRAY_TASK_MAX",
        "task_min": "SLURM_ARRAY_TASK_MIN",
    }

    if os.getenv(d["array_job_id"]) is None:
        return None

    return {k: _to_int(os.getenv(env_var)) for k, env_var in d.items()}


def _to_int(s: Optional[str]) -> Optional[int]:
    return int(s) if s else None
