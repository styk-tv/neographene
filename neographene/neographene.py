import graphene
import neomodel
from graphene.types import datetime, json
from neomodel import StructuredNode

graphene_types = (graphene.String, graphene.Int, graphene.Float, graphene.Boolean, graphene.List,
                  datetime.DateTime, datetime.DateTime, json.JSONString, graphene.ID)
neomodel_types = (neomodel.StringProperty, neomodel.IntegerProperty, neomodel.FloatProperty,
                  neomodel.BooleanProperty, neomodel.ArrayProperty, neomodel.DateTimeProperty,
                  neomodel.DateProperty, neomodel.JSONProperty, neomodel.UniqueIdProperty)

neomodel_to_graphene_dict = {k: v for k, v in zip(neomodel_types, graphene_types)}  # neomodel -> graphene
graphene_to_neomodel_dict = {k: v for k, v in zip(graphene_types, neomodel_types)}  # graphene -> neomodel


class SchemaFactory(graphene.ObjectType):
    def __init__(self, neomodel: StructuredNode):
        for field_name, field_instance in neomodel.__dict__.items():
            setattr(self, field_name, neomodel_to_graphene_dict[field_instance])

    def get_schema(self):
        return self


class NodeFactory(neomodel.StructuredNode):
    def __init__(self, schema: graphene.ObjectType):
        for field_name, field_instance in schema.__dict__.items():
            setattr(self, field_name, graphene_to_neomodel_dict[field_instance])

    def get_node(self):
        return self


class TestSchema(graphene.ObjectType):
    def __init__(self):
        for index, type in enumerate(graphene_types):
            setattr(self, "field" + str(index), type)


class TestNode(StructuredNode):
    def __init__(self):
        for index, type in enumerate(neomodel_types):
            setattr(self, "field" + str(index), type)

print("+++++++++++++Schema Factory+++++++++++++++++++")
print(SchemaFactory(TestNode()).get_schema())
print(isinstance(SchemaFactory(TestNode()).get_schema(), graphene.ObjectType))
print("+++++++++++++Node   Factory+++++++++++++++++++")
print(NodeFactory(TestSchema()).get_node())
print(isinstance(NodeFactory(TestSchema()).get_node(), neomodel.StructuredNode))

