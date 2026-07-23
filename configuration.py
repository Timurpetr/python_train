class CPU:
    def __init__(self, name, fr):
        self.name = name
        self.fr = fr


class Memory:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume


class MotherBoard:
    def __init__(self, name, cpu, *mem_slots, total_mem_slots=4):
        if len(mem_slots) > total_mem_slots:
            raise ValueError(f"Максимум слотов: {total_mem_slots}!")
        self.name = name
        self.cpu = cpu
        self.mem_slots = mem_slots
        self.total_mem_slots = total_mem_slots

    def get_config(self):
        mem_details = [f"{m.name} - {m.volume}" for m in self.mem_slots]
        mem_string = "; ".join(mem_details) if mem_details else "Нет памяти"
        return [
            f"Материнская плата: {self.name}",
            f"Центральный процессор: {self.cpu.name}, {self.cpu.fr}",
            f"Слотов памяти: {self.total_mem_slots}",
            f"Память: {mem_string}",
        ]


mb = MotherBoard("asdads", CPU("MB", 0), Memory("MB", "2000"), Memory("MB", "2000"))

# cpu = CPU(наименование, тактовая частота)
# mem = Memory(наименование, размер памяти)
# mb = MotherBoard(наименование, процессор, память1, память2, ..., памятьN) (максимум N = 4)
