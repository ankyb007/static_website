import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(),"<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("dev", [child_node])

        self.assertEqual(parent_node.to_html(), "<dev><span><b>grandchild</b></span></dev>")

    def test_to_html_mul_child(self):
        child_node1 = LeafNode("b", "child node 1")
        child_node2 = LeafNode("b", "child node 2")
        parent_node = ParentNode("dev", [child_node1, child_node2])
        self.assertEqual(parent_node.to_html(),"<dev><b>child node 1</b><b>child node 2</b></dev>" )

    def test_to_html_no_child(self):
        parent_node = ParentNode("span", None)
        with self.assertRaises(ValueError):
            parent_node.to_html()


if __name__ == "__main__":
    unittest.main()