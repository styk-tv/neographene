from tests.fixtures import TestNode, TestSchema

from neographene.neographene import NodeFactory, SchemaFactory


def test_schmea_factory():
    assert SchemaFactory(TestNode()) == TestSchema()


def test_node_factory():
    assert NodeFactory(TestSchema()) == TestNode()
