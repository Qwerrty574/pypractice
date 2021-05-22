from struct import *
from tkinter import *
import json


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
    window = Tk()
    window.geometry("800x1000")

    def parser(bin_s):
        bin_l = []
        final_l = []
        c = 4
        struct_l = []
        type_l = ['5s', 'H', 'b', 'H', 'i', 'Q', 'H', 'b', 'I', 'b', 'd', 'B', 'H', 'H', 'b', 'I', 'b', 'd', 'B', 'H',
                  'H',
                  'I', 'B', 'f', 'h', 'f', 'H', 'I', 'i', 'Q', 'f', 'Q']
        """
        int8 -> b(1)
        uint8 -> B(1)
        int8 -> h(2)
        uint8 -> H(2)
        int8 -> i(4)
        uint8 -> I(4)
        int8 -> q(8)
        uint8 -> Q(8)
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
            final_l.append(unpack('>{}'.format(type_l[i]), bin_l[i])[0])
        return final_l

    s = parser(s_in)

    struct_D = Struct('D', 5)
    struct_С = Struct('C', 7)
    struct_B = Struct('B', 8)
    struct_A = Struct('A', 6)

    struct_С.gen(['H', 'b', 'I', 'b', 'd', 'B', 'H'])
    struct_B.gen(['5s', 'H', 'b', 'H', 'i', 'Q', [struct_С.build(), struct_С.build()], ['d']])
    struct_A.gen([struct_B.build(), 'B', 'f', struct_D.build(), 'f', 'Q'])

    """
    struct_D.fill(
        [s[24], s[25], [unpack('>f', s_in[s[27] + i * 4:s[27] + 4 * (i + 1)])[0] for i in range(s[26])], s[28], s[29]])
    struct_C_1.fill([s[6], s[7], s[8], s[9], s[10], s[11], s[12]])
    struct_C_2.fill([s[13], s[14], s[15], s[16], s[17], s[18], s[19]])
    struct_B.fill([struct_С.build(), [], s[2], s[3], s[4], s[5], [struct_C_1.build(), struct_C_2.build()],
                   [unpack('>d', s_in[s[21] + i * 8:s[21] + 8 * (i + 1)])[0] for i in range(s[20])]])
    struct_A.fill([s[0], s[1], s[2], s[3], s[4],
                   [unpack('>d', s_in[s[21] + i * 8:s[21] + 8 * (i + 1)])[0] for i in range(s[20])]], s[31]])
    """

    output = json.dumps(struct_A.build(), indent=8)
    print(struct_A.build())
    lbl = Label(window, text=output, font=("Arial Bold", 11), padx=10, pady=5, justify=LEFT)
    lbl.grid(column=0, row=0)
    window.mainloop()

    return struct_A.build()


f31(b'GFX|eemceM\xfc8\x9e\xf2\xeb\xa9@\x0c\x91\xac\xf0\xa0Z"\x83\xa0\xd2L'
    b'W\x96]\x1d\x9b9\xbf\x94\xf8 \xd6t\xce\xc0~\x89?\x9e\x99\x0f\xfa\xc0Z9'
    b'\xc2\xbf\xe4l5\xee9e\xa0\\!R\x00\x02\x00\x00\x00o\xb4?2\xf2}\xdf'
    b'\x82\xbe\xc41\x8e\x00\x04\x00\x00\x00\x7f|V\r\xf4\xacm,z\xb5\xfb\x1f+<'
    b'\xee\xfca\xb6\xb2\xf2\x9c\n\x93i\xc1\xbf\xe8\xe8\x94\xb8\xea\xe1X?'
    b'\xe6\xec\xf6iR*\xb8\xbfx\xbc\x00\xbfcw\x1b\xbeM{\xdb\xbfG\x05\xab')
