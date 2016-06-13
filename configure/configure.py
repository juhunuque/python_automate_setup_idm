#!/usr/bin/env python
import os
import sys
from utils import resolve_config_parameters

if sys.version_info[0] == 2:
    import ConfigParser
else:
    import configparser as ConfigParser

config_file = os.path.join(os.path.dirname(__file__), 'settings.cfg')
config_parser = ConfigParser.ConfigParser()
config_parser.read(config_file)

# GIT SETTINGS
git_user = resolve_config_parameters(config_parser, 'GIT SETTINGS', 'GIT_USER')
git_password = resolve_config_parameters(config_parser, 'GIT SETTINGS', 'GIT_PASSWORD')
git_idm_python_url = resolve_config_parameters(config_parser, 'GIT SETTINGS', 'GIT_IDM_PYTHON_URL')
git_target_url = resolve_config_parameters(config_parser, 'GIT SETTINGS', 'GIT_TARGET_URL')
git_middle_url = resolve_config_parameters(config_parser, 'GIT SETTINGS', 'GIT_MIDDLE_URL')
git_functional_url = resolve_config_parameters(config_parser, 'GIT SETTINGS', 'GIT_FUNCTIONAL_URL')

# LOCAL SETTINGS
project_folder = resolve_config_parameters(config_parser, 'LOCAL SETTINGS', 'PROJECT_FOLDER')
python_exec_cmd = resolve_config_parameters(config_parser, 'LOCAL SETTINGS', 'PYTHON_CMD')

# P2020 SETTINGS
p2020_token_server = resolve_config_parameters(config_parser, 'P2020 SETTINGS', 'P2020_TOKEN_SERVER')
p2020_resource_id = resolve_config_parameters(config_parser, 'P2020 SETTINGS', 'P2020_RESOURCE_ID')
p2020_client_id = resolve_config_parameters(config_parser, 'P2020 SETTINGS', 'P2020_CLIENT_ID')
p2020_client_secret = resolve_config_parameters(config_parser, 'P2020 SETTINGS', 'P2020_CLIENT_SECRET')
p2020_token_key = resolve_config_parameters(config_parser, 'P2020 SETTINGS', 'P2020_TOKEN_KEY')
p2020_name_logger = resolve_config_parameters(config_parser, 'P2020 SETTINGS', 'P2020_NAME_LOGGER', 1)
p2020_dtformat = resolve_config_parameters(config_parser, 'P2020 SETTINGS', 'P2020_DTFORMAT', 1)
p2020_formatter = resolve_config_parameters(config_parser, 'P2020 SETTINGS', 'P2020_FORMATTER', 1)
p2020_log_file = resolve_config_parameters(config_parser, 'P2020 SETTINGS', 'P2020_LOG_FILE')

# TARGET SETTINGS
target_config_port = resolve_config_parameters(config_parser, 'TARGET SETTINGS', 'TARGET_CONFIG_PORT')
target_config_host = resolve_config_parameters(config_parser, 'TARGET SETTINGS', 'TARGET_CONFIG_HOST')
target_service_name = resolve_config_parameters(config_parser, 'TARGET SETTINGS', 'TARGET_SERVICE_NAME')
target_service_discovery_name = resolve_config_parameters(config_parser, 'TARGET SETTINGS', 'TARGET_SERVICE_DISCOVERY_NAME')

# MIDDLE SETTINGS
middle_config_port = resolve_config_parameters(config_parser, 'MIDDLE SETTINGS', 'MIDDLE_CONFIG_PORT')
middle_config_host = resolve_config_parameters(config_parser, 'MIDDLE SETTINGS', 'MIDDLE_CONFIG_HOST')
middle_target_port = resolve_config_parameters(config_parser, 'MIDDLE SETTINGS', 'MIDDLE_TARGET_PORT')
middle_target_host = resolve_config_parameters(config_parser, 'MIDDLE SETTINGS', 'MIDDLE_TARGET_HOST')
middle_service_name = resolve_config_parameters(config_parser, 'MIDDLE SETTINGS', 'MIDDLE_SERVICE_NAME')
middle_service_discovery_name = resolve_config_parameters(config_parser, 'MIDDLE SETTINGS', 'MIDDLE_SERVICE_DISCOVERY_NAME')

# FUNCTIONAL SETTINGS
functional_config_port = resolve_config_parameters(config_parser, 'FUNCTIONAL SETTINGS', 'FUNCTIONAL_CONFIG_PORT')
functional_config_host = resolve_config_parameters(config_parser, 'FUNCTIONAL SETTINGS', 'FUNCTIONAL_CONFIG_HOST')
functional_service_name = resolve_config_parameters(config_parser, 'FUNCTIONAL SETTINGS', 'FUNCTIONAL_SERVICE_NAME')
functional_service_discovery_name = resolve_config_parameters(config_parser, 'FUNCTIONAL SETTINGS', 'FUNCTIONAL_SERVICE_DISCOVERY_NAME')
functional_token_server = resolve_config_parameters(config_parser, 'FUNCTIONAL SETTINGS', 'FUNCTIONAL_TOKEN_SERVER')
functional_resource_id = resolve_config_parameters(config_parser, 'FUNCTIONAL SETTINGS', 'FUNCTIONAL_RESOURCE_ID')
functional_client_id = resolve_config_parameters(config_parser, 'FUNCTIONAL SETTINGS', 'FUNCTIONAL_CLIENT_ID')
functional_client_secret = resolve_config_parameters(config_parser, 'FUNCTIONAL SETTINGS', 'FUNCTIONAL_CLIENT_SECRET')
functional_user_id = resolve_config_parameters(config_parser, 'FUNCTIONAL SETTINGS', 'FUNCTIONAL_USER_ID')
functional_user_secret = resolve_config_parameters(config_parser, 'FUNCTIONAL SETTINGS', 'FUNCTIONAL_USER_SECRET')
functional_user1 = resolve_config_parameters(config_parser, 'FUNCTIONAL SETTINGS', 'FUNCTIONAL_USER1')
functional_user1_password = resolve_config_parameters(config_parser, 'FUNCTIONAL SETTINGS', 'FUNCTIONAL_USER1_PASSWORD')
functional_user2 = resolve_config_parameters(config_parser, 'FUNCTIONAL SETTINGS', 'FUNCTIONAL_USER2')
functional_user2_password = resolve_config_parameters(config_parser, 'FUNCTIONAL SETTINGS', 'FUNCTIONAL_USER2_PASSWORD')
functional_user3 = resolve_config_parameters(config_parser, 'FUNCTIONAL SETTINGS', 'FUNCTIONAL_USER3')
functional_user3_password = resolve_config_parameters(config_parser, 'FUNCTIONAL SETTINGS', 'FUNCTIONAL_USER3_PASSWORD')
functional_target_server = resolve_config_parameters(config_parser, 'FUNCTIONAL SETTINGS', 'FUNCTIONAL_TARGET_SERVER')
functional_middle_server = resolve_config_parameters(config_parser, 'FUNCTIONAL SETTINGS', 'FUNCTIONAL_MIDDLE_SERVER')
functional_token_expired = resolve_config_parameters(config_parser, 'FUNCTIONAL SETTINGS', 'FUNCTIONAL_TOKEN_EXPIRED')
functional_token_invalid = resolve_config_parameters(config_parser, 'FUNCTIONAL SETTINGS', 'FUNCTIONAL_TOKEN_INVALID')







