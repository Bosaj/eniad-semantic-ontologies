import os
import unittest
import xml.etree.ElementTree as ET

repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


class TestOntologies(unittest.TestCase):
    def test_owl_files_integrity(self):
        ontologies_dir = os.path.join(repo_root, "Ontologies_Library")
        self.assertTrue(os.path.isdir(ontologies_dir))
        owl_files = [f for f in os.listdir(ontologies_dir) if f.endswith(".owl")]
        self.assertGreater(len(owl_files), 0, "There should be at least one .owl file")

        for owl_file in owl_files:
            owl_path = os.path.join(ontologies_dir, owl_file)
            with open(owl_path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read().strip()
            self.assertGreater(len(content), 0, f"{owl_file} must not be empty")

            if content.startswith("<?xml") or content.startswith("<rdf:RDF"):
                # XML syntax
                tree = ET.parse(owl_path)
                root = tree.getroot()
                self.assertIsNotNone(root)
                tag_lower = root.tag.lower()
                self.assertTrue("rdf" in tag_lower or "ontology" in tag_lower)
            else:
                # Turtle / Manchester / N3 syntax
                self.assertTrue(
                    "@prefix" in content or "owl:Ontology" in content or "Class:" in content,
                    f"{owl_file} should contain valid ontology definitions"
                )

    def test_curriculum_and_docs_exist(self):
        docs_dir = os.path.join(repo_root, "docs")
        self.assertTrue(os.path.isdir(docs_dir))
        self.assertTrue(os.path.exists(os.path.join(docs_dir, "ARCHITECTURE.md")))
        self.assertTrue(os.path.exists(os.path.join(docs_dir, "CURRICULUM_MATRIX.md")))


if __name__ == "__main__":
    unittest.main()
