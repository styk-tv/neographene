from neographene.neographene import SchemaFactory, NodeFactory
from tests.fixtures import TestNode, TestSchema


def test_print():
    assert SchemaFactory(TestNode()).__dict__ == TestSchema()
    assert NodeFactory(TestSchema()).__dict__ == TestNode()
