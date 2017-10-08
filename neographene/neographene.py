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


class SchemaFactory(graphene.ObjectType, object):
    def __init__(self, neomodel: StructuredNode):
        for field_name, field_instance in neomodel.__dict__.items():
            setattr(self, field_name, neomodel_to_graphene_dict[field_instance])


class NodeFactory(neomodel.StructuredNode, object):
    def __init__(self, schema: graphene.ObjectType):
        for field_name, field_instance in schema.__dict__.items():
            setattr(self, field_name, graphene_to_neomodel_dict[field_instance])
