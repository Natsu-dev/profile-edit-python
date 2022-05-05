import cmd
import class_def as cd
import numpy as np

LINE_LMT = 1024  # 標準入力の上限bytes
NAME_LMT = 70  # プロフの名前欄の上限bytes
ADRS_LMT = 70  # プロフの住所欄の上限bytes
PROF_LMT = 10000  # プロフの格納数の上限


# コマンド本体と引数のかたまりを分離
def split_command(in_val):
    return in_val.split(None, 1)


# コマンド
def switch_command(Prf_list, in_list):
    if in_list[0] == "%A":
        cmd.cmd_add(Prf_list, in_list[1])
    elif in_list[0] == "%C":
        cmd.cmd_count(Prf_list)
    elif in_list[0] == "%D":
        cmd.cmd_delete(Prf_list, in_list[1])
    elif in_list[0] == "%F":
        cmd.cmd_find(Prf_list, in_list[1])
    elif in_list[0] == "%H":
        cmd.cmd_help()
    elif in_list[0] == "%P":
        cmd.cmd_print(Prf_list, in_list[1])
    elif in_list[0] == "%R":
        cmd.cmd_read(Prf_list, in_list[1])
    elif in_list[0] == "%S":
        cmd.cmd_sort(Prf_list, in_list[1])
    elif in_list[0] == "%W":
        cmd.cmd_write(Prf_list, in_list[1])
    else:
        print("Invalid command " + str(in_list[0]) + " .\n"
            + "Please type '%H' to see the help-list for all commands.\n")


def main():

    Profile_list = []

    while True:
        print("Command: ")

        input_list = split_command(input())
        print(input_list)  # debug

        # %Qだけbreak使うので別処理
        if input_list[0] == "%Q":
            break
        else:
            # 分岐処理
            switch_command(Profile_list, input_list)


if __name__ == "__main__":
    main()
