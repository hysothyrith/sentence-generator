import csv
import fingerprints

from sentences import (
    FindMeetingRoom,
    FindRoomInfo,
    SayGoodbye,
    Dissatisfied,
    DoesToiletExist,
    FindToilet,
)

modules = [
    FindMeetingRoom,
    FindRoomInfo,
    SayGoodbye,
    Dissatisfied,
    DoesToiletExist,
    FindToilet,
]


def write_module(module):
    file_path = "storage/sentences/{}.csv".format(module.intent)
    with open(file_path, "w", encoding="UTF8") as file:
        writer = csv.writer(file)
        writer.writerow(["query", "entities"])

        for sentence in module.sentences():
            query = sentence[0]
            entities = ""
            # * Skip writing the entities for now
            # try:
            #     entities = "|".join(sentence[1])
            # except IndexError:
            #     pass
            writer.writerow([query, entities])


def main():
    sentence_count = 0
    for module in modules:
        if fingerprints.changed(module):
            print("Writing {}...".format(module.intent))
            write_module(module)
        else:
            print("Skipping {}...".format(module.intent))
        sentence_count += len(module.sentences())

    print("\nDone! Wrote {} sentences.".format(sentence_count))
    fingerprints.save()


if __name__ == "__main__":
    main()
