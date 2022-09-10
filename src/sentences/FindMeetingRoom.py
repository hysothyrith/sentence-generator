# -*- coding: utf-8 -*-
from dictionary.objects import meeting_room
from dictionary.questions import where
from utils.generation import materialize

intent = "FindMeetingRoom"

topic = [
    "អាហារូបករណ៍",
    "ការងារស្ម័គ្រចិត្ត",
]

time = [
    "ព្រឹកនេះ",
    "ម៉ោង៩",
    "ម៉ោងដប់",
    "ម៉ោងបួន",
]

person = [
    "លោកគ្រូបញ្ញា",
    "នាយកសាលា",
]

organization = [
    "ក្រសួង",
    "ស្ថានទូតអាមេរិក",
    "ធនាគារអេសុីលីដា",
    "អង្គការសហគមន៍អាមេរិក",
    "ក្រុមហ៊ុនស្មាត",
]


def sentences():
    return materialize(
        # Simple
        (where, meeting_room, "?"),
        (meeting_room, "នៅ", where, "?"),
        # With time
        (meeting_room, time, "នៅ", where, "?"),
        (where, "ទៅ", meeting_room, "នៅ", time, "?"),
        # With topic
        (meeting_room, "ពាក់ព័ន្ធនឹង", topic, "នៅ", where, "?"),
        # With person
        (where, meeting_room, "ជាមួយ", person, "?"),
        # With organization
        (where, meeting_room, "ជាមួយ", organization, "?"),
        # Complex combination
        (where, meeting_room, "ជាមួយ", person, "ពាក់ព័ន្ធនឹង", topic, "នៅ", time, "?"),
        (
            where,
            meeting_room,
            "ជាមួយ",
            person,
            "និង",
            organization,
            "រឿង",
            topic,
            "នៅ",
            time,
            "?",
        ),
    )
    return [
        # * Direct
        ["តើបន្ទប់ប្រជុំនៅទីណា?", ["MeetingRoom"]],
        ["ទីណាបន្ទប់ប្រជុំ?", ["MeetingRoom"]],
        ["ឯ​ណាបន្ទប់ប្រជុំ?", ["MeetingRoom"]],
        ["តើបន្ទប់ប្រជុំនៅកន្លែងណា?", ["MeetingRoom"]],
        ["តើបន្ទប់ប្រជុំនៅឯ​ណា?", ["MeetingRoom"]],
        # * With time
        ["តើបន្ទប់ប្រជុំម៉ោង៩នៅទីណា?", ["MeetingRoom", "Time:9"]],
        ["តើបន្ទប់ប្រជុំម៉ោង៩នៅឯណា?", ["MeetingRoom", "Time:9"]],
        ["តើបន្ទប់ប្រជុំម៉ោង៩កន្លះនៅកន្លែងណា?", ["MeetingRoom", "Time:9_30"]],
        ["តើបន្ទប់ប្រជុំរឿងម៉ោងធ្វើការនៅឯណា?", ["MeetingRoom"]],
        ["ព្រឹកនេះគេប្រជុំនៅឯណា?", ["Meeting", "Time:this_morning"]],
        # * With time and event
        [
            "តើបន្ទប់ប្រជុំកម្មវិធីព្រឹកនេះកន្លែងណា?",
            ["MeetingRoom", "Event", "Time:this_morning"],
        ],
        [
            "តើបន្ទប់ប្រជុំកម្មវិធីព្រឺកនេះទីណា?",
            ["MeetingRoom", "Event", "Time:this_morning"],
        ],
        # * With time and other related entities
        ["តើបន្ទប់ប្រជុំជាមួយលោកគ្រូបញ្ញានៅទីណា?", ["MeetingRoom", "Lecturer:panha"]],
        ["តើបន្ទប់ប្រជុំជាមួយលោកគ្រូបញ្ញានៅឯណា?", ["MeetingRoom", "Lecturer:panha"]],
        ["ឯ​ណាបន្ទប់ប្រជុំជាមួយក្រុមហ៊ុនSmart?", ["MeetingRoom", "Organization:smart"]],
        [
            "កន្លែងប្រ​ជុំជាមួយស្ថានទូតអាមេរិកនៅទីណា?",
            ["MeetingRoom", "Organization:united_states_embassy"],
        ],
        ["បន្ទប់ជួបជាមួយធនាគារអេសុីលីដានៅឯណា?", ["MeetingRoom", "Organization:acleda"]],
    ]
