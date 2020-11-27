@echo off
title Kalkulator

:START
cls
echo Jakie dzialanie chcesz wykonac?
echo Dodaj, Odejmij, Pomnoz, Podziel.
set /p licz=
IF '%licz%' == 'Dodaj' GOTO Dodaj
IF '%licz%' == 'Odejmij' GOTO Odejmij
IF '%licz%' == 'Pomnoz' GOTO Pomnoz
IF '%licz%' == 'Podziel' GOTO Podziel
Exit

:Dodaj
Cls
GOTO Dodawanie
pause
exit

:Odejmij
Cls
GOTO Odejmowanie
pause
exit

:Pomnoz
Cls
GOTO Mnozenie
pause
exit

:Podziel
Cls
GOTO Dzielenie
pause
exit

:Dodawanie
echo Podaj pierwsza liczbe
set /p L1=
cls
echo Podaj druga liczbe
set /p L2=
cls

GOTO LiczDod
exit

:Odejmowanie
echo Podaj pierwsza liczbe?
set /p L1=
cls
echo Podaj druga liczbe?
set /p L2=
cls
GOTO LiczOde
exit

:Mnozenie
echo Podaj pierwsza liczbe?
set /p L1=
cls
echo Podaj druga liczbe?
set /p L2=
cls
GOTO LiczMno
exit

:Dzielenie
echo Podaj pierwsza liczbe?
set /p L1=
cls
echo Podaj druga liczbe?
set /p L2=
cls
GOTO LiczDz
exit

:LiczDod
Set /A wynik = %L1% + %L2%
echo Wynik to: %wynik%.
Pause
GOTO START
exit

:LiczOde
Set /A wynik = %L1% - %L2%
echo Wynik to: %wynik%.
pause
GOTO START
exit

:LiczMno
Set /A wynik = %L1% * %L2%
echo Wynik to: %wynik%.
pause
GOTO START
exit

:LiczDz
Set /A wynik = %L1% / %L2%
echo Wynik to: %wynik%.
pause
GOTO START
exit