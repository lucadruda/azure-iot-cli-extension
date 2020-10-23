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


def list_devices(cmd, app_id: str, token=None, central_dns_suffix=CENTRAL_ENDPOINT):
    provider = CentralDeviceProvider(cmd=cmd, app_id=app_id, token=token)
    return provider.list_devices()


def get_device(
    cmd, app_id: str, device_id: str, token=None, central_dns_suffix=CENTRAL_ENDPOINT,
):
    provider = CentralDeviceProvider(cmd=cmd, app_id=app_id, token=token)
    return provider.get_device(device_id)


def create_device(
    cmd,
    app_id: str,
    device_id: str,
    device_name=None,
    instance_of=None,
    simulated=False,
    token=None,
    central_dns_suffix=CENTRAL_ENDPOINT,
):
    if simulated and not instance_of:
        raise CLIError(
            "Error: if you supply --simulated you must also specify --instance-of"
        )
    provider = CentralDeviceProvider(cmd=cmd, app_id=app_id, token=token)
    return provider.create_device(
        device_id=device_id,
        device_name=device_name,
        instance_of=instance_of,
        simulated=simulated,
        central_dns_suffix=central_dns_suffix,
    )

def simulate_device(cmd,app_id:str,device_id:str,telemetry=None,properties=None,device_name=None,instance_of=None,token=None,
    central_dns_suffix=CENTRAL_ENDPOINT):
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
    import asyncio
    from random import randint
    from iotc import IOTCConnectType, IOTCLogLevel, IOTCEvents
    from iotc.aio import IoTCClient

    scope_id = credentials['idScope']
    key = credentials['symmetricKey']['primaryKey']

    def get_random_string(length):
        letters = string.ascii_lowercase
        return ''.join(choice(letters) for i in range(length))

    if telemetry:
        telemetry_obj = {}
        fields = telemetry.split(',')
        if len(fields) > 0:
            for field in fields:
                field_data = field.split('=')
                if len(field_data) > 0:
                    telemetry_obj[field_data[0]]=field_data[1]

    if properties:
        properties_obj = {}
        fields = properties.split(',')
        if len(fields) > 0:
            for field in fields:
                field_data = field.split('=')
                if len(field_data) > 0:
                    properties_obj[field_data[0]]=field_data[1]

    # optional model Id for auto-provisioning
    try:
        model_id = instance_of
    except:
        model_id = None


    async def on_props(propName, propValue):
        print(propValue)
        return True


    async def on_commands(command, ack):
        print(command.name)
        await ack(command.name, 'Command received', command.request_id)

    async def on_enqueued_commands(command_name,command_data):
        print(command_name)
        print(command_data)

    # change connect type to reflect the used key (device or group)
    client = IoTCClient(device_id, scope_id,
                    IOTCConnectType.IOTC_CONNECT_DEVICE_KEY, key)
    if model_id != None:
        client.set_model_id(model_id)

    client.on(IOTCEvents.IOTC_PROPERTIES, on_props)
    client.on(IOTCEvents.IOTC_COMMAND, on_commands)
    client.on(IOTCEvents.IOTC_ENQUEUED_COMMAND, on_enqueued_commands)

    # iotc.setQosLevel(IOTQosLevel.IOTC_QOS_AT_MOST_ONCE)

    async def command_loop(device_client):
        while True:
            # Wait for unknown method calls
            method_request = (await device_client.receive_method_request())
            print('Received command {}'.format(method_request.name))
            await device_client.send_method_response(MethodResponse.create_from_method_request(
                method_request, 200, {
                    'result': True, 'data': 'Command received'}
            ))

    async def main():
        await client.connect()
        print("Device connected!")
        if properties_obj:
            await client.send_property({k: (str(randint(20, 45)) if v == "number" else get_random_string(6)) for (k,v) in properties_obj.items()})
        while client.is_connected():
            if telemetry_obj:
                await client.send_telemetry({k: (str(randint(20, 45)) if v == "number" else get_random_string(6)) for (k,v) in telemetry_obj.items()})
            await asyncio.sleep(3)
        

    asyncio.run(main())
    
    

def delete_device(
    cmd, app_id: str, device_id: str, token=None, central_dns_suffix=CENTRAL_ENDPOINT,
):
    provider = CentralDeviceProvider(cmd=cmd, app_id=app_id, token=token)
    return provider.delete_device(device_id)


def registration_info(
    cmd, app_id: str, device_id, token=None, central_dns_suffix=CENTRAL_ENDPOINT,
):
    provider = CentralDeviceProvider(cmd=cmd, app_id=app_id, token=token,)

    return provider.get_device_registration_info(
        device_id=device_id, central_dns_suffix=central_dns_suffix, device_status=None,
    )


def run_command(
    cmd,
    app_id: str,
    device_id: str,
    interface_id: str,
    command_name: str,
    content: str,
    token=None,
    central_dns_suffix=CENTRAL_ENDPOINT,
):
    if not isinstance(content, str):
        raise CLIError("content must be a string: {}".format(content))

    payload = utility.process_json_arg(content, argument_name="content")

    provider = CentralDeviceProvider(cmd=cmd, app_id=app_id, token=token)
    return provider.run_component_command(
        device_id=device_id,
        interface_id=interface_id,
        command_name=command_name,
        payload=payload,
    )


def get_command_history(
    cmd,
    app_id: str,
    device_id: str,
    interface_id: str,
    command_name: str,
    token=None,
    central_dns_suffix=CENTRAL_ENDPOINT,
):
    provider = CentralDeviceProvider(cmd=cmd, app_id=app_id, token=token)
    return provider.get_component_command_history(
        device_id=device_id, interface_id=interface_id, command_name=command_name,
    )


def registration_summary(
    cmd, app_id: str, token=None, central_dns_suffix=CENTRAL_ENDPOINT,
):
    provider = CentralDeviceProvider(cmd=cmd, app_id=app_id, token=token,)
    return provider.get_device_registration_summary(
        central_dns_suffix=central_dns_suffix,
    )


def get_credentials(
    cmd, app_id: str, device_id, token=None, central_dns_suffix=CENTRAL_ENDPOINT,
):
    provider = CentralDeviceProvider(cmd=cmd, app_id=app_id, token=token,)
    return provider.get_device_credentials(
        device_id=device_id, central_dns_suffix=central_dns_suffix,
    )


def compute_device_key(cmd, primary_key, device_id):
    return utility.compute_device_key(
        primary_key=primary_key, registration_id=device_id
    )
