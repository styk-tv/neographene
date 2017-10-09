from neographene.neographene import SchemaFactory, NodeFactory
from tests.fixtures import TestNode, TestSchema


def test_schema_factory():
    schema = TestSchema()
    node = TestNode()
    assert SchemaFactory(node).get_schema() == schema.__dict__

def test_node_factory():
    node = TestNode()
    schema = TestSchema()
    assert NodeFactory(schema).get_node() == node.__dict__
