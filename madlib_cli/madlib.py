print(
    """
**************************************
**   Welcome to the Madlib Game!   **
**   Please respond to the prompts. **
**************************************
"""
)
# with open("assets/sample.txt") as file:
#     print(file.read())
open_sample = open("assets/sample.txt")
import re


def read_template(path):
    content = open(path).read()
    return content.strip()


string = read_template("assets/sample.txt")


def parse_template(string):
    split_template_list = re.findall(r"\{(.*?)\}", string)
    # print(split_template_list)
    print(re.sub(r"\{(.*?)\}", "{}", string))
    return split_template_list


print(parse_template(string))


def merge_template(bare_temp, term_list):