import shutil
import psutil
class PCHealth:
    def __init__(self):
        self.free_disk_space=None
        self.per_cpu_usage=None
        self.calculate_free_disk_space()
        self.calculate_per_cpu_usage()

    def calculate_free_disk_space(self):
        du=shutil.disk_usage("/")
        self.free_disk_space=du.free/du.total*100


    def calculate_per_cpu_usage(self):
        self.per_cpu_usage=psutil.cpu_percent(1)


    def is_free_disk_space_ok(self):
       if self.free_disk_space>=20:
            return True
       else:
            return False



    def is_per_cpu_usage_ok(self):
        if self.per_cpu_usage<=75:
            return True
        else:
            return False



    def get_free_disk_space(self):
        return self.free_disk_space

    def get_per_cpu_usage(self):
        return self.per_cpu_usage
