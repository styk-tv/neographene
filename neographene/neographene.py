from graphene import Boolean, Field, Float, ID, Int, List, ObjectType, String
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


def get_equivalent_field(field_type):
    if field_type in neomodel_to_graphene_dict.keys():
        return neomodel_to_graphene_dict[field_type]
    elif field_type in graphene_to_neomodel_dict.keys():
        return graphene_to_neomodel_dict[field_type]
    else:
        raise Exception('There are no equivalent type for type ', field_type)


def ClassFactory(name, BaseClass, class_dict):
    new_class = type(name, (BaseClass,), class_dict)
    return new_class


#
# class SchemaFactory(ObjectType):
#     def __init__(self, neomodel: StructuredNode):
#         super(SchemaFactory, self).__init__()
#         print(neomodel.__dict__.items())
#         for field_name, field_instance in neomodel.__dict__.items():
#             setattr(self, field_name, neomodel_to_graphene_dict[field_instance.__class__])
def SchemaFactory(class_name, neomodel_class):
    schema_dict = dict()
    print("+++++++")
    neomodel_class.__dict__.items()
    print("+++++++")
    for field_name, field_instance in neomodel_class.__dict__.items():
        print(field_name, field_instance)
        schema_dict[field_name] = get_equivalent_field(field_instance)
    return ClassFactory(class_name, ObjectType, schema_dict)


# class NodeFactory(StructuredNode):
#     def __init__(self, schema: ObjectType):
#         super(NodeFactory, self).__init__()
#         print(schema.__dict__.items())
#         for field_name, field_instance in schema.__dict__.items():
#             setattr(self, field_name, graphene_to_neomodel_dict[field_instance.__class__])

def NodeFactory(class_name, schema_class):
    node_dict = dict()
    print("+++++++")
    schema_class.__dict__.items()
    print("+++++++")
    for field_name, field_instance in schema_class._meta.local_fields.items():
        print(field_name, field_instance)

        node_dict[field_name] = get_equivalent_field(field_instance.type().__class__)
    return ClassFactory(class_name, StructuredNode, node_dict)


class TestSchema(ObjectType):
    field1 = Field(String)
    field2 = Field(Int)
    field3 = Field(Float)
    field4 = Field(Boolean)
    field5 = List(String)
    field6 = Field(datetime.DateTime())
    field7 = Field(datetime.DateTime())
    field8 = Field(json.JSONString())
    field8 = Field(ID())


class TestNode(StructuredNode):
    field1 = StringProperty()
    field2 = IntegerProperty()
    field3 = FloatProperty()
    field4 = BooleanProperty()
    field5 = ArrayProperty()
    field6 = DateTimeProperty()
    field7 = DateProperty()
    field8 = JSONProperty()
    field8 = UniqueIdProperty()


test_schema = TestSchema
print(test_schema._meta.local_fields)
print(NodeFactory('TestNode', test_schema))
