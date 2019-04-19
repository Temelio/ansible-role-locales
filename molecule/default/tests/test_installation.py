"""
Role tests
"""

import os
from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    """
    Ensure /etc/default/locale file exists
    """

    f = host.file('/etc/default/locale')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
