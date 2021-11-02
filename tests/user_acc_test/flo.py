import builtins
from textwrap import dedent

def diff(run_calc_func,path="", sample=""):
    """[Runs a given run_calc functions and compared output with a provided sample]

    Args:
        cun_calc_func ([function]): [Runs the calculator]
        path (str, optional): [path to simulation text file defaults to ""]. Defaults to "".
        sample (str, optional): [simulated text to run if no path provided]. Defaults to "".
    """

    text = ""

    expected_lines = _parse_expected_lines(path,sample)

    responses = _extract_responses(expected_lines)



    #inner fucntion to mock print functionality
    def mock_print(*args):

        nonlocal text

        text += "".join(args) + "\n"

    
    # inner function to mock input functionality
    def mock_input(*args):

        nonlocal text

        response = reponses.pop(0)

        text += "".join(args) + response + "\n"

        return response


# functions "private" to the module use leading underscore convention
# WARNING: they are not TRULY private, which is truly pythonic
def _parse_expected_lines(path, sample):
    if path:
        with open(path) as f:
            expected_lines = f.read().splitlines()
    else:
        expected_lines = sample.splitlines()

    return expected_lines


def _extract_responses(lines):
    responses = []
    for line in lines:
        if line.startswith(">"):
            response = line.replace("> ", "").strip()
            responses.append(response)

    return responses

def _find_differences(text, expected_lines):
    
    actual_lines = text.splitlines()

    differences = []

    for i in range(len(expected_lines)):

        try:
            actual = actual_lines[i]

            expected = expected_lines[i]

            if actual != expected:
                difference = _format_difference(actual, expected, i + 1)
                differences.append(difference)

        except IndexError:
            break

    actual_lines_length = len(actual_lines)
    expected_lines_length = len(expected_lines)

    if actual_lines_length < expected_lines_length:

        difference = _format_difference(
            "", expected_lines[actual_lines_length], actual_lines_length
        )
        differences.append(difference)

    elif actual_lines_length > expected_lines_length:

        difference = _format_difference(
            "", actual_lines[expected_lines_length], expected_lines_length
        )
        differences.append(difference)

    return differences


def _format_difference(actual, expected, line_num):

    msg = f"""
        Difference on line {line_num}:
        Actual:
        {actual}
        Expected:
        {expected}
    """

    return dedent(msg)