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


class Twin(Model):
    """The state information for a device or module. This is implicitly created
    and deleted when the corresponding device/ module identity is created or
    deleted in the IoT Hub.

    :param device_id: The unique identifier of the device in the identity
     registry of the IoT Hub. It is a case-sensitive string (up to 128 char
     long) of ASCII 7-bit alphanumeric chars, and the following special
     characters {'-', ':', '.', '+', '%', '_', '#', '*', '?', '!', '(', ')',
     ',', '=', '@', ';', '$', '''}.
    :type device_id: str
    :param module_id: The unique identifier of the module in the identity
     registry of the IoT Hub. It is a case-sensitive string (up to 128 char
     long) of ASCII 7-bit alphanumeric chars, and the following special
     characters {'-', ':', '.', '+', '%', '_', '#', '*', '?', '!', '(', ')',
     ',', '=', '@', ';', '$', '''}.
    :type module_id: str
    :param tags: The collection of key-value pairs read and written by the
     solution back end. They are not visible to device apps. They keys are
     UTF-8 encoded, case-sensitive and up-to 1KB in length. Allowed characters
     exclude UNICODE control characters (segments C0 and C1), '.', '$' and
     space. The values are JSON objects, up-to 4KB in length.
    :type tags: dict[str, object]
    :param properties: The desired and reported properties of the twin.
    :type properties: ~service.models.TwinProperties
    :param etag: The string representing a ETag for the device twin, as per
     RFC7232.
    :type etag: str
    :param version: The version for the device twin including tags and desired
     properties
    :type version: long
    :param device_etag: The string representing a ETag for the device, as per
     RFC7232.
    :type device_etag: str
    :param status: The enabled status of the device. If disabled, the device
     cannot connect to the service. Possible values include: 'enabled',
     'disabled'
    :type status: str or ~service.models.enum
    :param status_reason: The reason for the current status of the device, if
     any.
    :type status_reason: str
    :param status_update_time: The date and time when the status of the device
     was last updated.
    :type status_update_time: datetime
    :param connection_state: The connection state of the device. Possible
     values include: 'Disconnected', 'Connected'
    :type connection_state: str or ~service.models.enum
    :param last_activity_time: The date and time when the device last
     connected or received or sent a message. The date and time is sepecified
     in ISO8601 datetime format in UTC, for example, 2015-01-28T16:24:48.789Z.
     This value is not updated if the device uses the HTTP/1 protocol to
     perform messaging operations.
    :type last_activity_time: datetime
    :param cloud_to_device_message_count: The number of cloud-to-device
     messages sent.
    :type cloud_to_device_message_count: int
    :param authentication_type: The authentication type used by the device.
     Possible values include: 'sas', 'selfSigned', 'certificateAuthority',
     'none'
    :type authentication_type: str or ~service.models.enum
    :param x509_thumbprint: The X509 thumbprint of the device.
    :type x509_thumbprint: ~service.models.X509Thumbprint
    :param capabilities:
    :type capabilities: ~service.models.DeviceCapabilities
    :param device_scope: The scope of the device.
    :type device_scope: str
    :param parent_scopes: The scopes of the upper level edge devices if
     applicable. Only available for edge devices.
    :type parent_scopes: list[str]
    """

    _attribute_map = {
        'device_id': {'key': 'deviceId', 'type': 'str'},
        'module_id': {'key': 'moduleId', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{object}'},
        'properties': {'key': 'properties', 'type': 'TwinProperties'},
        'etag': {'key': 'etag', 'type': 'str'},
        'version': {'key': 'version', 'type': 'long'},
        'device_etag': {'key': 'deviceEtag', 'type': 'str'},
        'status': {'key': 'status', 'type': 'str'},
        'status_reason': {'key': 'statusReason', 'type': 'str'},
        'status_update_time': {'key': 'statusUpdateTime', 'type': 'iso-8601'},
        'connection_state': {'key': 'connectionState', 'type': 'str'},
        'last_activity_time': {'key': 'lastActivityTime', 'type': 'iso-8601'},
        'cloud_to_device_message_count': {'key': 'cloudToDeviceMessageCount', 'type': 'int'},
        'authentication_type': {'key': 'authenticationType', 'type': 'str'},
        'x509_thumbprint': {'key': 'x509Thumbprint', 'type': 'X509Thumbprint'},
        'capabilities': {'key': 'capabilities', 'type': 'DeviceCapabilities'},
        'device_scope': {'key': 'deviceScope', 'type': 'str'},
        'parent_scopes': {'key': 'parentScopes', 'type': '[str]'},
    }

    def __init__(self, *, device_id: str=None, module_id: str=None, tags=None, properties=None, etag: str=None, version: int=None, device_etag: str=None, status=None, status_reason: str=None, status_update_time=None, connection_state=None, last_activity_time=None, cloud_to_device_message_count: int=None, authentication_type=None, x509_thumbprint=None, capabilities=None, device_scope: str=None, parent_scopes=None, **kwargs) -> None:
        super(Twin, self).__init__(**kwargs)
        self.device_id = device_id
        self.module_id = module_id
        self.tags = tags
        self.properties = properties
        self.etag = etag
        self.version = version
        self.device_etag = device_etag
        self.status = status
        self.status_reason = status_reason
        self.status_update_time = status_update_time
        self.connection_state = connection_state
        self.last_activity_time = last_activity_time
        self.cloud_to_device_message_count = cloud_to_device_message_count
        self.authentication_type = authentication_type
        self.x509_thumbprint = x509_thumbprint
        self.capabilities = capabilities
        self.device_scope = device_scope
        self.parent_scopes = parent_scopes
