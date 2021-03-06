# coding: utf-8

"""
    WALKOFF

    An active cyber defense development framework enabling orchestration capabilities to be written once and deployed across WALKOFF-enabled orchestration tools. https://nsacyber.github.io/WALKOFF/  # noqa: E501

    The version of the OpenAPI document: 0.9.1
    Contact: walkoff@nsa.gov
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import walkoff_client
from walkoff_client.api.scheduler_api import SchedulerApi  # noqa: E501
from walkoff_client.rest import ApiException


class TestSchedulerApi(unittest.TestCase):
    """SchedulerApi unit test stubs"""

    def setUp(self):
        self.api = walkoff_client.api.scheduler_api.SchedulerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_scheduled_task(self):
        """Test case for create_scheduled_task

        Create a new Scheduled Task  # noqa: E501
        """
        pass

    def test_delete_scheduled_task(self):
        """Test case for delete_scheduled_task

        Delete the scheduled task  # noqa: E501
        """
        pass

    def test_get_scheduler_status(self):
        """Test case for get_scheduler_status

        Get the current scheduler status.  # noqa: E501
        """
        pass

    def test_read_all_scheduled_tasks(self):
        """Test case for read_all_scheduled_tasks

        Get all the scheduled tasks  # noqa: E501
        """
        pass

    def test_read_scheduled_task(self):
        """Test case for read_scheduled_task

        Get the scheduled task  # noqa: E501
        """
        pass

    def test_update_scheduled_task(self):
        """Test case for update_scheduled_task

        Update a new Scheduled Task  # noqa: E501
        """
        pass

    def test_update_scheduler_status(self):
        """Test case for update_scheduler_status

        Update the status of the scheduler  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
