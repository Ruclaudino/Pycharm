import sys
from subprocess import Popen, PIPE

######################################################################################################################
# TODO:                                                                                                              #
# 1) PUT THIS FILE IN THE SAME FOLDER AS THE PYTHON FILE CONTAINING YOUR SOLUTION                                    #
# 2) CHANGE THE NAME 'MY_FILE_NAME.py' BELOW THIS BOX TO THE NAME OF YOUR PYTHON FILE                                #
# 3) RUN THIS FILE                                                                                                   #
######################################################################################################################

YOUR_SOLUTION_FILE_NAME = "praticum.py"

######################################################################################################################
# DO NOT CHANGE ANYTHING BELOW THIS LINE                                                                             #
######################################################################################################################


# Parse the given output string into a readable string

def parse_output(full_output_string):
    try:
        print(full_output_string)
        output = str(full_output_string).replace('\\n', ' ').replace(',', '').replace('\\r', ' ').replace('(', '')\
            .replace(')', '').replace('"', '').replace('\'', '')
    except:
        output = None
    return output


# Run one test case with given input and output, return True when test succeeds, False when test fails
def run_one_test_case(inp, expected_output):
    process = Popen([sys.executable, YOUR_SOLUTION_FILE_NAME], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    (output, err) = process.communicate(inp)
    if len(str(err)) > 3:
        print(err)
        print("Je programma gooide een error. "
              "(Kijk eventueel ook na of de naam en locatie van je programma correct zijn.)")
        return False
    process.wait()
    output = output.decode('utf-8').replace("\n", "").replace("\r", "")
 #   parsed_output = parse_output(output)
    parsed_output = output[output.find("Resultaat:"):]
    if "Resultaat:" not in output:
        print("Controleer het formaat van je output! ")
        return False

    print("INPUT: ", inp.decode('utf-8').replace("\n", " / ").replace("\r", " / "))
    print("EXPECTED: ", expected_output)
    print ("OUTPUT:   ", parsed_output)
    return parsed_output == expected_output


# Retrieve a list containing all test_cases
def get_test_cases():
    test_cases = []
    # In: abc e 3 Uit: dfh
    test_cases.append((b"abc\ne\n3", "Resultaat: dfh"))
    # In: dfh d 3 Uit: abc
    test_cases.append((b"dfh\nd\n3", "Resultaat: abc"))
    # In: test e 5 Uit: ykzb
    test_cases.append((b"test\ne\n5", "Resultaat: ykzb"))
    # In: beginselen van programmeren e 11 Uit: mqtwcivdxh rxl psqjvfstmaoy
    test_cases.append((b"beginselen van programmeren\ne\n11", "Resultaat: mqtwcivdxh rxl psqjvfstmaoy"))
    # In: randomstring e 0 Uit: rbpgsryazrxr
    test_cases.append((b"randomstring\ne\n0", "Resultaat: rbpgsryazrxr"))
    #In: python is leuk e 6 Uit: vfbqyy vg bvmd
    test_cases.append((b"python is leuk\ne\n6", "Resultaat: vfbqyy vg bvmd"))
    #In: gfkzia te rt rdeymabprtf ninflz d 4 Uit: caesar is de allereerste keizer
    test_cases.append((b"gfkzia te rt rdeymabprtf ninflz\nd\n4", "Resultaat: caesar is de allereerste keizer"))
    return test_cases


# Run all given test_cases
def run_test_cases(all_tests):
    print("Alle tests worden uitgevoerd")
    print("")
    for test_nb in range(len(all_tests)):
        (inp, exp_out) = all_tests[test_nb]
        test_result = run_one_test_case(inp, exp_out)
        if test_result:
            print('Test ' + str(test_nb + 1) + ': Succeeded')
        else:
            print('Test ' + str(test_nb + 1) + ': Failed')
        print("")


# Load all test cases and test them
run_test_cases(get_test_cases())
