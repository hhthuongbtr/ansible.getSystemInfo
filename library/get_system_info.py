#!/usr/bin/python
from ansible.module_utils.basic import *

class SystemInfo:
    def __init__(self):
        self.mem_path = "/proc/meminfo"
        self.cpu_path = "/proc/cpuinfo"
        self.hostname_path = "/etc/hostname"

    def get_mem(self):
        mem_list = file(self.mem_path).read()
        result = []
        for line in mem_list.split('\n'):
            if len(line) < 1:
                continue
            (name, value) = line.split(":")
            name = name.strip()
            value = value.strip()
            data = {name: value}
            result.append(data)
        return result

    def get_cpu(self):
        cpu_list = file(self.cpu_path).read()
        result = []
        for line in cpu_list.split('\n'):
            if len(line) < 1:
                continue
            (name, value) = line.split(":")
            name = name.strip()
            value = value.strip()
            data = {name: value}
            result.append(data)
        return result

    def get_hostname(self):
        hostname_list = file(self.hostname_path).read()
        if len(hostname_list) < 1:
            return "unknow"
        for line in hostname_list.split('\n'):
            hostname = line.strip()
            break
        return hostname

    def get_info(self):
        return {"mem": self.get_mem(), "cpu": self.get_cpu(), "hostname": self.get_hostname()}

def main():
    module = AnsibleModule(argument_spec={})
    si = SystemInfo()
    response = si.get_info()
    module.exit_json(changed=False, meta=response)


if __name__ == '__main__':
    main()
