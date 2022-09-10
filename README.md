# Sentence Generator 🐍

A utility for generating Khmer sentences that can be used for training machine learning models.

## Example

```python
# -*- coding: utf-8 -*-
from dictionary.objects import toilet
from dictionary.questions import where
from utils.generation import materialize

intent = "FindToilet"


def sentences():
    return materialize(
        (toilet, "នៅ", where, "?"),
        (where, "ទៅ", toilet, "?"),
    )
```
