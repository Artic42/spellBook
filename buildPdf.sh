# Activate the virtual environment
source .venv/bin/activate

# Generate the spells
python src/generateSpells.py

# Generate the classes tex
python src/generateArtificer.py
python src/generateDruid.py
python src/generateRanger.py
python src/generateCleric.py

mkdir -p build

# Generate the pdf
pdflatex -interaction=nonstopmode -output-directory=build artificer.tex
pdflatex -interaction=nonstopmode -output-directory=build druid.tex
pdflatex -interaction=nonstopmode -output-directory=build Ranger.tex
pdflatex -interaction=nonstopmode -output-directory=build cleric.tex

pdflatex -interaction=nonstopmode -output-directory=build artificer.tex
pdflatex -interaction=nonstopmode -output-directory=build druid.tex
pdflatex -interaction=nonstopmode -output-directory=build Ranger.tex
pdflatex -interaction=nonstopmode -output-directory=build cleric.tex

# Clean up
rm build/*.aux
rm build/*.log
rm build/*.out
rm build/*.toc
