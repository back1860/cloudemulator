# -*- coding:utf-8 -*-

import time
import uuid
import threading


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


_lock = threading.Lock()


def singleton(cls, *args, **kw):
    instances = {}
    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return _singleton


class Task(object):
    def __init__(self, id, operation):
        self.id = id
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


@singleton
class TaskManager(object):
    def __init__(self):
        self.run_queue = {}

    def add_task(self, operation):
        _lock.acquire()
        try:
            task_id = str(uuid.uuid1())
            self.run_queue[task_id] = Task(task_id, operation)
        except Exception as e:
            pass
        finally:
            _lock.release()
        return task_id

    def get_task(self, task_id):
        _lock.acquire()
        try:
            task = self.run_queue[task_id]
            task.update_task_status()
        except Exception as e:
            pass
        finally:
            _lock.release()

        return task

    def get_task_status(self, task_id):
        task_status = "running"
        _lock.acquire()
        try:
            task = self.run_queue[task_id]
            task_status = task.update_task_status()
        except Exception as e:
            pass
        finally:
            _lock.release()
        return task_status


if __name__ == '__main__':
    tm = TaskManager()
    tm2 = TaskManager()
    task_id = tm.add_task(OperationName.CREATE_VAPP)
    print "create task_id = %s" % task_id
    task_status = tm2.get_task_status(task_id)
    print task_status

    time.sleep(30)

    task_status = tm.get_task_status(task_id)
    print task_status
