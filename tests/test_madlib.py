import pytest
from madlib_cli.madlib import read_template, parse_template, merge_template

open_sample_text = open("assets/sample.txt").read()
path = "assets/sample.txt"
string = read_template("assets/sample.txt")


def test_read_template():
    actual = read_template("assets/sample.txt")
    expected = open_sample_text.strip()
    assert actual == expected


def test_parse_template():
    actual_string, actual_list = parse_template(string)
    expected_string = "Make Me A Video Game!\n\nI the {} and {} {} have {}{}'s {} sister and plan to\nsteal her {} {}!\n\nWhat are a {} and backpacking {} to do? Before you can help {}, you'll have to collect \nthe {} {} and {} {} that open up the {} worlds connected to A {} Lair. \nThere are {} {} and {} {} in the game, along with hundreds of other goodies for you to find."
    expected_list = [
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
    assert actual_string == expected_string
    assert actual_list == expected_list


def test_merge():
    actual = merge_template("This {} shall {}.", ["too", "pass"])
    expected = "This too shall pass."
    assert actual == expected