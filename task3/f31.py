from struct import *


class Struct:
    s_size = None
    name = None
    struct = None

    def __init__(self, name, s_size):
        self.s_size = s_size
        self.name = name
        keys = ['{}{}'.format(self.name, i) for i in range(1, self.s_size + 1)]
        self.struct = dict.fromkeys(keys)

    @staticmethod
    def retype(value):
        if isinstance(value, dict) or isinstance(value, list):
            return value
        elif isinstance(value, int):
            return int(value)
        elif isinstance(value, float):
            return float(value)
        elif isinstance(value, bytes):
            return value.decode("utf-8")
        else:
            return str(value)

    def gen(self, f):
        for i in range(1, self.s_size + 1):
            self.struct['{}{}'.format(self.name, i)] = f[i - 1]

    def fill(self, value):
        for i in range(1, self.s_size + 1):
            self.struct['{}{}'.format(self.name, i)] = self.retype(value[i - 1])

    def build(self):
        return self.struct


def f31(s_in):
    def parser(bin_s):
        bin_l = []
        final_l = []
        c = 3
        struct_l = []
        """
        type_l = ['5s', 'H', 'b', 'H', 'i', 'Q', 'H', 'b', 'I', 'b', 'd', 'B', 'H', 'H', 'b', 'I', 'b', 'd', 'B', 'H',
                  'H',
                  'I', 'B', 'f', 'h', 'f', 'H', 'I', 'i', 'Q', 'f', 'Q']
        """
        type_l = ['H', 'H', 'Q', 'H', 'H', 'H', 'I', 'H', 'H', 'B', 'i', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'b', 'd',
                  'I', 'I', 'H', 'f', 'I', 'h', 'b', 'Q', 'B', 'H', 'I', 'i', 'B', 'f']

        """
        int8 -> b(1)
        uint8 -> B(1)
        int16 -> h(2)
        uint16 -> H(2)
        int32 -> i(4)
        uint32 -> I(4)
        int64 -> q(8)
        uint64 -> Q(8)
        char[] -> s(1)
        double -> d(8)
        float -> f(4)
        """
        for i in type_l:
            struct_l.append(calcsize(i))
        for i in struct_l:
            bin_l.append(bin_s[c:c + i])
            c += i
        for i in range(len(type_l)):
            final_l.append(unpack('<{}'.format(type_l[i]), bin_l[i])[0])
        return final_l

    s = parser(s_in)

    struct_F = Struct('F', 5)
    struct_E = Struct('E', 5)
    struct_D = Struct('D', 4)
    struct_С = Struct('C', 3)
    struct_B_2 = Struct('B', 4)
    struct_B_1 = Struct('B', 4)
    struct_A = Struct('A', 4)
    """
    struct_D.fill(
        [s[24], s[25], [unpack('>f', s_in[s[27] + i * 4:s[27] + 4 * (i + 1)])[0] for i in range(s[26])], s[28], s[29]])
    """
    """
    struct_B_1.fill(
        [[unpack('>H', s_in[(int(unpack('>H', s_in[s[0]]))) + i * 2:(s[0]) + 2 * (i + 1)])[0] for i in range()], s[6],
         s[7],
         [unpack('>H', s_in[s[8] + i * 2:s[8] + 2 * (i + 1)])[0] for i in range(20)]])
    """
    """
    struct_B_2.fill([s[13], s[14], s[15], s[16], s[17], s[18], s[19]])
    """
    """
    struct_B.fill([s[0], s[1], s[2], s[3], s[4], s[5], [struct_C_1.build(), struct_C_2.build()],
                   [unpack('>d', s_in[s[21] + i * 8:s[21] + 8 * (i + 1)])[0] for i in range(s[20])]])
    """

    print(s[3])

    def repack(in_s, adr, type, fix):
        size = 0
        if type == 'b' or type == 's' or type == 'B':
            size = 1
        elif type == 'b' or type == 'h' or type == 'H':
            size = 2
        elif type == 'f' or type == 'i' or type == 'I':
            size = 4
        elif type == 'd' or type == 'q' or type == 'Q':
            size = 8
        return unpack('<{}'.format(type), in_s[adr + fix:adr + fix + size])

    struct_A.fill([[struct_B_1.build(), struct_B_2.build()], s[0], struct_E.build(), struct_F.build()])

    adr_E = int(s[3])
    struct_E.fill([repack(s_in, adr_E, 'f', 0), repack(s_in, adr_E, 'I', 4), repack(s_in, adr_E, 'h', 8),
                   repack(s_in, adr_E, 'b', 10), repack(s_in, adr_E, 'Q', 11)])
    adr_F = int(s[4])
    struct_F.fill([repack(s_in, adr_F, 'B', 0), [
        [repack(s_in, repack(s_in, adr_F, 'I', 3)[0], 'i', p) for p in range(repack(s_in, adr_F, 'H', 1)[0])]],
                   repack(s_in, adr_F, 'i', 7), repack(s_in, adr_F, 'B', 11), repack(s_in, adr_F, 'f', 12)])
    adr_D = 0
    struct_D.fill([repack(s_in, adr_D, 'b', 0), repack(s_in, adr_D, 'b', 0), repack(s_in, adr_D, 'b', 0),
                   [repack(s_in, repack(s_in, adr_F, 'I', 3)[0], 'i', p) for p in
                    range(repack(s_in, adr_F, 'H', 1)[0])]])
    return struct_A.build()


"""
Struct sizes:
A 16
B 10
C 19
D 20
E 19
F 16
"""

print(f31(b'VXOE\x00\x81\x00\xa2!\xabV\\=\x90\x9b\x8b\x00\xa6\x00$\xcf\x14\xbbi'
          b"?\xc1\xb4\xb2\xa0*\xc8_\x06 \x8c\xc1n\x97\xf1'\xf0\xf7\x14\x8f"
          b'\xd2\x89\xc5\xc7\x042_\xe0\xe0\xc4\xf2P\xc2\xee?[o\xf8\xa2\x06\x00\x00\x00&'
          b'\x00\x13\x00\xf2\xfe\x9e\xe1\xb1i2\x00\x95\xfdh1i\xa9\t\xc0\x82\xfciO\x87'
          b'q\xca\xad5\x86v\xee\xb7\x1br.\xa0W\xb4\xcf\x02>\x1b\xa3\x9c\xe1|\n\x15'
          b'\xf4\xdb\xbf\xc1\x1fnf\x06\x00\x00\x00b\x00O\x00\x97G\x9a\xb1\xb8Bn\x00\x94'
          b'2X?Z|po\x86t:8\xc9\xc1\x00\x86U\xf1\n\xb9`\x9b\x8c9\xbd(\xc4\xea\x02'
          b'\x00\x9e\x00\x00\x00\xc9W\xbd\x0c\xf1p\x14~\xbd'))
