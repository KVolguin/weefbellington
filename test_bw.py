from bw import remove_suffixes
from bw import switch_letters
from bw import print_in_terminal_process


def main():
    test_switch_letters()
    test_print_in_terminal_process()
    test_remove_suffixes()


def test_remove_suffixes():
    assert remove_suffixes("treating", "kingdom") == ("treat", "king")
    assert remove_suffixes("delicacy", "tratae") == ("delic", "trat")
    assert remove_suffixes("motive", "fancily") == ("mot", "fanci")
    assert remove_suffixes("potato", "tomato") == ("pot", "tom")


def test_switch_letters():
    assert switch_letters("felt", "pelt") == "Pel Fel"
    assert switch_letters("Wowie", "Zowie") == "Zowi Wowi"
    assert switch_letters("Wizard", "Harry") == "Hazar Wirr"
    assert switch_letters("Terry", "Lingle") == "Lirr Tengl"
    assert switch_letters("Tel", "Aviv") == "Av Tei"


def test_print_in_terminal_process():
    input_str = "['Buddy Holly', 'Mike Jones', 'Bill Murray']"
    expected_output = ['Hodd Bu', 'Jok Mine', 'Mul Birra']
    assert print_in_terminal_process(input_str) == expected_output
    assert print_in_terminal_process("['wat bit', 'lit man', 'tat fam']") == ['Bi Wa', 'Ma Li', 'Fa Ta']


if __name__ == "__main__":
    main()
