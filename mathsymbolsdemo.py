import mathsymbols as ms


def main():

    print("------------------------")
    print("| codedrome.com        |")
    print("| Mathematical Symbols |")
    print("------------------------\n")

    # ms.print_symbols()

    # f = ms.search("root")
    # ms.print_symbols(f)

    # print using dictionary key
    print(f"12{ms.symbols['superscript_two_2']} = {12**2}")

    # print using symbols copied/pasted into code
    print(f"⅝ + ⅛ = ¾")

    # print using decimal Unicode
    temp_celsius = 18.5
    print(f"The temperature is {temp_celsius}{chr(8451)}")

    # print using hexadecimal Unicode
    print("\u221e + \u221e = \u221e")


if __name__ == "__main__":

    main()
