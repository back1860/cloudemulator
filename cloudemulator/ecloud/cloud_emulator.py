# -*- coding:utf-8 -*-

import time
import uuid
import threading
import copy


DEFAULT_COST = 0
CREATE_VAPP_COST = 0
DELETE_VAPP_COST = 0


class OperationName(object):
    CREATE_VAPP = "create_vapp"
    DELETE_VAPP = "delete_vapp"
    VAPP_UPDATE_VM = "vapp_update_vm"
    CREATE_VOLUME = "create_volume"
    DELETE_VOLUME = "delete_volume"
    ATTACH_VOLUME = "attach_volume"
    DETACH_VOLUME = "detach_volume"


class VirtualMachineStatus(object):
    CREATING = "CREATING",
    UNRESOLVED = "UNRESOLVED",
    RESOLVED = "RESOLVED",
    SUSPENDED = "SUSPENDED",
    POWERED_ON = "POWERED_ON",
    POWERED_OFF = "POWERED_OFF",
    NO_STATE = "NOSTATE"

_task_queue_lock = threading.Lock()
_vm_room_lock = threading.Lock()


def singleton(cls, *args, **kw):
    instances = {}
    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return _singleton


class Task(object):
    def __init__(self, operation):
        self.id = str(uuid.uuid1())
        self.operation = operation
        self.startTime = time.time()
        self.endTime = None
        self.status = 'running'
        self.progress = 1

    def update_task_status(self):
        run_time = time.time() - self.startTime
        cost_time = DEFAULT_COST
        if self.status == OperationName.CREATE_VAPP:
            cost_time = CREATE_VAPP_COST
        elif self.status == OperationName.DELETE_VAPP:
            cost_time = DELETE_VAPP_COST

        if run_time >= cost_time:
            self.status = "success"
            self.progress = 100
        else:
            self.progress = run_time * 100 / cost_time

        return self.status


class VirtualMachine(object):
    def __init__(self, vm_name):
        self.id = str(uuid.uuid1())
        self.name = vm_name
        self.status = VirtualMachineStatus.POWERED_ON

    def power_on(self):
        self.status = VirtualMachineStatus.POWERED_ON

    def power_off(self):
        self.status = VirtualMachineStatus.POWERED_OFF


@singleton
class CloudManager(object):
    def __init__(self):
        self.vm_room = {}
        self.run_queue = {}
        self.vm_room_snapshot = None

    def create_virtual_machine(self, vm_name):
        task = Task(OperationName.CREATE_VAPP)
        vm = VirtualMachine(vm_name)
        self._add_task(task)
        self._add_vm(vm)
        return task.id, vm.id

    def delete_virtual_machine(self, vm_name):
        task = Task(OperationName.DELETE_VAPP)
        self._add_task(task)
        vm_id = self._delete_vm(vm_name)
        return task.id, vm_id

    def update_virtual_machine(self, vm_id):
        task = Task(OperationName.VAPP_UPDATE_VM)
        self._add_task(task)
        return task.id, vm_id

    def power_on_virtual_machine(self, vm_name):
        vm_id = self._get_vm_id_by_name(vm_name)
        task = Task(OperationName.VAPP_UPDATE_VM)
        return task.id, vm_id

    def power_off_virtual_machine(self, vm_name):
        vm_id = self._get_vm_id_by_name(vm_name)
        task = Task(OperationName.VAPP_UPDATE_VM)
        return task.id, vm_id

    def query_virtual_machine(self, vm_id):
        if vm_id in self.vm_room:
            return copy.deepcopy(self.vm_room.get(id))
        else:
            return None

    def paged_query_virtual_machines(self, page=1, pageSize=100):
        if page == 1:
            self._snapshot_vm_room()

        total = len(self.vm_room) / pageSize + 1

        start_index = (page-1)*pageSize
        if start_index >= len(self.vm_room_snapshot):
            return total, -1, None

        next_page = page + 1
        end_index = page*pageSize
        if end_index > len(self.vm_room_snapshot):
            end_index = len(self.vm_room_snapshot)
            next_page = -1

        return total, next_page, self.vm_room_snapshot[start_index: end_index]

    def query_virtual_machines(self):
        return copy.deepcopy(self.vm_room.values())

    def query_task(self, task_id):
        _task_queue_lock.acquire()
        try:
            task = self.run_queue[task_id]
            task.update_task_status()
        except Exception as e:
            pass
        finally:
            _task_queue_lock.release()
        return task

    def get_task_status(self, task_id):
        task_status = "running"
        _task_queue_lock.acquire()
        try:
            task = self.run_queue[task_id]
            task_status = task.update_task_status()
        except Exception as e:
            pass
        finally:
            _task_queue_lock.release()
        return task_status

    def _snapshot_vm_room(self):
        _vm_room_lock.acquire()
        try:
            self.vm_room_snapshot = []
            for vm_id in self.vm_room:
                self.vm_room_snapshot.append(copy.deepcopy(self.vm_room.get(vm_id)))
        except Exception as e:
            pass
        finally:
            _vm_room_lock.release()

    def _add_vm(self, vm):
        _vm_room_lock.acquire()
        try:
            self.vm_room[vm.id] = vm
        except Exception as e:
            pass
        finally:
            _vm_room_lock.release()

    def _get_vm_id_by_name(self, vm_name):
        for id in self.vm_room.keys():
            vm = self.vm_room.get(id)
            if vm.name == vm_name:
                return id

        return None

    def _delete_vm(self, vm_name):
        vm_id = self._get_vm_id_by_name(vm_name)
        if not vm_id:
            return
        _vm_room_lock.acquire()
        try:
            self.vm_room.pop(vm_id)
        except Exception as e:
            pass
        finally:
            _vm_room_lock.release()
        return vm_id

    def _add_task(self, task):
        _task_queue_lock.acquire()
        try:
            self.run_queue[task.id] = task
        except Exception as e:
            pass
        finally:
            _task_queue_lock.release()


if __name__ == '__main__':
    tm = CloudManager()

    for i in range(100):
        task_id, vm_id = tm.create_virtual_machine("server@dsdsadas" + str(i))

    next_page, records = tm.paged_query_virtual_machines(page=1, pageSize=30)
    print "page 1"
    print records

    while next_page > 0:
        print "page %s" % next_page
        next_page, records = tm.paged_query_virtual_machines(page=next_page, pageSize=30)
        print records

    vm_list = tm.query_virtual_machines()
    vm_body = ""
    for vm in vm_list:
        vm_body = vm_body + '<ResourceEntity type="application/vnd.vmware.vcloud.vApp+xml" name="%s" href="http://162.3.201.10/api/vApp/vapp-%s"/>' % (vm.name, vm.id)
    print vm_body

