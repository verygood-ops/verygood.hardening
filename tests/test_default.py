from testinfra.utils.ansible_runner import AnsibleRunner
testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_ssh_port(Socket):
    socket = Socket('tcp://22')
    assert socket.is_listening
