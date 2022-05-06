from datetime import datetime
import class_def as cd


# ===== modules =====

# 成功時: True, 失敗時: False
def add_one_profile(Prf_list, line):

    # 複数行入力は許さないわよ、改行を許すな
    ln_one = line.split("\n")[0]

    # CSV分割
    ln_list = ln_one.split(",")
    dt_list = ln_list[2].split("-")

    # バリデーション
    if not (len(ln_list) == 5 and len(dt_list) == 3):
        print("Number of elements is incorrect.")
        return False

    try:
        datetime.strptime(ln_list[2], "%Y-%m-%d")
    except ValueError as e:
        print("Date of the input data is incorrect.", e)
        return False

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
    return True


def print_profiles(Prf_list, option):

    try:
        int(option)
    except ValueError as e:
        print(
            "Invalid option "
            + str(option)
            + " .\n"
            + "Please type '%H' to see the help-list for all commands.\n",
            e,
        )
        return False

    if option == 0:
        for p in Prf_list:
            print(
                "==Profile No.{}==\nId    : {}\nName  : {}\nBirth : {}-{}-{}\nAddr. : {}\nComm. : ".format(
                    Prf_list[p].id,
                    Prf_list[p].name,
                    Prf_list[p].date.year,
                    Prf_list[p].date.month,
                    Prf_list[p].date.day,
                    Prf_list[p].address,
                    Prf_list[p].note,
                )
            )
    return True


# ===== cmds =====


def cmd_add(Prf_list, line):
    add_one_profile(Prf_list, line)
    print("%A Command.\n" "Added new profile.\n")
    return


def cmd_count(Prf_list):
    print("%C Command.\n" + str(len(Prf_list)) + " profile(s).\n")
    return


def cmd_delete(Prf_list, line):
    try:
        Prf_list.pop(int(line))
    except ValueError as e:
        print(
            "Invalid option "
            + str(line)
            + " .\n"
            + "Please type '%H' to see the help-list for all commands.\n",
            e,
        )
        return False
    except IndexError as e:
        print("The number is invalid.", e)
        return False

    print("%D Command.\nDeleted Profile in No." + str(line))
    return True


# TODO
def cmd_find():
    print("%F Command.")
    return


def cmd_help():
    print(
        "Help:\n"
        "To add a new profile, type string with following template.\n"
        "{ID: 7},{Name: < 70},{Year: 4}-{Month: < 3}-{Date: < 3},"
        "{Addr: < 70},{Comm: Any}\n"
        "Numbers are the characters you can insert.\n"
        "\n"
        "To run functions, type command and parameter with following template.\n"
        "%%{Command} {Parameter}\n"
        "\n"
        "---List of Commands---\n"
        "H (Help)  : Show command list for help\n"
        "     Param:\n"
        "Q (Quit)  : Close and quit the program\n"
        "     Param:\n"
        "C (Count) : Count and show the number of profiles in memory\n"
        "     Param:\n"
        "P (Print) : Print profiles in memory\n"
        "     Param: 0 - Show all\n"
        "     {Positive number} - Show profiles from the first one to the number's\n"
        "     {Negative number} - Show profiles from the number's one to the last\n"
        "R (Read)  : Read and insert profiles into memory from CSV file\n"
        "     Param: {filename}.csv\n"
        "W (Write) : Write profiles in memory into CSV file\n"
        "     Param: {filename}.csv\n"
        "F (Find)  : Find profiles matching a string\n"
        "     Param: {string}\n"
        "S (Sort)  : Sort profiles in memory\n"
        "     Param: 1 - Sort by ID\n"
        "D (Delete): Delete a profile in memory\n"
        "     Param: {Profile No.}\n"
    )
    return


def cmd_print(Prf_list, line):

    print_profiles(Prf_list, line)
    return


def cmd_read(Prf_list, line):
    # TODO ファイル名バリデーション
    try:
        with open(line) as f:
            l = f.readlines()
            add_count = 0
            for p in l:
                if add_one_profile(Prf_list, p):
                    add_count += 1

            print("Added {} profiles.".format(add_count))
            return True
    except FileNotFoundError as e:
        print("Something went wrong when opening file: '" + str(line) + "'.", e)
        return False


# TODO
def cmd_sort():
    print("%S Command.")
    return


# TODO
def cmd_write():
    print("%W Command.")
    return
