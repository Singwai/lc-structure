import unittest

from lc_structure.Node import Node


class MyTestCase(unittest.TestCase):
    def test_init_with_val(self):
        node = Node(1)

        self.assertEqual(node.val, 1)
        self.assertIsNone(node.children)


if __name__ == '__main__':
    unittest.main()
