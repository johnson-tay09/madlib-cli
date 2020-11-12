from madlib_cli.madlib import read_template, parse_template

open_sample_text = open("assets/sample.txt").read()
path = "assets/sample.txt"
string = read_template("assets/sample.txt")


def test_read_template():
    actual = read_template(path)
    expected = open_sample_text.strip()
    assert actual == expected


def test_parse_template():
    actual = parse_template(string)
    expected = [
        "Adjective",
        "Adjective",
        "A First Name",
        "Past Tense Verb",
        "A First Name",
        "Adjective",
        "Adjective",
        "Plural Noun",
        "Large Animal",
        "Small Animal",
        "A Girl's Name",
        "Adjective",
        "Plural Noun",
        "Adjective",
        "Plural Noun",
        "Number 1-50",
        "First Name's",
        "Number",
        "Plural Noun",
        "Number",
        "Plural Noun",
    ]
    assert actual == expected


# def test_merge_template():
