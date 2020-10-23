# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

"""
CLI parameter definitions.
"""

from knack.arguments import CLIArgumentType, CaseInsensitiveList
from azure.cli.core.commands.parameters import get_three_state_flag
from azext_iot.monitor.models.enum import Severity
from azext_iot.central.models.enum import Role
from azext_iot._params import event_msg_prop_type, event_timeout_type

severity_type = CLIArgumentType(
    options_list=["--minimum-severity"],
    choices=CaseInsensitiveList([sev.name for sev in Severity]),
    help="Minimum severity of issue required for reporting.",
)

role_type = CLIArgumentType(
    options_list=["--role", "-r"],
    choices=CaseInsensitiveList([role.name for role in Role]),
    help="Role for the user/service-principal you are adding to the app.",
)

style_type = CLIArgumentType(
    options_list=["--style"],
    choices=CaseInsensitiveList(["scroll", "json", "csv"]),
    help="Indicate output style"
    "scroll = deliver errors as they arrive, json = summarize results as json, csv = summarize results as csv",
)


def load_central_arguments(self, _):
    """
    Load CLI Args for Knack parser
    """
    with self.argument_context("iot central") as context:
        context.argument("app_id", options_list=["--app-id", "-n"], help="Target App.")
        context.argument(
            "token",
            options_list=["--token"],
            help="Authorization token for request. "
            "More info available here: https://docs.microsoft.com/en-us/learn/modules/manage-iot-central-apps-with-rest-api/ "
            "MUST INCLUDE type (e.g. 'SharedAccessToken ...', 'Bearer ...'). "
            "Example: 'Bearer someBearerTokenHere'",
        )
        context.argument(
            "central_dns_suffix",
            options_list=["--central-dns-suffix", "--central-api-uri"],
            help="Central dns suffix. "
            "This enables running cli commands against non public/prod environments",
        )

    with self.argument_context("iot central device-template") as context:
        context.argument(
            "device_template_id",
            options_list=["--device-template-id", "--dtid"],
            help="Device template id. Example: somedevicetemplate",
        )
        context.argument(
            "content",
            options_list=["--content", "-k"],
            help="Configuration for request. "
            "Provide path to JSON file or raw stringified JSON. "
            "[File Path Example: ./path/to/file.json] "
            "[Stringified JSON Example: {'a': 'b'}] ",
        )

    with self.argument_context("iot central api-token") as context:
        context.argument(
            "token_id",
            options_list=["--token-id", "--tkid"],
            help="Unique ID for the API token. ",
        )
        context.argument("role", arg_type=role_type)

    with self.argument_context("iot central device compute-device-key") as context:
        context.argument(
            "primary_key",
            options_list=["--primary-key", "--pk"],
            help="The primary symmetric shared access key stored in base64 format. ",
        )

    with self.argument_context("iot central device") as context:
        context.argument(
            "instance_of",
            options_list=["--instance-of"],
            help="Central template id. Example: urn:ojpkindbz:modelDefinition:iild3tm_uo",
        )
        context.argument(
            "simulated",
            options_list=["--simulated"],
            arg_type=get_three_state_flag(),
            help="Add this flag if you would like IoT Central to set this up as a simulated device. "
            "--instance-of is required if this is true",
        )
        context.argument(
            "device_name",
            options_list=["--device-name"],
            help="Human readable device name. Example: Fridge",
        )
        context.argument(
            "interface_id",
            options_list=["--interface-id", "-i"],
            help="Interface name as specified in the device template. Example: c2dTestingTemplate_356",
        )
        context.argument(
            "command_name",
            options_list=["--command-name", "--cn"],
            help="Command name as specified in device template. Example: run_firmware_update",
        )
        context.argument(
            "content",
            options_list=["--content", "-k"],
            help="Configuration for request. "
            "Provide path to JSON file or raw stringified JSON. "
            "[File Path Example: ./path/to/file.json] "
            "[Stringified JSON Example: {'a': 'b'}] ",
        )

    with self.argument_context("iot central device simulate") as context:
        context.argument(
            "telemetry",
            options_list=["--telemetry", "-t"],
            help="The telemetry field names and type to use. Simulation will generate random values for them and will send out every 5 seconds."
            "Available types: ['number','text']"
            "Example: ['temperature=number,pressure=number,message=text]",
        )
        context.argument(
            "properties",
            options_list=["--properties", "-p"],
            help="The properties field names and type to use. Simulation will generate random values for them."
            "Available types: ['number','text']"
            "Example: ['manufacturer=text,fanSpeed=number]",
        )

    with self.argument_context("iot central user") as context:
        context.argument(
            "tenant_id",
            options_list=["--tenant-id", "--tnid"],
            help="Tenant ID for service principal to be added to the app. Object ID must also be specified. ",
        )
        context.argument(
            "object_id",
            options_list=["--object-id", "--oid"],
            help="Object ID for service principal to be added to the app. Tenant ID must also be specified. ",
        )
        context.argument(
            "email",
            options_list=["--email"],
            help="Email address of user to be added to the app. ",
        )
        context.argument(
            "assignee",
            options_list=["--user-id", "--assignee"],
            help="ID associated with the user. ",
        )
        context.argument("role", arg_type=role_type)

    with self.argument_context("iot central diagnostics") as context:
        context.argument("timeout", arg_type=event_timeout_type)
        context.argument("properties", arg_type=event_msg_prop_type)
        context.argument(
            "module_id", options_list=["--module-id", "-m"], help="Iot Edge Module ID",
        )
        context.argument("minimum_severity", arg_type=severity_type)
        context.argument("style", arg_type=style_type)
        context.argument(
            "duration",
            options_list=["--duration", "--dr"],
            type=int,
            help="Maximum duration to receive messages from target device before terminating connection."
            "Use 0 for infinity.",
        )
        context.argument(
            "max_messages",
            options_list=["--max-messages", "--mm"],
            type=int,
            help="Maximum number of messages to recieve from target device before terminating connection."
            "Use 0 for infinity.",
        )
        context.argument(
            "module_id", options_list=["--module-id", "-m"], help="Iot Edge Module ID",
        )
    # TODO: Delete this by end of Dec 2020
    load_deprecated_params(self, _)


def load_deprecated_params(self, _):
    with self.argument_context("iot central app monitor-events") as context:
        context.argument("timeout", arg_type=event_timeout_type)
        context.argument("properties", arg_type=event_msg_prop_type)
        context.argument(
            "module_id", options_list=["--module-id", "-m"], help="Iot Edge Module ID",
        )
        context.argument("minimum_severity", arg_type=severity_type)
