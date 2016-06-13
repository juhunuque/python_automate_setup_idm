#!/usr/bin/env python

from configure.configure import *


def set_variables():
    print 'CONFIGURING ENVIRONMENT VARIABLES: PROCESS START'

    # P2020 SETTINGS
    os.environ['P2020_IDENTITY_TOKEN_SERVER'] = p2020_token_server
    os.environ['P2020_IDENTITY_RESOURCE_ID'] = p2020_resource_id
    os.environ['P2020_IDENTITY_CLIENT_ID'] = p2020_client_id
    os.environ['P2020_IDENTITY_CLIENT_SECRET'] = p2020_client_secret
    os.environ['P2020_IDENTITY_NAME_LOGGER'] = p2020_name_logger
    os.environ['P2020_IDENTITY_DTFORMAT'] = p2020_dtformat
    os.environ['P2020_IDENTITY_FORMATTER'] = p2020_formatter
    os.environ['P2020_IDENTITY_LOG_FILE'] = p2020_log_file
    if p2020_token_key is not None:
        os.environ['P2020_IDENTITY_TOKEN_KEY'] = p2020_token_key

    # TARGET SETTINGS
    os.environ['P2020_IDENTITY_CONFIG_TARGET_CONFIG_PORT'] = target_config_port
    os.environ['P2020_IDENTITY_CONFIG_TARGET_CONFIG_HOST'] = target_config_host
    os.environ['P2020_IDENTITY_CONFIG_TARGET_SERVICE_NAME'] = target_service_name
    os.environ['P2020_IDENTITY_CONFIG_TARGET_SERVICE_DISCOVERY_NAME'] = target_service_discovery_name

    # MIDDLE SETTINGS
    os.environ['P2020_IDENTITY_CONFIG_MIDDLE_CONFIG_PORT'] = middle_config_port
    os.environ['P2020_IDENTITY_CONFIG_MIDDLE_CONFIG_HOST'] = middle_config_host
    os.environ['P2020_IDENTITY_CONFIG_MIDDLE_TARGET_PORT'] = middle_target_port
    os.environ['P2020_IDENTITY_CONFIG_MIDDLE_TARGET_HOST'] = middle_config_host
    os.environ['P2020_IDENTITY_CONFIG_MIDDLE_SERVICE_NAME'] = middle_service_name
    os.environ['P2020_IDENTITY_CONFIG_MIDDLE_SERVICE_DISCOVERY_NAME'] = middle_service_discovery_name

    # FUNCTIONAL SETTINGS
    os.environ['P2020_IDENTITY_CONFIG_FUNCTIONAL_CONFIG_PORT'] = functional_config_port
    os.environ['P2020_IDENTITY_CONFIG_FUNCTIONAL_CONFIG_HOST'] = functional_config_host
    os.environ['P2020_IDENTITY_CONFIG_FUNCTIONAL_SERVICE_NAME'] = functional_service_name
    os.environ['P2020_IDENTITY_CONFIG_FUNCTIONAL_SERVICE_DISCOVERY_NAME'] = functional_service_discovery_name
    os.environ['P2020_IDENTITY_USER_ID'] = functional_user_id
    os.environ['P2020_IDENTITY_USER_SECRET'] = functional_user_secret
    os.environ['P2020_IDENTITY_USER1'] = functional_user1
    os.environ['P2020_IDENTITY_PASSWORD1'] = functional_user1_password
    os.environ['P2020_IDENTITY_USER2'] = functional_user2
    os.environ['P2020_IDENTITY_PASSWORD2'] = functional_user2_password
    os.environ['P2020_IDENTITY_USER3'] = functional_user3
    os.environ['P2020_IDENTITY_PASSWORD3'] = functional_user3_password
    os.environ['P2020_IDENTITY_TARGET_SERVICE'] = functional_target_server
    os.environ['P2020_IDENTITY_TOKEN_EXPIRED'] = functional_token_expired
    os.environ['P2020_IDENTITY_TOKEN_INVALID'] = functional_token_invalid

    print 'CONFIGURING ENVIRONMENT VARIABLES: PROCESS DONE'

if __name__ == '__main__':
    set_variables()


