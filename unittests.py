import unittest
import os
from tempfile import NamedTemporaryFile
from xor_merge import xor_merge, read_file  # Assuming script name is xor_merge_script.py

class TestXorMerge(unittest.TestCase):
    def setUp(self):
        """Create temporary files for testing."""
        self.file1 = NamedTemporaryFile(delete=False, mode="w+")
        self.file2 = NamedTemporaryFile(delete=False, mode="w+")
        self.out1 = "output1.txt"
        self.out2 = "output2.txt"

    def tearDown(self):
        """Clean up temporary files after each test."""
        os.remove(self.file1.name)
        os.remove(self.file2.name)
        if os.path.exists(self.out1):
            os.remove(self.out1)
        if os.path.exists(self.out2):
            os.remove(self.out2)

    def write_to_file(self, file, content):
        """Helper function to write content to a temporary file."""
        file.writelines(content)
        file.seek(0)

    def read_output(self, filename):
        """Helper function to read content from output files."""
        with open(filename, "r") as f:
            return f.readlines()

    def test_xor_merge_basic(self):
        """Test basic functionality with distinct sorted lines."""
        content1 = ["apple\n", "banana\n", "cherry\n"]
        content2 = ["banana\n", "date\n", "fig\n"]

        self.write_to_file(self.file1, content1)
        self.write_to_file(self.file2, content2)

        xor_merge(self.file1.name, self.file2.name)

        self.assertEqual(self.read_output(self.out1), ["apple\n", "cherry\n"])
        self.assertEqual(self.read_output(self.out2), ["date\n", "fig\n"])

    def test_xor_merge_identical_files(self):
        """Test case where both files contain the same lines."""
        content = ["apple\n", "banana\n", "cherry\n"]
        self.write_to_file(self.file1, content)
        self.write_to_file(self.file2, content)

        xor_merge(self.file1.name, self.file2.name)

        self.assertEqual(self.read_output(self.out1), [])
        self.assertEqual(self.read_output(self.out2), [])

    def test_xor_merge_one_empty_file(self):
        """Test case where one file is empty."""
        content1 = ["apple\n", "banana\n", "cherry\n"]
        self.write_to_file(self.file1, content1)

        xor_merge(self.file1.name, self.file2.name)

        self.assertEqual(self.read_output(self.out1), ["apple\n", "banana\n", "cherry\n"])
        self.assertEqual(self.read_output(self.out2), [])

    def test_xor_merge_both_empty_files(self):
        """Test case where both files are empty."""
        xor_merge(self.file1.name, self.file2.name)
        self.assertEqual(self.read_output(self.out1), [])
        self.assertEqual(self.read_output(self.out2), [])

    def test_xor_merge_subset_case(self):
        """Test case where one file is a subset of the other."""
        content1 = ["apple\n", "banana\n", "cherry\n"]
        content2 = ["banana\n"]
        self.write_to_file(self.file1, content1)
        self.write_to_file(self.file2, content2)

        xor_merge(self.file1.name, self.file2.name)

        self.assertEqual(self.read_output(self.out1), ["apple\n", "cherry\n"])
        self.assertEqual(self.read_output(self.out2), [])

    def test_xor_merge_duplicate_lines(self):
        """Test case where both files contain the same lines, but one contains a duplicate."""
        content = ["banana\n"]
        self.write_to_file(self.file1, content)
        self.write_to_file(self.file2, content + content)
        xor_merge(self.file1.name, self.file2.name)

        self.assertEqual(self.read_output(self.out1), [])
        self.assertEqual(self.read_output(self.out2), [])

if __name__ == "__main__":
    unittest.main()
