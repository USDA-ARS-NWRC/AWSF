import os
import shutil
import unittest

from inicheck.tools import get_user_config

import awsm


class AWSMTestCase(unittest.TestCase):
    """
    The base test case for SMRF that will load in the configuration file and
    store as the base config. Also will remove the output directory upon
    tear down.
    """

    @classmethod
    def setUpClass(cls):
        cls.test_dir = os.path.abspath(os.path.join(
            os.path.dirname(awsm.__file__), '..', 'tests'
        ))

    def tearDown(self):
        """
        Clean up the output directory
        """
        if hasattr(self, 'cache_run') and self.cache_run:
            return
        elif hasattr(self, 'run_dir') and self.run_dir:
            folder = os.path.join(self.run_dir, 'output')
            no_delete = os.path.join(folder, '.keep')
            for the_file in os.listdir(folder):
                file_path = os.path.join(folder, the_file)
                if file_path != no_delete:
                    try:
                        if os.path.isfile(file_path):
                            os.unlink(file_path)
                        elif os.path.isdir(file_path):
                            shutil.rmtree(file_path)
                    except Exception as e:
                        print(e)
