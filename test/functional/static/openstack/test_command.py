#  Copyright (c) 2015-2017 Cisco Systems, Inc.
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to
#  deal in the Software without restriction, including without limitation the
#  rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
#  sell copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#  DEALINGS IN THE SOFTWARE.

import pytest


@pytest.fixture()
def scenario_name():
    return 'openstack'


@pytest.mark.parametrize(
    'with_scenario', ['driver/static'], indirect=['with_scenario'])
def test_command_check(with_scenario, scenario_name):
    pytest.helpers.check(scenario_name)


@pytest.mark.parametrize(
    'with_scenario', ['driver/static'], indirect=['with_scenario'])
def test_command_converge(with_scenario, scenario_name):
    pytest.helpers.converge(scenario_name)


@pytest.mark.parametrize(
    'with_scenario', ['driver/static'], indirect=['with_scenario'])
def test_command_create(with_scenario, scenario_name):
    pytest.helpers.create(scenario_name)


@pytest.mark.parametrize(
    'with_scenario', ['dependency'], indirect=['with_scenario'])
def test_command_dependency_ansible_galaxy(with_scenario, scenario_name):
    pass


@pytest.mark.parametrize(
    'with_scenario', ['dependency'], indirect=['with_scenario'])
def test_command_dependency_gilt(with_scenario, scenario_name):
    pass


@pytest.mark.parametrize(
    'with_scenario', ['driver/static'], indirect=['with_scenario'])
def test_command_destroy(with_scenario, scenario_name):
    pytest.helpers.destroy(scenario_name)


@pytest.mark.parametrize(
    'with_scenario', ['driver/static'], indirect=['with_scenario'])
def test_command_idempotence(with_scenario, scenario_name):
    pytest.helpers.idempotence(scenario_name)


def test_command_init_role(temp_dir, scenario_name):
    pass


def test_command_init_scenario(temp_dir, scenario_name):
    pass


@pytest.mark.parametrize(
    'with_scenario', ['driver/static'], indirect=['with_scenario'])
def test_command_list(with_scenario, scenario_name):
    x = """
Instance Name              Driver Name    Provisioner Name    Scenario Name    Created    Converged
-------------------------  -------------  ------------------  ---------------  ---------  -----------
static-instance-docker     Static         Ansible             docker           False      True
static-instance-openstack  Static         Ansible             openstack        False      True
static-instance-vagrant    Static         Ansible             vagrant          False      True
""".strip()  # noqa

    pytest.helpers.list(x)


@pytest.mark.parametrize(
    'with_scenario', ['driver/static'], indirect=['with_scenario'])
def test_command_list_with_format_plain(with_scenario, scenario_name):
    x = """
static-instance-docker     Static  Ansible  docker     False  True
static-instance-openstack  Static  Ansible  openstack  False  True
static-instance-vagrant    Static  Ansible  vagrant    False  True
""".strip()

    pytest.helpers.list_with_format_plain(x)


@pytest.mark.parametrize(
    'with_scenario', ['driver/static'], indirect=['with_scenario'])
def test_command_login(with_scenario, scenario_name):
    pytest.helpers.login('static-instance-openstack',
                         '.*static-instance-openstack.*', scenario_name)


@pytest.mark.parametrize(
    'with_scenario', ['driver/static'], indirect=['with_scenario'])
def test_command_syntax(with_scenario, scenario_name):
    pytest.helpers.syntax(scenario_name)


@pytest.mark.parametrize(
    'with_scenario', ['driver/static'], indirect=['with_scenario'])
def test_command_test(with_scenario, scenario_name):
    pytest.helpers.test(scenario_name)


@pytest.mark.parametrize(
    'with_scenario', ['driver/static'], indirect=['with_scenario'])
def test_command_verify(with_scenario, scenario_name):
    pytest.helpers.verify(scenario_name)
