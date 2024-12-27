import csv
import json
import articlib.articFileUtils as AFU


def readCSV(file: str) -> dict:
    FP = open(file, "r")
    csvReader = csv.DictReader(FP)
    data = [row for row in csvReader]
    FP.close()
    return data


def readSpellTemplate() -> AFU.FileIO:
    File = AFU.FileIO("spellTemplate.txt", readIt=True)
    return File


def cleanOld() -> None:
    AFU.deleteDirectory("spells")
    AFU.createDirectory("spells")
    AFU.createDirectory("spells/Cantrip")
    AFU.createDirectory("spells/1")
    AFU.createDirectory("spells/2")
    AFU.createDirectory("spells/3")
    AFU.createDirectory("spells/4")
    AFU.createDirectory("spells/5")
    AFU.createDirectory("spells/6")
    AFU.createDirectory("spells/7")
    AFU.createDirectory("spells/8")
    AFU.createDirectory("spells/9")


def writeSpell(spell: dict, file: AFU.FileIO) -> AFU.FileIO:
    # Read spell
    spellName = spell["Name"]
    spellLevel = spell["Level"]
    spellSchool = spell["School"]
    spellSource = spell["Source"]
    spellPage = spell["Page"]
    spellCastingTime = spell["Casting Time"]
    spellRange = spell["Range"]
    spellComponents = spell["Components"]
    spellDuration = spell["Duration"]
    spellClasses = spell["Classes"]
    spellDescription = spell["Text"]
    spellAtHigherLevels = spell["At Higher Levels"]
    spellAtHigherLevels = spellAtHigherLevels[19:]
    if spellAtHigherLevels == "":
        noHigherLevels = True
    else:
        noHigherLevels = False

    # Remove last line if no higher levels
    file.readFile()
    if noHigherLevels:
        file.removeLastLine()
    # Replace all the values
    file.findAndReplace("$SPELL_NAME$", spellName)
    file.findAndReplace("$SPELL_LEVEL$", spellLevel)
    file.findAndReplace("$SPELL_SCHOOL$", spellSchool)
    file.findAndReplace("$SPELL_SOURCE$", spellSource)
    file.findAndReplace("$SPELL_PAGE$", spellPage)
    file.findAndReplace("$SPELL_CASTING_TIME$", spellCastingTime)
    file.findAndReplace("$SPELL_RANGE$", spellRange)
    file.findAndReplace("$SPELL_COMPONENTS$", spellComponents)
    file.findAndReplace("$SPELL_DURATION$", spellDuration)
    file.findAndReplace("$SPELL_CLASSES$", spellClasses)
    file.findAndReplace("$SPELL_DESCRIPTION$", spellDescription)
    file.findAndReplace("$SPELL_AT_HIGHER_LEVELS$", spellAtHigherLevels)

    return file


def addSpellMetaData(metaData: dict, spell: dict) -> dict:
    spellEntry = {}
    spellEntry["Name"] = spell["Name"]
    spellEntry["Level"] = spellLevelInt(spell)
    spellEntry["School"] = spell["School"]
    spellEntry["Source"] = spell["Source"]
    spellEntry["Classes"] = spell["Classes"]
    metaData[spell["Name"]] = spellEntry
    return metaData


def spellLevelInt(spell: dict) -> int:
    spellLevel = spell["Level"]
    if spellLevel == "Cantrip":
        return "Cantrip"
    return int(spellLevel[0])


if __name__ == "__main__":
    cleanOld()
    metaData = {}
    spells = readCSV("spells.csv")
    for spell in spells:
        spellFile = writeSpell(spell, AFU.FileIO("template/spellTemplate.tex", readIt=True))

        fileName = spell['Name'].replace(" ", "_")
        fileName = fileName.replace("/", "_")
        spellFile.path = f"spells/{spellLevelInt(spell)}/{fileName}.tex"
        spellFile.writeFile()
        addSpellMetaData(metaData, spell)

    # Write meta data on JSON
    FP = open("spells/metaData.json", "w")
    FP.write(json.dumps(metaData))
    FP.close()
    print("Done!")
