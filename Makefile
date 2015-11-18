 all: V203.pdf

plot.pdf: plot.py V203Daten1.txt
	python plot.py

plot2.pdf: plot2.py V203Daten2.txt
	python plot2.py

plot3.pdf: plot3.py
	python plot3.py

V203.pdf: plot.pdf plot2.pdf plot3.pdf V203.tex header.tex auswertung.tex theorie.tex durchfuehrung.tex lit.bib
	lualatex V203.tex
	biber V203.bcf
	lualatex V203.tex
