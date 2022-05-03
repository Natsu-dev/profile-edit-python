from commands import cmd_a, cmd_c, cmd_p, cmd_r, cmd_w, cmd_f, cmd_s, cmd_d, cmd_h

LINE_LMT = 1024  # 標準入力の上限bytes
NAME_LMT = 70  # プロフの名前欄の上限bytes
ADRS_LMT = 70  # プロフの住所欄の上限bytes
PROF_LMT = 10000  # プロフの格納数の上限


class date:
    def __init__(self, year, month, day) -> None:
        self.year = year
        self.month = month
        self.day = day


class profile:
    def __init__(self, id, name, year, month, day, address, note) -> None:
        self.id = id
        self.name = name
        self.date = date(year, month, day)
        self.address = address
        self.note = note


# コマンド本体と引数のかたまりを分離
def split_command(in_val):
    return in_val.split(None, 1)


# コマンド
def switch_command(in_list):
    if in_list[0] == "%A":
        cmd_a.cmd_add(in_list[1])
    elif in_list[0] == "%C":
        cmd_c.cmd_count(in_list[1])
    elif in_list[0] == "%P":
        cmd_p.cmd_print(in_list[1])
    elif in_list[0] == "%R":
        cmd_r.cmd_read(in_list[1])
    elif in_list[0] == "%W":
        cmd_w.cmd_write(in_list[1])
    elif in_list[0] == "%F":
        cmd_f.cmd_find(in_list[1])
    elif in_list[0] == "%S":
        cmd_s.cmd_sort(in_list[1])
    elif in_list[0] == "%D":
        cmd_d.cmd_delete(in_list[1])
    elif in_list[0] == "%H":
        cmd_h.cmd_help()


def main():
    while True:
        print("Command: ")

        input_list = split_command(input())
        print(input_list) # debug

        # %Qだけbreak使うので別処理
        if input_list[0] == "%Q":
            break
        else:
            # 分岐処理
            switch_command(input_list)


if __name__ == "__main__":
    main()
