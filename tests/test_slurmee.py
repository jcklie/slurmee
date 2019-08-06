import os
import unittest

import slurmee


class TestSlurmee(unittest.TestCase):
    def setUp(self):
        os.environ["SLURM_JOB_ID"] = "5741192"
        os.environ["SLURM_JOB_NAME"] = "myjob"
        os.environ["SLURM_SUBMIT_DIR"] = "/lustre/payerle/work"
        os.environ["SLURM_JOB_NODELIST"] = "compute-b24-[1-3,5-9],compute-b25-[1,4,8]"
        os.environ["SLURM_SUBMIT_HOST"] = "login-1.deepthought2.umd.edu"
        os.environ["SLURM_JOB_NUM_NODES"] = "2"
        os.environ["SLURM_CPUS_ON_NODE"] = "8"
        os.environ["SLURM_NTASKS"] = "11"
        os.environ["SLURM_NODEID"] = "0"
        os.environ["PBS_O_VNODENUM"] = "4"
        os.environ["SLURM_PROCID"] = "0"

    def tearDown(self):
        os.environ.clear()

    def test_get_job_id(self):
        self.assertEqual(slurmee.get_job_id(), 5741192)

    def test_get_job_name(self):
        self.assertEqual(slurmee.get_job_name(), "myjob")

    def test_get_submit_dir(self):
        self.assertEqual(slurmee.get_submit_dir(), "/lustre/payerle/work")

    def test_get_job_nodelist(self):
        self.assertEqual(slurmee.get_job_nodelist(), "compute-b24-[1-3,5-9],compute-b25-[1,4,8]")

    def test_get_submit_host(self):
        self.assertEqual(slurmee.get_submit_host(), "login-1.deepthought2.umd.edu")

    def test_get_job_num_nodes(self):
        self.assertEqual(slurmee.get_job_num_nodes(), 2)

    def test_get_cpus_on_node(self):
        self.assertEqual(slurmee.get_cpus_on_node(), 8)

    def test_get_ntasks(self):
        self.assertEqual(slurmee.get_ntasks(), 11)

    def test_get_nodeid(self):
        self.assertEqual(slurmee.get_nodeid(), 0)

    def test_get_job_id_when_absent(self):
        os.environ.clear()
        self.assertEqual(slurmee.get_job_id(), None)

    def test_get_job_name_when_absent(self):
        os.environ.clear()
        self.assertEqual(slurmee.get_job_name(), None)

    def test_get_submit_dir_when_absent(self):
        os.environ.clear()
        self.assertEqual(slurmee.get_submit_dir(), None)

    def test_get_job_nodelist_when_absent(self):
        os.environ.clear()
        self.assertEqual(slurmee.get_job_nodelist(), None)

    def test_get_submit_host_when_absent(self):
        os.environ.clear()
        self.assertEqual(slurmee.get_submit_host(), None)

    def test_get_job_num_nodes_when_absent(self):
        os.environ.clear()
        self.assertEqual(slurmee.get_job_num_nodes(), None)

    def test_get_cpus_on_node_when_absent(self):
        os.environ.clear()
        self.assertEqual(slurmee.get_cpus_on_node(), None)

    def test_get_ntasks_when_absent(self):
        os.environ.clear()
        self.assertEqual(slurmee.get_ntasks(), None)

    def test_get_nodeid_when_absent(self):
        os.environ.clear()
        self.assertEqual(slurmee.get_nodeid(), None)
