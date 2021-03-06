# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class IncomingRelationship(Model):
    """An incoming relationship.

    :param relationship_id: A user-provided string representing the id of this
     relationship, unique in the context of the source digital twin, i.e.
     sourceId + relationshipId is unique in the context of the service.
    :type relationship_id: str
    :param source_id: The id of the source digital twin.
    :type source_id: str
    :param relationship_name: The name of the relationship.
    :type relationship_name: str
    :param relationship_link: Link to the relationship, to be used for
     deletion.
    :type relationship_link: str
    """

    _attribute_map = {
        'relationship_id': {'key': '$relationshipId', 'type': 'str'},
        'source_id': {'key': '$sourceId', 'type': 'str'},
        'relationship_name': {'key': '$relationshipName', 'type': 'str'},
        'relationship_link': {'key': '$relationshipLink', 'type': 'str'},
    }

    def __init__(self, *, relationship_id: str=None, source_id: str=None, relationship_name: str=None, relationship_link: str=None, **kwargs) -> None:
        super(IncomingRelationship, self).__init__(**kwargs)
        self.relationship_id = relationship_id
        self.source_id = source_id
        self.relationship_name = relationship_name
        self.relationship_link = relationship_link
