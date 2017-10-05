import graphene
from neomodel import StructuredNode, UniqueIdProperty, StringProperty


class TestQuery(graphene.ObjectType):
    uid = graphene.ID()
    text = graphene.String()


class TestNode(StructuredNode):
    uid = UniqueIdProperty()
    text = StringProperty(required=True)
