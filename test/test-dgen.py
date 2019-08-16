import sys
sys.path.insert(1, '../dgen')

import unittest
import mock
from dgen import *
import dgen_model
from dgen_model import dgen_project

class BuildTest(unittest.TestCase):

    # Print functions
    def logTestStart(self, name):
        print ('-'*100)
        print ('Testing: ' + name)
        print ('-'*100)

    def logTestEnd(self, result):
        print ('\nTest Passed' if result else 'Test Failed')

    def checkFile(self, filepath):
        exists = os.path.exists(filepath)
        stdout = '%s...%r' % (filepath, exists)
        stdout = stdout.replace('...', '.' * (100 - len(stdout)))
        print (stdout)
        return exists

    # Generate a dgen document
    @mock.patch('sys.argv', ['../dgen/dgen.py'])
    def test_generate_document(self):
        self.logTestStart('Document Generation')
        global document
        document = dgen()
        self.logTestEnd(document is not None)
    
    # Test files have been created
    def test_generated_files(self):
        self.logTestStart('Generated Files')
        
        html_dir = document.project.filename + '-html'
        
        results = [
            self.checkFile(html_dir),
            self.checkFile(html_dir + '/css'),
            self.checkFile(html_dir + '/document_information.html'),
            self.checkFile(html_dir + '/footer.html'),
            self.checkFile(html_dir + '/header.html'),
            self.checkFile(html_dir + '/report.html'),
            self.checkFile(html_dir + '/title_page.html'),
            self.checkFile(html_dir + '/toc.template.xsl'),
            self.checkFile(document.project.filename + '.pdf')
        ]

        self.logTestEnd((results.count(False) == 0))
        self.assertTrue((results.count(False) == 0))

    # Test report PDF file attributes
    def test_report_file(self):
        self.logTestStart('Report PDF file size')
        report = document.project.filename + '.pdf'
        filesize = os.stat(report).st_size
        self.logTestEnd((filesize > 100))
        self.assertTrue(filesize > 100)

if __name__ == '__main__':
    unittest.main()