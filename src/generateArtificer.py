import json
import articlib.articFileUtils as AFU


if __name__ == "__main__":
    # Read metadata
    metaData = open("spells/metaData.json", "r")
    metaData = json.load(metaData)

    # Open the artificer template
    file = AFU.FileIO("template/artificerTemplate.tex", readIt=True)
    file.path = "artificer.tex"

    # Add cantrips
    artificerCantrips = {}
    for spell in metaData:
        if "Artificer" in metaData[spell]["Classes"] and metaData[spell]["Level"] == "Cantrip":
            artificerCantrips[spell] = metaData[spell]

    if len(artificerCantrips) != 0:
        file.addLine("\\chapter{Cantrips}")
        for spell in artificerCantrips:
            fileName = spell
            fileName = spell.replace(" ", "_")
            fileName = fileName.replace("/", "_")
            file.addLine(f"\\subfile{{spells/Cantrip/{fileName}}}")

    # Add rest of spells
    for i in range(1, 10):
        artificerSpells = {}
        for spell in metaData:
            if "Artificer" in metaData[spell]["Classes"] and metaData[spell]["Level"] == i:
                artificerSpells[spell] = metaData[spell]

        if len(artificerSpells) != 0:
            file.addLine(f"\\chapter{{Level {i}}}")
            for spell in artificerSpells:
                fileName = spell
                fileName = spell.replace(" ", "_")
                fileName = fileName.replace("/", "_")
                file.addLine(f"\\subfile{{spells/{i}/{fileName}}}")

    file.addLine("\\end{document}")
    file.writeFile()
