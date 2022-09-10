# -*- coding: utf-8 -*-

intent = "SayGoodbye"


def sentences():
    return [
        ["លាហើយ"],
        ["លាហើយណា"],
        ["លាហើយអូន", ["Me"]],
        ["ខ្ញុំលាសិនហើយ", ["Inquirer"]],
        ["ជម្រាបលា"],
        ["ជួបគ្នាថ្ងៃស្អែក", ["Time:tomorrow"]],
        ["ជួបគ្នាថ្ងៃក្រោយ", ["Time:next_time"]],
        # * Implied
        ["សុខសប្បាយ"],
        # * From english
        ["បាយបាយ"],
        ["សុីយ៊ូរ"],
    ]
