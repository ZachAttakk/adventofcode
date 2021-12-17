import sys
from timeit import default_timer as timer
from colorama.ansi import Cursor
from zUtils.utils import *

data: list[str] = []

# FILENAME FOR INPUT DATA
INPUT_FILENAME: str = "day16.txt"


class Packet:
    version: int = -1
    type_id: int = -1
    sub_type: int = -1
    value: str = ""

    def __init__(self, *, version=-1, type_id=-1, value: str = "", sub_type: int = -1) -> None:
        self.version = version
        self.type_id = type_id
        self.value = value

    def __repr__(self) -> str:
        if self.sub_type >= 0:
            return f"{self.type_id}(v{self.version}): Sub-Type:{self.sub_type}"

        return f"{self.type_id}(v{self.version}): {self.value}"


class Bitfeed:

    # Class variables
    bits: str = ""
    cursor: int = 0

    def __init__(self, bits: str = "") -> None:
        self.bits = bits

    @classmethod
    def from_hex(cls, hex: str):
        values = [format(int(i, 16), 'b').zfill(4) for i in hex]
        bits = "".join(values)
        return cls(bits)

    def next(self, length: int = 1) -> str:
        if self.done:
            return ""

        st: int = self.cursor
        end: int = min(st+length, len(self.bits))
        self.cursor = end
        return self.bits[st:end]

    @property
    def done(self) -> bool:
        if self.cursor >= len(self.bits) or int(self.bits[self.cursor:], 2) == 0:
            return True
        else:
            return False

    def __repr__(self) -> str:
        if not self.done:
            return self.bits[self.cursor:]
        else:
            return f"{self.bits[self.cursor:]}(done)"

    # INIT
    # Code for startup

    def parse_literal(self, length: int = -1) -> int:
        num: str = ""
        keep_reading: bool = True

        if length > 0:  # specific length
            num = self.next(length)
            return int(num, 2)

        # reading according to 5 group with starter bit
        # first bit says number continues
        while keep_reading:
            _group: str = self.next(5)
            if len(_group) == 0:
                break

            keep_reading = bool(int(_group[0]))
            num += str(_group[1:])

        printDebug(f"Literal: {int(num, 2)}")
        return int(num, 2)

    def parse(self, *, depth: int = 0, number: int = -1) -> List[Packet]:
        """Parse bits according to their TypeID.

        Args:
            depth (int, optional): Depth of recursion. Defaults to 0, pass in +1 for each level
            number (int, optional): Number of packets to read before returning. Defaults to -1.

        Returns:
            List[Packet]: List of parsed packets with their version and their value
        """
        result: List[Packet] = []

        packet_countdown: int = number

        while not self.done and packet_countdown != 0:
            packet_countdown -= 1

            # 3 bits header with version number
            version = int(self.next(3), 2)

            type_id = int(self.next(3), 2)
            new_packet: Packet = Packet(version=version, type_id=type_id)
            printDebug(new_packet)
            match type_id:
                case 4:  # literal number
                    new_packet.value = str(self.parse_literal())
                    result.append(new_packet)
                case _:  # sub-packets
                    subpacket_type: int = int(self.next())
                    new_packet.sub_type = subpacket_type
                    result.append(new_packet)
                    match subpacket_type:
                        case 0:  # 15 bits of describing total length in bits
                            bit_length: int = self.parse_literal(15)
                            sub_packet_feed: Bitfeed = Bitfeed(self.next(bit_length))
                            result += sub_packet_feed.parse(depth=depth+1)
                        case 1:  # 11 bits describing number of sub-packets
                            packet_count: int = self.parse_literal(length=11)
                            result += self.parse(number=packet_count, depth=depth+1)
                        case _:
                            printBad(
                                f"Type ID {type_id} and subpacket type {subpacket_type} not found")

        if depth == 0:
            # FIXME: Prevent race conditions when accessed directly
            self.cursor = 0

        return result


start_time = timer()
data = advent_init(INPUT_FILENAME, sys.argv, clear_screen=False)

bits = Bitfeed.from_hex(data[0])

# HERE WE GO
printOK(bits.parse())

printGood(f"Part 1: {sum([a.version for a in bits.parse()])}")


printOK("Time: %.5f seconds" % (timer()-start_time))
