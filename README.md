# bil_histogram
Worksheet for Histogram, BIL and correlation tests.

##Executable and manipulatable Jupyter Notpads hosted on MyBinder:
https://notebooks.gesis.org/binder/jupyter/user/simon-donike-bil_histogram-62j7qpeb/tree



Aufgabe:
Hi Simon
 
Nochmal zur Histogramm Übung (entsprechende Excel und Lösung anbei).
Das Lernziel ist zu verstehen, wie ein string von Zahlen im BIL format gelesen wird, beispielhaft für ein 2-Kanal Bild.
Zunächst [Teil 1, Blatt 1] soll der Zahlenstring in zwei Bildmatrizen der beiden Kanäle (A und B) übergeführt
werden (Blatt 2) und zwar einmal numerisch (oben) und dann visualisiert in 5 Grauwertstufen (unten).
Sodann wird für jeweils eine Reihe (Zeile 3) ein Intensitätsdiagramm erstellt, sowie für die ganze
Matrix jeweils ein Histogramm.
 
Zusätzlich sollen die Studierenden noch für einen kleinen Ausschnitt einer Bildmatrix (ImageMtrx.jpg)
begründen ob diese realistisch ist oder nicht. Die Antwort ist JA, weil sich die Werte in einem gewissen
Wertebereich (8-bit) bewegen und die jeweils benachbarten Pixelwerte ähnlich sind (spatial auto-correlation).
Daraus ließe sich dann mit deinem bestehenden notebook ein Histogramm erstellen, sowie ggf. für einen weiteren
etwas größeren Ausschnitt. Damit soll klar werden dass ein Histogramm die Werteverteilung rasch vermittelt
(auf Histogramme wird gesondert eingegangen).
 
Zusätzlich ließen sich für die Matrix auch Korrelationskoeffizienten für die räumliche Autokorrelation berechnen
(Moran’s I od. Geary’s C, die Formeln wären in der angehängten Excel Link_seg zu finden). Dann könnte man das
ganze mit einer random Matrix  mit denselben Werten vergleichen (selbes Histogramm aber andere Autocorrelation).
 
Es muss natürlich nicht alles sofort sein, insb die Sache mit der Autocorrelation kann man auch erstmal weglassen.
 
Damit einen schönen Abend !
