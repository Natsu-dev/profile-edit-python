from .. import class_def as cd


def add_one_profile(Prf_list, line):

    # 複数行入力は許さないわよ
    ln_one = line.split("\n")[0]

    # CSV分割
    ln_list = ln_one.split(",")
    dt_list = ln_list[2].split("-")

    # 形式が合ってるか確認
    # TODO: バリデーション

    # 合ってたら構造体に格納
    Prf_one = cd.Profile(
        ln_list[0],
        ln_list[1],
        dt_list[0],
        dt_list[1],
        dt_list[2],
        ln_list[3],
        ln_list[4],
    )

    # append
    Prf_list.append(Prf_one)
    return


def cmd_add(Prf_list, line):
    add_one_profile(Prf_list, line)
    print("%A Command." "Added new profile.")
