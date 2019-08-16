import sys
sys.path.insert(1, '../dgen')

import unittest
import mock
from dgen import *
import dgen_model
from dgen_model import dgen_project

class BuildTest(unittest.TestCase):

    def checkFile(self, filepath):
        exists = os.path.exists(filepath)
        stdout = '%s...%r' % (filepath, exists)
        stdout = stdout.replace('...', '.' * (100 - len(stdout)))
        print (stdout)
        return exists

    # Generate a dgen document
    @mock.patch('sys.argv', ['../dgen/dgen.py'])
    def test_generate_document(self):
        global document
        document = dgen()
        self.assertTrue(True)
    
    # Test files have been created
    def test_template_files(self):
        print ('\nChecking template files exists...')
        results = []

        # Template files - Match generated files against template source
        for root, dirs, files in os.walk(document.project.template):
            for fil in files:
                results.append(self.checkFile((root + '/' + fil).replace(document.project.template, 'default')))

        # Check for HTML dir, and report.pdf
        print('Checking report files exist...')
        results.append(self.checkFile(document.project.filename + '-html'))
        results.append(self.checkFile(document.project.filename + '.pdf'))

        self.assertTrue((results.count(False) == 0))

if __name__ == '__main__':
    unittest.main()