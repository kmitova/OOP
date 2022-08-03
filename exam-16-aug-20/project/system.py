from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:

    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        new_power_hardware = PowerHardware(name, capacity, memory)
        System._hardware.append(new_power_hardware)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        new_heavy_hardware = HeavyHardware(name, capacity, memory)
        System._hardware.append(new_heavy_hardware)

    @staticmethod
    def __find_hardware_by_name(name):
        for h in System._hardware:
            if h.name == name:
                return h
        # return None

    @staticmethod
    def __find_software_by_name(name):
        for s in System._software:
            if s.name == name:
                return s
        # return None

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware = System.__find_hardware_by_name(hardware_name)
        if not hardware:
            return "Hardware does not exist"
        new_express_software = ExpressSoftware(name, capacity_consumption, memory_consumption)
        hardware.install(new_express_software)
        System._software.append(new_express_software)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware = System.__find_hardware_by_name(hardware_name)
        if not hardware:
            return "Hardware does not exist"
        new_light_software = LightSoftware(name, capacity_consumption, memory_consumption)
        hardware.install(new_light_software)
        System._software.append(new_light_software)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        hardware = System.__find_hardware_by_name(hardware_name)
        software = System.__find_software_by_name(software_name)
        if not hardware or not software:
            return f"Some of the components do not exist"
        hardware.uninstall(software)
        System._software.remove(software)

    @staticmethod
    def analyze():
        result = ""
        result += "System Analysis\n"
        result += f"Hardware Components: {len(System._hardware)}\n"
        result += f"Software Components: {len(System._software)}\n"
        total_memory_software = sum([s.memory_consumption for s in System._software])
        total_memory_hardware = sum([h.memory for h in System._hardware])

        total_capacity_software = sum([s.capacity_consumption for s in System._software])
        total_capacity__hardware = sum([h.capacity for h in System._hardware])
        result += f"Total Operational Memory: {total_memory_software} / {total_memory_hardware}\n"
        result += f"Total Capacity Taken: {total_capacity_software} / {total_capacity__hardware}"
        return result

    @staticmethod
    def system_split():
        result = ''
        for hardware in System._hardware:
            result += f"Hardware Component - {hardware.name}\n"
            express_comp = len([c for c in hardware.software_components if c.software_type == "Express"])
            result += f"Express Software Components: {express_comp}\n"
            light_comp = len([c for c in hardware.software_components if c.software_type == "Light"])
            result += f"Light Software Components: {light_comp}\n"
            memory_used = sum(s.memory_consumption for s in hardware.software_components)
            result += f"Memory Usage: {memory_used} / {hardware.memory}\n"
            capacity_used = sum(s.capacity_consumption for s in hardware.software_components)
            result += f"Capacity Usage: {capacity_used} / {hardware.capacity}\n"
            result += f"Type: {hardware.hardware_type}\n"
            if len(hardware.software_components) == 0:
                result = f"Software Components: None\n"
            else:
                result += f"Software Components: {', '.join(s.name for s in hardware.software_components)}\n"
        return result




