# maths
Maths stuff for university

primzahlen.py mit funktionen fuer primzahlen etc., kann und soll als cli anwendung verwendet werden
VORSICHT: primzahlen.py benoetigt fuer das berechnen des modular inversen die python library "sympy", die vorher (ueblicherweise per pip) installiert werden muss.
Standartbefehl, um sympy unter Windows 10 fuer python per pip zu installieren: python -m pip install sympy
Usage: primzahlen.py -h
um die funktionen anzeigen zu lassen, dann
Usage: primzahlen.py [NAME DER FUNKTION] [PARAMETER]

1000000.txt
Beinhaltet alle durch primzahlen.py innerhalb von 2h generierten Primfaktorzerlegungen aller Zahlen bis 1000000.
Diese sind wie in primzahlen.py im Format [Zahl_Selbst, Primfaktor_1, Primfaktor_2, ...] angegeben

relations.py ist fuer relationen, testet diese auf eigenschaften und gibt aus, ob eine relation auf einer menge eine aequivalenzrelation oder ordnungsrelation ist
