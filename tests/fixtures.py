import graphene
from neomodel import StructuredNode, UniqueIdProperty, StringProperty

from neographene.neographene import graphene_types, neomodel_types


class TestSchema(graphene.ObjectType):
    def __init__(self):
        for index, type in enumerate(graphene_types):
            setattr(self, "field" + str(index), type)


class TestNode(StructuredNode):
    def __init__(self):
        for index, type in enumerate(neomodel_types):
            setattr(self, "field" + str(index), type)
