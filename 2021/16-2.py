import sys
from timeit import default_timer as timer
from math import prod
from zUtils.utils import *

data: list[str] = []

# FILENAME FOR INPUT DATA
INPUT_FILENAME: str = "day16.txt"


class Packet:
    version: int = -1
    type_id: int = -1
    sub_type: int = -1
    value: int

    def __init__(self, *, version=-1, type_id=-1, value: int = -1, sub_type: int = -1) -> None:
        self.version = version
        self.type_id = type_id
        self.value = value

    def __repr__(self) -> str:
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
        return_value: str = self.peak(length)
        self.cursor += length
        return return_value

    def peak(self, length: int = 1) -> str:
        if self.cursor >= len(self.bits):
            return ""

        st: int = self.cursor
        end: int = min(st+length, len(self.bits))
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
            if type_id == 4:  # literal number
                new_packet.value = self.parse_literal()
                printDebug("-"*depth + f"literal: {new_packet.value}")
            else:  # operator
                subpacket_type: int = int(self.next())
                new_packet.sub_type = subpacket_type
                values: List[Packet] = []
                match subpacket_type:
                    case 0:  # 15 bits of describing total length in bits
                        bit_length: int = self.parse_literal(15)
                        sub_packet_feed: Bitfeed = Bitfeed(self.next(bit_length))
                        values += sub_packet_feed.parse(depth=depth+1)
                    case 1:  # 11 bits describing number of sub-packets
                        packet_count: int = self.parse_literal(length=11)
                        values += self.parse(number=packet_count, depth=depth+1)
                    case _:
                        printBad(
                            f"Type ID {type_id} and subpacket type {subpacket_type} not found")

                # Do with the packets what needs to be done
                match type_id:
                    case 0:  # sum
                        new_packet.value = sum([a.value for a in values])
                        printDebug("-"*depth + f"sum: {values}: {new_packet.value}")
                    case 1:  # product
                        new_packet.value = prod([a.value for a in values])
                        printDebug("-"*depth + f"prod: {values}: {new_packet.value}")
                    case 2:  # min
                        new_packet.value = min([a.value for a in values])
                        printDebug("-"*depth + f"min: {values}: {new_packet.value}")
                    case 3:  # max
                        new_packet.value = max([a.value for a in values])
                        printDebug("-"*depth + f"max: {values}: {new_packet.value}")
                    case 5:  # greater than
                        new_packet.value = 1 if values[0].value > values[1].value else 0
                        printDebug("-"*depth + f"greater: {values}: {new_packet.value}")
                    case 6:  # less than
                        new_packet.value = 1 if values[0].value < values[1].value else 0
                        printDebug("-"*depth + f"less: {values}: {new_packet.value}")
                    case 7:  # equal
                        new_packet.value = 1 if values[0].value == values[1].value else 0
                        printDebug("-"*depth + f"equal: {values}: {new_packet.value}")
                    case _:
                        printBad(
                            f"Type ID {type_id} and subpacket type {subpacket_type} not found")

            # Add the result to the list
            result.append(new_packet)

        if depth == 0:
            # FIXME: Prevent race conditions when accessed directly
            self.cursor = 0

        return result


def main():
    start_time = timer()
    data = advent_init(INPUT_FILENAME, sys.argv, clear_screen=False)

    for i in data:
        printOK(i)
        bits = Bitfeed.from_hex(i)
        printGood(bits.parse())

    printOK("Time: %.5f seconds" % (timer()-start_time))


if __name__ == "__main__":
    main()
