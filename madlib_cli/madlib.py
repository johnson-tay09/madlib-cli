import re


def read_template(path):
    with open(path) as file:
        content = file.read()
        stripped_content = content.strip()
    return stripped_content


def parse_template(string):
    split_template_list = re.findall(r"\{(.*?)\}", string)
    # print(split_template_list)
    split_string = re.sub(r"\{(.*?)\}", "{}", string)
    return split_string, split_template_list


def merge_template(bare_temp, resp):
    return bare_temp.format(*resp)


if __name__ == "__main__":
    print(
        """
    **************************************
    **   Welcome to the Madlib Game!   **
    **   Please respond to the prompts. **
    **************************************
    """
    )
    string = read_template("assets/sample.txt")
    # print(parse_template(string))
    responses = []
    bare_string, word_list = parse_template(string)
    # print(word_list)
    for word in word_list:
        response = input(f"Give me a {word} >")
        responses.append(response)
    print(responses)
    print(merge_template(bare_string, responses))