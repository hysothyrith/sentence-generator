# Sentence Generator 🐍

A utility for generating Khmer sentences that can be used for training machine learning models.

## Example

```python
# -*- coding: utf-8 -*-
from utils.generation import materialize

where = [
    "ទីណា",
    "កន្លែងណា",
]

bathroom = [
    "បង្គន់",
    "បន្ទប់ទឹក",
]

print(
    materialize(
        ("តើ", bathroom, "នៅ", where, "?"),
        (where, "ទៅ", bathroom, "?"),
    )
)

# Output:
# [
#     ["តើបង្គន់នៅទីណា?"],
#     ["តើបង្គន់នៅកន្លែងណា?"],
#     ["តើបន្ទប់ទឹកនៅទីណា?"],
#     ["តើបន្ទប់ទឹកនៅកន្លែងណា?"],
#     ["ទីណាទៅបង្គន់?"],
#     ["ទីណាទៅបន្ទប់ទឹក?"],
#     ["កន្លែងណាទៅបង្គន់?"],
#     ["កន្លែងណាទៅបន្ទប់ទឹក?"],
# ]
```
