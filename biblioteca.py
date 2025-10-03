import csv

def carica_da_file(file_path):
    """Carica i libri dal file"""

    with open(file_path, "r", encoding="utf-8") as file:
        num_sezione = int(file.readline().strip())
        biblioteca = [[] for _ in range(num_sezione)]
        max_sezione = 0

        reader = csv.reader(file)
        for row in reader:
            if len(row) < 5:
                continue
            titolo = row[0].strip()
            autore = row[1].strip()
            anno = int(row[2].strip())
            pagine = int(row[3].strip())
            sezione = int(row[4].strip())

            if sezione > max_sezione:
                max_sezione = sezione
        if max_sezione >= num_sezione:
            num_sezione = max_sezione + 1

            if 0 <= sezione < num_sezione:
                biblioteca[sezione].append([titolo, autore, anno, pagine, sezione])
            else:
                print(f"Attenzione: sezione {sezione} fuori intervallo per il libro '{titolo}'")

    return biblioteca


def aggiungi_libro(biblioteca, titolo, autore, anno, pagine, sezione, file_path):
    """Aggiunge un libro nella biblioteca"""
    if sezione < 0 or sezione >= len(biblioteca):
        print("Sezione non valida")
        return None

    libro = [titolo.strip(), autore.strip(), anno, pagine, sezione]

    if libro not in biblioteca[sezione]:
        biblioteca[sezione].append(libro)
        with open(file_path, "a", encoding="utf-8", newline = "") as file:
            writer = csv.writer(file)
            writer.writerow(libro)
        return  True
    elif libro in biblioteca[sezione]:
        return False


def cerca_libro(biblioteca, titolo):
    """Cerca un libro nella biblioteca dato il titolo"""
    risultato = []

    for sezione in biblioteca:
        for libro in sezione:
            if libro[0].lower() == titolo.lower():
                risultato.append(libro)

    return risultato


def elenco_libri_sezione_per_titolo(biblioteca, sezione):
    """Ordina i titoli di una data sezione della biblioteca in ordine alfabetico"""

    if 0 <= sezione < len(biblioteca):
        titoli = sorted([libro[0] for libro in biblioteca[sezione]])
        return titoli
    else:
        print("Sezione non valida")
        return None


def main():
    biblioteca = []
    file_path = "biblioteca.csv"

    while True:
        print("\n--- MENU BIBLIOTECA ---")
        print("1. Carica biblioteca da file")
        print("2. Aggiungi un nuovo libro")
        print("3. Cerca un libro per titolo")
        print("4. Ordina titoli di una sezione")
        print("5. Esci")

        scelta = input("Scegli un'opzione >> ").strip()

        if scelta == "1":
            while True:
                file_path = input("Inserisci il path del file da caricare: ").strip()
                biblioteca = carica_da_file(file_path)
                if biblioteca is not None:
                    break

        elif scelta == "2":
            if not biblioteca:
                print("Prima carica la biblioteca da file.")
                continue

            titolo = input("Titolo del libro: ").strip()
            autore = input("Autore: ").strip()
            try:
                anno = int(input("Anno di pubblicazione: ").strip())
                pagine = int(input("Numero di pagine: ").strip())
                sezione = int(input("Sezione: ").strip())
            except ValueError:
                print("Errore: inserire valori numerici validi per anno, pagine e sezione.")
                continue

            libro = aggiungi_libro(biblioteca, titolo, autore, anno, pagine, sezione, file_path)
            if libro:
                print(f"Libro aggiunto con successo!")
            else:
                print("Non è stato possibile aggiungere il libro.")

        elif scelta == "3":
            if not biblioteca:
                print("La biblioteca è vuota.")
                continue

            titolo = input("Inserisci il titolo del libro da cercare: ").strip()
            risultato = cerca_libro(biblioteca, titolo)
            if risultato:
                print(f"Libro trovato: {risultato}")
            else:
                print("Libro non trovato.")

        elif scelta == "4":
            if not biblioteca:
                print("La biblioteca è vuota.")
                continue

            try:
                sezione = int(input("Inserisci numero della sezione da ordinare: ").strip())
            except ValueError:
                print("Errore: inserire un valore numerico valido.")
                continue

            titoli = elenco_libri_sezione_per_titolo(biblioteca, sezione)
            if titoli is not None:
                print(f'\nSezione {sezione} ordinata:')
                print("\n".join([f"- {titolo}" for titolo in titoli]))

        elif scelta == "5":
            print("Uscita dal programma...")
            break
        else:
            print("Opzione non valida. Riprova.")


if __name__ == "__main__":
    main()


