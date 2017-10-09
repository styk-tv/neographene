from graphene import Boolean, Float, ID, Int, List, ObjectType, String
from graphene.types import datetime
from graphene.types import json
from neomodel import ArrayProperty, BooleanProperty, DateProperty, DateTimeProperty, FloatProperty, IntegerProperty, \
    JSONProperty, StringProperty, StructuredNode, UniqueIdProperty

graphene_types = (
    String, Int, Float, Boolean, List, datetime.DateTime, datetime.DateTime, json.JSONString, ID)
neomodel_types = (
    StringProperty, IntegerProperty, FloatProperty, BooleanProperty, ArrayProperty, DateTimeProperty, DateProperty,
    JSONProperty, UniqueIdProperty)

neomodel_to_graphene_dict = {k: v for k, v in zip(neomodel_types, graphene_types)}  # neomodel -> graphene
graphene_to_neomodel_dict = {k: v for k, v in zip(graphene_types, neomodel_types)}  # graphene -> neomodel


def ClassFactory(name, arg_names, BaseClass):
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            # here, the argnames variable is the one passed to the
            # ClassFactory call
            if key not in arg_names:
                raise TypeError("Argument %s not valid for %s"
                                % (key, self.__class__.__name__))
            setattr(self, key, value)
        BaseClass.__init__(self, name[:-len("Class")])

    newclass = type(name, (BaseClass,), {"__init__": __init__})
    return newclass

#
# class SchemaFactory(ObjectType):
#     def __init__(self, neomodel: StructuredNode):
#         super(SchemaFactory, self).__init__()
#         print(neomodel.__dict__.items())
#         for field_name, field_instance in neomodel.__dict__.items():
#             setattr(self, field_name, neomodel_to_graphene_dict[field_instance.__class__])
def SchemaFactory(neomodel):
    return ClassFactory(ObjectType, neomodel.__dict__.items())


class NodeFactory(StructuredNode):
    def __init__(self, schema: ObjectType):
        super(NodeFactory, self).__init__()
        print(schema.__dict__.items())
        for field_name, field_instance in schema.__dict__.items():
            setattr(self, field_name, graphene_to_neomodel_dict[field_instance.__class__])
