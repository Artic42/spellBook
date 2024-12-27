import json
import articlib.articFileUtils as AFU


if __name__ == "__main__":
    className = "Ranger"
    template = "template/rangerTemplate.tex"

    # Read metadata
    metaData = open("spells/metaData.json", "r")
    metaData = json.load(metaData)

    # Open the artificer template
    file = AFU.FileIO(template, readIt=True)
    file.path = f"{className}.tex"

    # Add cantrips
    cantrips = {}
    for spell in metaData:
        if className in metaData[spell]["Classes"] and metaData[spell]["Level"] == "Cantrip":
            cantrips[spell] = metaData[spell]

    if len(cantrips) != 0:
        file.addLine("\\chapter{Cantrips}")
        for spell in cantrips:
            fileName = spell
            fileName = spell.replace(" ", "_")
            fileName = fileName.replace("/", "_")
            file.addLine(f"\\subfile{{spells/Cantrip/{fileName}}}")

    # Add rest of spells
    for i in range(1, 6):
        file.addLine("")
        spells = {}
        for spell in metaData:
            if className in metaData[spell]["Classes"] and metaData[spell]["Level"] == i:
                spells[spell] = metaData[spell]
        if len(spells) != 0:
            file.addLine(f"\\chapter{{Level {i}}}")
        for spell in spells:
            fileName = spell
            fileName = spell.replace(" ", "_")
            fileName = fileName.replace("/", "_")
            file.addLine(f"\\subfile{{spells/{i}/{fileName}}}")

    file.addLine("\\end{document}")
    file.writeFile()
