from graphene import Boolean, Float, ID, Int, List, ObjectType, String, Field
from graphene.types import datetime
from graphene.types import json
from neomodel import ArrayProperty, BooleanProperty, DateProperty, DateTimeProperty, FloatProperty, IntegerProperty, \
    JSONProperty, StringProperty, StructuredNode, UniqueIdProperty


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
