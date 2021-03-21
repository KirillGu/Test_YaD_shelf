import unittest
from shelf import add_new_doc, delete_doc



class DocuTests(unittest.TestCase):

	def test_ap(self):
		self.assertEqual(add_new_doc('11', 'doc', 'kirill', '3'), '3')

	def test_del(self):
		self.assertEqual(delete_doc('11-2'), ('11-2', True))


if __name__ == "__main__":
  unittest.main()
