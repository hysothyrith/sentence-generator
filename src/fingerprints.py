import pickle
import hashlib


def load() -> dict:
    try:
        with open("storage/fingerprints.pickle", "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return {}


def save():
    with open("storage/fingerprints.pickle", "wb") as file:
        pickle.dump(fingerprints, file)


fingerprints = load()


def changed(module) -> bool:
    hash = hashlib.md5(str(module.sentences()).encode("utf-8")).hexdigest()
    if fingerprints.get(module.intent) == hash:
        return False

    fingerprints[module.intent] = hash
    return True
