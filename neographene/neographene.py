from typing import Union

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


def schema_to_neomodel(schema: Union[graphene.ObjectType, graphene.Interface]) -> neomodel.StructuredNode:
    neomodel_dict = {}
    for field_name, field_instance in dict(schema.fields).items():
        neomodel_dict[field_name] = graphene_to_neomodel_dict[field_instance.__class__]

    return graphene.ObjectType(neomodel_dict)


def neomodel_to_graphene_schema(neomodel: StructuredNode) -> graphene.ObjectType:
    graphene_schema_dict = {}
    for field_name, field_instance in dict(neomodel.__all_properties__).items():
        graphene_schema_dict[field_name] = neomodel_to_graphene_dict[field_instance.__class__]

    return graphene.ObjectType(graphene_schema_dict)


def class_factory():
    pass
