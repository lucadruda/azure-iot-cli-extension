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


class CommandTest(Model):
    """CommandTest.

    :param command:
    :type command: ~product.models.CommandModel
    :param payload:
    :type payload: str
    :param expected_result:
    :type expected_result: str
    :param priority:
    :type priority: int
    :param validation_timeout:
    :type validation_timeout: int
    :param is_mandatory:
    :type is_mandatory: bool
    :param should_validate:
    :type should_validate: bool
    """

    _attribute_map = {
        'command': {'key': 'command', 'type': 'CommandModel'},
        'payload': {'key': 'payload', 'type': 'str'},
        'expected_result': {'key': 'expectedResult', 'type': 'str'},
        'priority': {'key': 'priority', 'type': 'int'},
        'validation_timeout': {'key': 'validationTimeout', 'type': 'int'},
        'is_mandatory': {'key': 'isMandatory', 'type': 'bool'},
        'should_validate': {'key': 'shouldValidate', 'type': 'bool'},
    }

    def __init__(self, *, command=None, payload: str=None, expected_result: str=None, priority: int=None, validation_timeout: int=None, is_mandatory: bool=None, should_validate: bool=None, **kwargs) -> None:
        super(CommandTest, self).__init__(**kwargs)
        self.command = command
        self.payload = payload
        self.expected_result = expected_result
        self.priority = priority
        self.validation_timeout = validation_timeout
        self.is_mandatory = is_mandatory
        self.should_validate = should_validate