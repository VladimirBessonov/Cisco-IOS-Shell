#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tests for `CiscoiosshellDriver`
"""
import unittest
from mock import patch, MagicMock

from src.cisco_ios_resource_driver import CiscoIOSResourceDriver


@patch('src.cisco_ios_resource_driver.get_api')
@patch('src.cisco_ios_resource_driver.get_logger_with_thread_id')
class TestCiscoIOSShellDriver(unittest.TestCase):
    def setUp(self):
        self.driver = CiscoIOSResourceDriver()
        self.mocked_context = MagicMock()

    @patch('src.cisco_ios_resource_driver.create_networking_resource_from_context')
    @patch('src.cisco_ios_resource_driver.get_cli')
    def test_initialize(self, mocked_cli, mocked_get_attr, mocked_logger, mocked_api):
        # Setup

        mocked_get_attr.sessions_concurrency_limit.return_value = "1"
        # Act
        result = self.driver.initialize(self.mocked_context)
        # Assert
        self.assertTrue(result, 'Finished initializing')

    @patch('src.cisco_ios_resource_driver.create_networking_resource_from_context')
    @patch('src.cisco_ios_resource_driver.AutoloadRunner')
    def test_get_inventory(self, mocked_class, mocked_get_attr, mocked_logger, mocked_api):
        # Arrange
        mocked_class.return_value.discover.return_value = ''

        # Act
        self.driver.get_inventory(self.mocked_context)

        # Assert
        mocked_class.return_value.discover.assert_called()

    @patch('src.cisco_ios_resource_driver.create_networking_resource_from_context')
    @patch('src.cisco_ios_resource_driver.CommandRunner')
    def test_run_custom_command(self, mocked_class, mocked_get_attr, mocked_logger, mocked_api):
        # Arrange
        command = 'test command'
        response = 'response'
        mocked_class.return_value.run_custom_command.return_value = response

        # Act
        result = self.driver.run_custom_command(self.mocked_context, command)

        # Assert
        self.assertTrue(response, result)
        mocked_class.return_value.run_custom_command.assert_called_with(custom_command=[command])

    @patch('src.cisco_ios_resource_driver.create_networking_resource_from_context')
    @patch('src.cisco_ios_resource_driver.StateRunner')
    def test_health_check(self, mocked_class, mocked_get_attr, mocked_logger, mocked_api):
        # Arrange
        response = 'response'
        mocked_class.return_value.health_check.return_value = response

        # Act
        result = self.driver.health_check(self.mocked_context)

        # Assert
        self.assertTrue(response, result)
        mocked_class.return_value.health_check.assert_called_with()

    @patch('src.cisco_ios_resource_driver.create_networking_resource_from_context')
    @patch('src.cisco_ios_resource_driver.CommandRunner')
    def test_run_custom_config_command(self, mocked_class, mocked_get_attr, mocked_logger, mocked_api):
        # Arrange
        command = 'test command'
        response = 'response'
        mocked_class.return_value.run_custom_config_command.return_value = response

        # Act
        result = self.driver.run_custom_config_command(self.mocked_context, command)

        # Assert
        self.assertTrue(response, result)
        mocked_class.return_value.run_custom_config_command.assert_called_with(custom_command=[command])

    @patch('src.cisco_ios_resource_driver.create_networking_resource_from_context')
    @patch('src.cisco_ios_resource_driver.CommandRunner')
    def test_send_custom_command(self, mocked_class, mocked_get_attr, mocked_logger, mocked_api):
        # Arrange
        command = 'test command'
        response = 'response'
        mocked_class.return_value.run_custom_command.return_value = response

        # Act
        result = self.driver.send_custom_command(self.mocked_context, command)

        # Assert
        self.assertTrue(response, result)
        mocked_class.return_value.run_custom_command.assert_called_with(custom_command=[command])

    @patch('src.cisco_ios_resource_driver.create_networking_resource_from_context')
    @patch('src.cisco_ios_resource_driver.CommandRunner')
    def test_send_custom_config_command(self, mocked_class, mocked_get_attr, mocked_logger, mocked_api):
        # Arrange
        command = 'test command'
        response = 'response'
        mocked_class.return_value.run_custom_config_command.return_value = response

        # Act
        result = self.driver.send_custom_config_command(self.mocked_context, command)

        # Assert
        self.assertTrue(response, result)
        mocked_class.return_value.run_custom_config_command.assert_called_with(custom_command=[command])

    @patch('src.cisco_ios_resource_driver.create_networking_resource_from_context')
    @patch('src.cisco_ios_resource_driver.FirmwareRunner')
    def test_load_firmware(self, mocked_class, mocked_get_attr, mocked_logger, mocked_api):
        # Arrange
        path = 'test'
        vrf_management_name = 'response'
        mocked_class.return_value.load_firmware.return_value = ''

        # Act
        self.driver.load_firmware(self.mocked_context, path=path, vrf_management_name=vrf_management_name)

        # Assert
        mocked_class.return_value.load_firmware.assert_called_with(path=path, vrf_management_name=vrf_management_name)

    @patch('src.cisco_ios_resource_driver.FirmwareRunner')
    @patch('src.cisco_ios_resource_driver.create_networking_resource_from_context')
    def test_load_firmware_no_vrf(self, mocked_get_attr, mocked_class, mocked_logger, mocked_api):
        # Arrange
        path = 'test'
        vrf_management_name = None
        mocked_class.return_value.load_firmware.return_value = ''
        mocked_get_attr.return_value.vrf_management_name = vrf_management_name

        # Act
        self.driver.load_firmware(self.mocked_context, path=path, vrf_management_name=vrf_management_name)

        # Assert
        mocked_class.return_value.load_firmware.assert_called_with(path=path, vrf_management_name=vrf_management_name)

    @patch('src.cisco_ios_resource_driver.FirmwareRunner')
    @patch('src.cisco_ios_resource_driver.create_networking_resource_from_context')
    def test_update_firmware(self, mocked_get_attr, mocked_class, mocked_logger, mocked_api):
        # Arrange
        remote_host = 'test'
        file_path = 'response'
        vrf_management_name = None
        mocked_class.return_value.load_firmware.return_value = ''
        mocked_get_attr.return_value.vrf_management_name = vrf_management_name

        # Act
        self.driver.update_firmware(self.mocked_context, remote_host=remote_host, file_path=file_path)

        # Assert
        mocked_class.return_value.load_firmware.assert_called_with(path=remote_host,
                                                                   vrf_management_name=vrf_management_name)

    @patch('src.cisco_ios_resource_driver.ConfigurationRunner')
    @patch('src.cisco_ios_resource_driver.create_networking_resource_from_context')
    def test_save_no_params(self, mocked_get_attr, mocked_class, mocked_logger, mocked_api):
        # Arrange
        mocked_class.return_value.save.return_value = ''
        vrf_management_name = 'default'
        mocked_get_attr.return_value.vrf_management_name = vrf_management_name

        # Act
        self.driver.save(self.mocked_context, folder_path='', configuration_type='', vrf_management_name='')

        # Assert
        mocked_class.return_value.save.assert_called_with(folder_path='', configuration_type='running',
                                                          vrf_management_name=vrf_management_name)

    @patch('src.cisco_ios_resource_driver.create_networking_resource_from_context')
    @patch('src.cisco_ios_resource_driver.ConfigurationRunner')
    def test_save_all_params(self, mocked_class, mocked_get_attr, mocked_logger, mocked_api):
        # Arrange
        folder_path = 'ftp://ftpuser:ftppass@server/folder'
        configuration_type = 'running'
        vrf_management_name = 'vrf'

        mocked_class.return_value.save.return_value = ''

        # Act
        self.driver.save(self.mocked_context, folder_path=folder_path, configuration_type=configuration_type,
                         vrf_management_name=vrf_management_name)

        # Assert
        mocked_class.return_value.save.assert_called_with(folder_path=folder_path,
                                                          configuration_type=configuration_type,
                                                          vrf_management_name=vrf_management_name)

    @patch('src.cisco_ios_resource_driver.ConfigurationRunner')
    @patch('src.cisco_ios_resource_driver.create_networking_resource_from_context')
    def test_save_no_vrf(self, mocked_get_attr, mocked_class, mocked_logger, mocked_api):
        # Arrange
        folder_path = 'ftp://ftpuser:ftppass@server/folder'
        configuration_type = 'running'
        vrf = 'default'
        mocked_class.return_value.save.return_value = ''
        mocked_get_attr.return_value.vrf_management_name = vrf

        # Act
        self.driver.save(self.mocked_context, folder_path=folder_path, configuration_type=configuration_type,
                         vrf_management_name=None)

        # Assert
        mocked_class.return_value.save.assert_called_with(configuration_type=configuration_type,
                                                          folder_path=folder_path,
                                                          vrf_management_name=vrf)

    @patch('src.cisco_ios_resource_driver.ConfigurationRunner')
    @patch('src.cisco_ios_resource_driver.create_networking_resource_from_context')
    def test_save_no_vrf_no_folder_path(self, mocked_get_attr, mocked_class, mocked_logger, mocked_api):
        # Arrange
        configuration_type = 'startup'

        vrf = 'default'
        mocked_class.return_value.save.return_value = ''
        mocked_get_attr.return_value.vrf_management_name = vrf

        # Act
        self.driver.save(self.mocked_context, configuration_type=configuration_type,
                         folder_path='', vrf_management_name='')

        # Assert
        mocked_class.return_value.save.assert_called_with(configuration_type=configuration_type,
                                                          folder_path='',
                                                          vrf_management_name=vrf)

    @patch('src.cisco_ios_resource_driver.ConfigurationRunner')
    @patch('src.cisco_ios_resource_driver.create_networking_resource_from_context')
    def test_save_no_vrf_no_config_file(self, mocked_get_attr, mocked_class, mocked_logger, mocked_api):
        # Arrange
        folder_path = 'ftp://ftpuser:ftppass@server/folder'
        vrf = 'default'
        mocked_class.return_value.save.return_value = ''
        mocked_get_attr.return_value.vrf_management_name = vrf

        # Act
        self.driver.save(self.mocked_context, folder_path=folder_path, configuration_type='', vrf_management_name='')

        # Assert
        mocked_class.return_value.save.assert_called_with(configuration_type='running',
                                                          folder_path=folder_path,
                                                          vrf_management_name=vrf)

    @patch('src.cisco_ios_resource_driver.create_networking_resource_from_context')
    @patch('src.cisco_ios_resource_driver.ConfigurationRunner')
    def test_restore_all_params(self, mocked_class, mocked_get_attr, mocked_logger, mocked_api):
        # Arrange
        path = 'ftp://ftpuser:ftppass@server/folder'
        configuration_type = 'startup'
        restore_method = 'append'
        vrf_management_name = 'vrf'
        mocked_class.return_value.restore.return_value = ''

        # Act
        self.driver.restore(self.mocked_context, path=path, configuration_type=configuration_type,
                            restore_method=restore_method, vrf_management_name=vrf_management_name)

        # Assert
        mocked_class.return_value.restore.assert_called_with(path=path, configuration_type=configuration_type,
                                                             restore_method=restore_method,
                                                             vrf_management_name=vrf_management_name)

    @patch('src.cisco_ios_resource_driver.ConfigurationRunner')
    @patch('src.cisco_ios_resource_driver.create_networking_resource_from_context')
    def test_restore_no_vrf(self, mocked_get_attr, mocked_class, mocked_logger, mocked_api):
        # Arrange
        path = 'ftp://ftpuser:ftppass@server/folder'
        configuration_type = 'startup'
        restore_method = 'append'
        vrf = 'management'
        mocked_class.return_value.restore.return_value = ''
        mocked_get_attr.return_value.vrf_management_name = vrf

        # Act
        self.driver.restore(self.mocked_context, path=path, configuration_type=configuration_type,
                            restore_method=restore_method, vrf_management_name='')

        # Assert
        mocked_class.return_value.restore.assert_called_with(path=path, configuration_type=configuration_type,
                                                             restore_method=restore_method, vrf_management_name=vrf)

    @patch('src.cisco_ios_resource_driver.ConfigurationRunner')
    @patch('src.cisco_ios_resource_driver.create_networking_resource_from_context')
    def test_restore_no_vrf_no_restore_method(self, mocked_get_attr, mocked_class, mocked_logger, mocked_api):
        # Arrange
        path = 'ftp://ftpuser:ftppass@server/folder'
        configuration_type = 'startup'
        vrf = 'management'
        mocked_class.return_value.restore.return_value = ''
        mocked_get_attr.return_value.vrf_management_name = vrf

        # Act
        self.driver.restore(self.mocked_context, path=path, configuration_type=configuration_type, restore_method='',
                            vrf_management_name='')

        # Assert
        mocked_class.return_value.restore.assert_called_with(path=path, configuration_type=configuration_type,
                                                             restore_method='override', vrf_management_name=vrf)

    @patch('src.cisco_ios_resource_driver.ConfigurationRunner')
    @patch('src.cisco_ios_resource_driver.create_networking_resource_from_context')
    def test_restore_no_optional_params(self, mocked_get_attr, mocked_class, mocked_logger, mocked_api):
        # Arrange
        path = 'ftp://ftpuser:ftppass@server/folder'
        mocked_class.return_value.restore.return_value = ''
        mocked_get_attr.return_value.vrf_management_name = None

        # Act
        self.driver.restore(self.mocked_context, path=path,
                            configuration_type=None,
                            restore_method=None,
                            vrf_management_name=None)

        # Assert
        mocked_class.return_value.restore.assert_called_with(path=path, configuration_type='running',
                                                             restore_method='override', vrf_management_name=None)

    @patch('src.cisco_ios_resource_driver.create_networking_resource_from_context')
    @patch('src.cisco_ios_resource_driver.ConfigurationRunner')
    def test_orchestration_save_no_optional_params(self, mocked_class, mocked_get_attr, mocked_logger, mocked_api):
        # Arrange
        mocked_class.return_value.orchestration_save.return_value = ''

        # Act
        self.driver.orchestration_save(self.mocked_context, None, None)

        # Assert
        mocked_class.return_value.orchestration_save.assert_called_with(mode='shallow', custom_params=None)

    @patch('src.cisco_ios_resource_driver.create_networking_resource_from_context')
    @patch('src.cisco_ios_resource_driver.ConfigurationRunner')
    def test_orchestration_save(self, mocked_class, mocked_get_attr, mocked_logger, mocked_api):
        # Arrange
        mode = 'shallow'
        custom_params = 'test json'
        mocked_class.return_value.orchestration_save.return_value = ''

        # Act
        self.driver.orchestration_save(self.mocked_context, mode=mode, custom_params=custom_params)

        # Assert
        mocked_class.return_value.orchestration_save.assert_called_with(mode=mode, custom_params=custom_params)

    @patch('src.cisco_ios_resource_driver.create_networking_resource_from_context')
    @patch('src.cisco_ios_resource_driver.ConfigurationRunner')
    def test_orchestration_save_no_custom_params(self, mocked_class, mocked_get_attr, mocked_logger, mocked_api):
        # Arrange
        mocked_class.return_value.orchestration_save.return_value = ''

        # Act
        self.driver.orchestration_save(self.mocked_context, mode='shallow', custom_params=None)

        # Assert
        mocked_class.return_value.orchestration_save.assert_called_with(mode='shallow', custom_params=None)

    @patch('src.cisco_ios_resource_driver.create_networking_resource_from_context')
    @patch('src.cisco_ios_resource_driver.ConfigurationRunner')
    def test_orchestration_restore_no_custom_params(self, mocked_class, mocked_get_attr, mocked_logger, mocked_api):
        # Arrange
        saved_artifact_info = 'test json'
        custom_params = None
        mocked_class.return_value.orchestration_restore.return_value = ''

        # Act
        self.driver.orchestration_restore(self.mocked_context, saved_artifact_info, custom_params)

        # Assert
        mocked_class.return_value.orchestration_restore.assert_called_with(saved_artifact_info=saved_artifact_info,
                                                                           custom_params=None)

    @patch('src.cisco_ios_resource_driver.create_networking_resource_from_context')
    @patch('src.cisco_ios_resource_driver.ConfigurationRunner')
    def test_orchestration_restore_all_params(self, mocked_class, mocked_get_attr, mocked_logger, mocked_api):
        # Arrange
        saved_artifact_info = 'test json'
        custom_params = 'test json'
        mocked_class.return_value.orchestration_restore.return_value = ''

        # Act
        self.driver.orchestration_restore(self.mocked_context, saved_artifact_info, custom_params)

        # Assert
        mocked_class.return_value.orchestration_restore.assert_called_with(saved_artifact_info=saved_artifact_info,
                                                                           custom_params=custom_params)

    @patch('src.cisco_ios_resource_driver.create_networking_resource_from_context')
    @patch('src.cisco_ios_resource_driver.ConnectivityRunner')
    def test_apply_connectivity_changes(self, mocked_class, mocked_get_attr, mocked_logger, mocked_api):
        # Arrange
        request = 'test json'
        mocked_class.return_value.apply_connectivity_changes.return_value = ''

        # Act
        self.driver.ApplyConnectivityChanges(self.mocked_context, request=request)

        # Assert
        mocked_class.return_value.apply_connectivity_changes.assert_called_with(request=request)


if __name__ == '__main__':
    import sys
    sys.exit(unittest.main())
