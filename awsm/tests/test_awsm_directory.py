from inicheck.tools import cast_all_variables

from awsm.framework.framework import AWSM
from awsm.tests.awsm_test_case import AWSMTestCase


class TestStandardRME(AWSMTestCase):
    """
    Integration test for AWSM using reynolds mountain east
    """

    def assert_rme_wyhr(self, a):
        self.assertEqual(
            a.path_wy,
            str(self.basin_dir.joinpath('output/rme/wy1986/rme_test'))
        )
        self.assertEqual(
            a.pathdd,
            str(self.basin_dir.joinpath(
                'output/rme/wy1986/rme_test/data/data3337_3344'))
        )
        self.assertEqual(
            a.pathrr,
            str(self.basin_dir.joinpath(
                'output/rme/wy1986/rme_test/runs/run3337_3344'))
        )

    def test_directory_creation_wyhr(self):

        a = AWSM(self.config_file)
        self.assert_rme_wyhr(a)

    def test_directory_creation_start_end(self):

        config = self.base_config_copy()
        config.raw_cfg['paths']['folder_date_style'] = 'start_end'
        config.apply_recipes()
        config = cast_all_variables(config, config.mcfg)

        a = AWSM(config)

        self.assertEqual(
            a.path_wy,
            str(self.basin_dir.joinpath('output/rme/wy1986/rme_test'))
        )
        self.assertEqual(
            a.pathdd,
            str(self.basin_dir.joinpath(
                'output/rme/wy1986/rme_test/data/data19860217_19860217'))
        )
        self.assertEqual(
            a.pathrr,
            str(self.basin_dir.joinpath(
                'output/rme/wy1986/rme_test/runs/run19860217_19860217'))
        )

    def test_directory_creation_day(self):

        config = self.base_config_copy()
        config.raw_cfg['paths']['folder_date_style'] = 'day'
        config.apply_recipes()
        config = cast_all_variables(config, config.mcfg)

        a = AWSM(config)

        self.assertEqual(
            a.path_wy,
            str(self.basin_dir.joinpath('output/rme/wy1986/rme_test'))
        )
        self.assertEqual(
            a.pathdd,
            str(self.basin_dir.joinpath(
                'output/rme/wy1986/rme_test/data/data19860217'))
        )
        self.assertEqual(
            a.pathrr,
            str(self.basin_dir.joinpath(
                'output/rme/wy1986/rme_test/runs/run19860217'))
        )

    def test_directory_creation_multiple(self):

        a = AWSM(self.config_file)
        a2 = AWSM(self.config_file)

        self.assert_rme_wyhr(a)
        self.assert_rme_wyhr(a2)
