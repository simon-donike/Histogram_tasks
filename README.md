# Understanding BIL and Histograms in Python

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/simon-donike/bil_histogram/master)

## Aufgabe

In this repository, you will find 3 jupyter notebooks, which use Python to complete
the exercises.

**01_BIL_to_Histogram:**
This notebook shows how BIL data is read and transformed to a histogram. All the 
necessary steps are to complete the task are annotated.

**02_Lincoln_hist_corrleation***
This notebook reads the Lincoln image and prints the table of values as well as
a rendered image.

**03_image_vs_random_histogr_comparison:**
This notebook loads a numeric pixel value image, as well as a same-size randomly
generated image. In order to show that histograms can show that an image is "realistic",
histograms for both images are created and compared.

**Click on Button to launch notepads in MyBinder:**
   
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/simon-donike/bil_histogram/master)

Launching Binder after new commit might take a while, since the docker needs to be rebuilt by MyBinder

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
