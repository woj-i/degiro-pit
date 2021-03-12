# Degiro - PIT

Celem tej aplikacji jest pobranie kursów EUR potrzebnych do obliczenia podatku giełdowego w Polsce. Aplikacja na licencji MIT, autor nie ponosi odpowiedzialności za poprawność działania programu.

## Instalacja z kodu źródłowego
Pobierz kod aplikacji

    git clone https://github.com/woj-i/degiro-pit.git

Otwórz terminal w katalogu projektu (tam gdzie README.md). Uruchom:

    python3.8 -m venv venv

Dla Windows:

    venv\Scripts\activate.bat

Dla Linux / MacOS:

    source venv/bin/activate

Uruchom:

    pip install -r requirements.txt


## Przygotowanie danych

Pobierz raport z transakcji DeGiro w formie plików csv. Umieść dane w katalogu data pod nazwą Transactions.csv (domyślna nazwa przy eksporcie z DeGiro).

Przykładowy plik z danymi znajdziesz w katalogu `examples/input`.

## Uruchomienie programu

    cd degiro_pit
    python enricher.py --date_column_name Datum --currency EUR

To komenda dla niemieckiej wersji DeGiro. Jeśli kolumna daty w Twoim pliku CSV nazywa się inaczej to zmień `Datum` na swoją nazwę. 
Możesz także wybrać inną walutę. Obecnie są wspierane EUR i USD. 
## Wyniki

Wyniki znajdują  się w katalogu `data` pod nazwą `output.csv`. 
Wyniki należy otworzyć używanym przez Ciebie arkuszem kalkulacyknym (np. LibreOffice Calc).

Dysponując kolumną z kursem waluty z dnia poprzedniego od transakcji (`eur_pln_day_before`) łatwo stworzyć kolumnę z wyliczoną wartością w złotówkach.
Do rocznego podsumowania należy pamiętać o usunięciu linii transakcji kupna, które nie zostały zamknięte.

# Rozwój aplikacji

Wszelkie uwagi i propozycje ulepszeń są mile widziane. Proszę używać do tego zakładki "issues" w GitHubie.