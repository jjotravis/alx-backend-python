#!/usr/bin/env python3
"""
Tests for client
"""

from client import GithubOrgClient
import unittest
from unittest import mock
from unittest.mock import Mock, patch, PropertyMock
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """
    Class for testing function in client
    """

    @parameterized.expand([
        ("google"),
        ("abc")
        ])
    @patch("client.get_json", return_value={"payload": True})
    def test_org(self, org, mock_org):
        """
        Test GithubOrgClient.org method
        """
        org_test = GithubOrgClient(org)
        test_resp = org_test.org
        self.assertEqual(test_resp, mock_org.return_value)
        mock_org.assert_called_once()

    def test_public_repos_url(self):
        """
        Tests if _public_repos_url works
        """
        with patch.object(GithubOrgClient, "org",
                          new_callable=PropertyMock) as mock:
            mock.return_value = {"repos_url": 89}
            test_org = GithubOrgClient("holberton")
            test_url = test_org._public_repos_url
            self.assertEqual(test_url, mock.return_value.get("repos_url"))
            mock.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, licence_key, expected):
        """
        Test has_license method
        """
        test_obj = GithubOrgClient('holberton')
        license_avail = test_obj.has_license(repo, licence_key)
        self.assertEqual(license_avail, expected)
