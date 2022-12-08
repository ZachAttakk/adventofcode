import sys
from timeit import default_timer as timer
from zUtils.utils import *

data: list[str] = []

# FILENAME FOR INPUT DATA
INPUT_FILENAME: str = "07.txt"


class Elf_dir_tree:
    def __init__(self):
        self.capacity = 70000000
        self._space_used = -1
        self.structure = [Elf_dir("/")]

    def _calc_folder_sizes(self):
        # update folders
        for i in self.structure:
            if type(i) == Elf_dir:
                i.calc_size(self.structure)
                if i.fullname == "/":
                    # update total
                    self._space_used = i.size

    def add(self, new_object):
        self.structure.append(new_object)
        # We probably only have to calculate the ones that changed
        self._calc_folder_sizes()

    @property
    def space_used(self):
        if self._space_used < 0:
            self._calc_folder_sizes()
        return self._space_used

    @property
    def space_available(self):
        return self.capacity-self.space_used

    def sum_size_capped(self, size):
        total = 0
        for i in self.structure:
            if type(i) == Elf_dir and i.size <= size:
                total += i.size
        return total

    def smallest_big_file(self, size):
        candidate_size = self.capacity
        for i in self.structure:
            if type(i) == Elf_dir and i.size > (size-self.space_available) and i.size < candidate_size:
                candidate_size = i.size
        return candidate_size


class Elf_dir:
    def __init__(self, fullname):
        self.fullname = fullname
        self._size = -1

    def __repr__(self) -> str:
        return "dir: "+self.fullname

    @property
    def name(self):
        return self.fullname[self.fullname.rfind('/', 0, -1)+1:-1]

    @property
    def parent(self):
        return self.fullname[:-len(self.name)-1]

    def in_folder(self, folder_name):
        if self.fullname.startswith(folder_name):
            return True
        return False

    @property
    def size(self):
        """Size of folder. If result is -1, call calc_size()

        Returns:
            int: Size of folder
        """
        return self._size

    def calc_size(self, structure):
        self._size = 0
        for f in structure:
            if type(f) == Elf_file and f.in_folder(self.fullname):
                self._size += f.size


class Elf_file:
    def __init__(self, fullname, size):
        self.fullname = fullname
        self.size = size

    def __repr__(self) -> str:
        return f"{self.fullname} {self.size}"

    @property
    def name(self):
        return self.fullname[self.fullname.rindex('/')+1:]

    @property
    def parent(self):
        return self.fullname[:-len(self.name)]

    def in_folder(self, folder_name):
        if self.fullname.startswith(folder_name):
            return True
        return False


def parse_structure(data):
    cur_path = "/"
    structure = Elf_dir_tree()
    for line in data:
        cmd = line.split(' ')
        if line.startswith("$ cd "):  # directory change
            match cmd[-1]:
                case "/":  # go back to zero
                    cur_path = "/"
                case "..":  # up one1
                    cur_path = cur_path[0:cur_path.rindex('/', 0, -1)+1]
                case _:  # new folder
                    cur_path += cmd[-1] + '/'
                    structure.add(Elf_dir(cur_path))
        elif cmd[0].isnumeric():  # it's a file
            structure.add(Elf_file(cur_path+cmd[1], int(cmd[0])))
    return structure


def main():

    # INIT
    # Code for startup
    start_time = timer()
    data = advent_init(INPUT_FILENAME, sys.argv, clear_screen=True)

    # turn data into folder structure
    file_list = parse_structure(data)

    # HERE WE GO
    printGood(file_list.sum_size_capped(100000))
    printOK("Time: %.5f seconds" % (timer()-start_time))


if __name__ == "__main__":
    main()
