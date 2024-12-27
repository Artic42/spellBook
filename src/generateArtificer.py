import json
import articlib.articFileUtils as AFU
import articlib.systemUtils as sysUtils


if __name__ == "__main__":
    # Read metadata
    metaData = open("spells/metaData.json", "r")
    metaData = json.load(metaData)

    # Open the artificer template
    file = AFU.FileIO("template/artificerTemplate.tex", readIt=True)
    file.path = "artificer.tex"

    # Add cantrips
    file.addLine("\\chapter{Cantrips}")
    file.addLine("")
    artificerCantrips = {}
    for spell in metaData:
        if "Artificer" in metaData[spell]["Classes"] and metaData[spell]["Level"] == "Cantrip":
            artificerCantrips[spell] = metaData[spell]

    for spell in artificerCantrips:
        fileName = spell
        fileName = spell.replace(" ", "_")
        fileName = fileName.replace("/", "_")
        file.addLine(f"\\subfile{{spells/Cantrip/{fileName}}}")
        
    # Add rest of spells
    for i in range(1, 6):
        file.addLine(f"\\chapter{{Level {i}}}")
        file.addLine("")
        artificerSpells = {}
        for spell in metaData:
            if "Artificer" in metaData[spell]["Classes"] and metaData[spell]["Level"] == i:
                artificerSpells[spell] = metaData[spell]

        for spell in artificerSpells:
            fileName = spell
            fileName = spell.replace(" ", "_")
            fileName = fileName.replace("/", "_")
            file.addLine(f"\\subfile{{spells/{i}/{fileName}}}")

    file.addLine("\\end{document}")
    file.writeFile()
    sysUtils.command("pdflatex artificer.tex")
