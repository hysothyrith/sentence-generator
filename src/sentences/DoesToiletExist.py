# -*- coding: utf-8 -*-
from dictionary.adjectives import exists, has
from dictionary.objects import toilet
from dictionary.questions import yes_or_no
from utils.generation import materialize


subject = [
    "នឹង",
    "នេះ",
    "កន្លែងនេះ",
    "កន្លែងនឹង",
    "អាគារនេះ",
    "អាគារនឹង",
    "សាលានឹង",
    "សាលានេះ",
    "ជាន់នឹង",
    "ជាន់នេះ",
    "ជាន់ផ្ទាល់ដី",
    "ជាន់ក្រោម",
    "ជាន់លើ",
    "ជាន់ទី១",
    "ជាន់ទី២",
    "ជាន់ខ្ពស់គេបំផុត",
    "ជាន់ខ្ពស់គេបង្អស់",
    "ជាន់លើគេបំផុត",
    "ជាន់លើគេបង្អស់",
]


def sentences():
    return materialize(
        (toilet, exists, yes_or_no, "?"),
        (exists, toilet, yes_or_no, "?"),
        (toilet, exists, yes_or_no, "នៅ", subject, "?"),
        (exists, toilet, yes_or_no, "នៅ", subject, "?"),
        (subject, has, toilet, yes_or_no, "?"),
        ("នៅ", subject, exists, toilet, yes_or_no, "?"),
    )
