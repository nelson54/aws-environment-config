import unittest
from environment_config.options import Options

class TestOptions(unittest.TestCase):

    def test_defaults(self):
        opt = Options()
        self.assertTrue(opt.has_environment(), True)
        self.assertEqual(opt.get_base_file(), 'settings/config.properties')
        self.assertEqual(opt.get_environment_file(), 'settings/config-local.properties')

    def test_no_environment(self):
        opt = Options(environment=None)
        self.assertFalse(opt.has_environment())
        self.assertFalse(opt.get_environment_file())

if __name__ == '__main__':
    unittest.main()