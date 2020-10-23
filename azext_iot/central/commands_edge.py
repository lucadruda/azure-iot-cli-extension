# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Dev note - think of this as a controller

from knack.util import CLIError

from azext_iot.common import utility
from azext_iot.constants import CENTRAL_ENDPOINT
from azext_iot.central.providers import CentralDeviceProvider


def iot_central_edge_set_modules(cmd,app_id: str, device_id:str,content:str,token=None, central_dns_suffix=CENTRAL_ENDPOINT):
    provider = CentralDeviceProvider(cmd=cmd, app_id=app_id, token=token)
    try:
        device = provider.get_device(device_id,central_dns_suffix)
    except:
        print('Not found')
        if not instance_of:
            raise CLIError('Device does not exist. Must pass a model Id to create it during simulation')
            exit(1)
        else:
            if not device_name:
                device_name = device_id
            device = provider.create_device(device_id,device_name,instance_of)
    credentials=provider.get_device_credentials(device_id)
    print(credentials)


def iot_central_edge_deployment_metric_show():
    pass
def iot_central_edge_deployment_create():
    pass
def iot_hub_configuration_show():
    pass
def iot_central_edge_deployment_list():
    pass
def iot_hub_configuration_delete():
    pass
