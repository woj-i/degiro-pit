# Degiro - PIT

Celem tej aplikacji jest pobranie kursów walut potrzebnych do obliczenia podatku giełdowego w Polsce. 
Aplikacja na licencji MIT, autor nie ponosi odpowiedzialności za poprawność działania programu.

## Wymagania

* [Python 3.8 lub nowszy](https://www.python.org/downloads/)

Dla Windows:

* [Powershell](https://docs.microsoft.com/pl-pl/powershell/scripting/windows-powershell/starting-windows-powershell?view=powershell-7.1), ewentualnie cmd.exe

## Instalacja

Otwórz `Powershell (Windows)`/ `Terminal (Linux)`. Uruchom:

    pip install degiro-pit-woj-i

## Aktualizacja

    pip install --upgrade degiro-pit-woj-i

## Instalacja z kodu źródłowego (alternatywna do pip install)
Pobierz kod aplikacji

    git clone https://github.com/woj-i/degiro-pit.git

Otwórz terminal w katalogu projektu (tam gdzie README.md). Uruchom:

    python -m venv venv

Dla Windows:

    venv\Scripts\activate.bat

Dla Linux / MacOS:

    source venv/bin/activate

Uruchom:

    pip install -r requirements.txt


## Przygotowanie danych

Pobierz raport z transakcji DeGiro w formie plików csv. Zapisz plik w osobnym katalogu (np. Degiro). 
Domyślna nazwa pliku z transakcjami przy eksporcie z DeGiro to `Transactions.csv`.

Przykładowy plik z danymi znajdziesz w katalogu `examples/input`.

## Uruchomienie programu

Otwórz Powershell/Terminal w katalogu gdzie znajdują się  plik z transakcjami. 
Powershell można uruchomić przez `Windows Explorer -> Plik -> Otwórz Windows Powershell`. Uruchom:

    python -m degiro_pit.enricher Transactions.csv --date_column_name Datum --currency EUR

To komenda dla niemieckiej wersji DeGiro. Jeśli kolumna daty w Twoim pliku CSV nazywa się inaczej to zmień `Datum` na swoją nazwę. 
Możesz także wybrać inną walutę. Obecnie są wspierane EUR i USD. 
Jeśli nazwałeś plik inaczej niż  domyślne `Transactions.csv` to użyj nazwy swojego pliku w komendzie powyżej.

## Wyniki

Wyniki znajdują  się w katalogu gdzie została uruchomiona aplikacja. Nazwa pliku wynikowego to `output.csv`. 
Wyniki należy otworzyć używanym przez Ciebie arkuszem kalkulacyknym (np. LibreOffice Calc).

Dysponując kolumną z kursem waluty z dnia poprzedniego od transakcji (`eur_pln_day_before`) łatwo stworzyć kolumnę z wyliczoną wartością w złotówkach.
Do rocznego podsumowania należy pamiętać o usunięciu linii transakcji kupna, które nie zostały zamknięte.

# Rozwój aplikacji

Wszelkie uwagi i propozycje ulepszeń są mile widziane. Proszę używać do tego zakładki "issues" w GitHubie.