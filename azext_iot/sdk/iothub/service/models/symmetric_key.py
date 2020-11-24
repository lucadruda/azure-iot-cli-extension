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


class SymmetricKey(Model):
    """SymmetricKey.

    :param primary_key: The base64 encoded primary key of the device.
    :type primary_key: str
    :param secondary_key: The base64 encoded secondary key of the device.
    :type secondary_key: str
    """

    _attribute_map = {
        'primary_key': {'key': 'primaryKey', 'type': 'str'},
        'secondary_key': {'key': 'secondaryKey', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(SymmetricKey, self).__init__(**kwargs)
        self.primary_key = kwargs.get('primary_key', None)
        self.secondary_key = kwargs.get('secondary_key', None)
