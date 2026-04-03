import sys
import os

from ZADANIE2.zadanie2 import process_tram_data


def test_return_values():
    """Test czy funkcja zwraca poprawne wartości"""
    stats, unique_stops = process_tram_data('linie_tramwajowe.json')

    # Sprawdź czy zwrócone typy są poprawne
    assert isinstance(stats, dict), "Pierwszy element powinien być słownikiem"
    assert isinstance(unique_stops, int), "Drugi element powinien być liczbą całkowitą"

    # Sprawdź liczby
    assert len(stats) == 17, f"Oczekiwano 17 linii, otrzymano {len(stats)}"
    assert unique_stops == 154, f"Oczekiwano 154 unikalnych przystanków, otrzymano {unique_stops}"


def test_specific_line_counts():
    """Test czy konkretne linie mają poprawną liczbę przystanków"""
    stats, _ = process_tram_data('linie_tramwajowe.json')

    expected_counts = {
        1: 28,
        10: 36,
        11: 18,
        50: 36
    }

    for line_num, expected_count in expected_counts.items():
        assert line_num in stats, f"Linia {line_num} powinna być w statystykach"
        assert stats[line_num] == expected_count, \
            f"Linia {line_num}: oczekiwano {expected_count} przystanków, otrzymano {stats[line_num]}"


def test_output_format(capsys):
    """Test czy format wydruku jest poprawny"""
    process_tram_data('linie_tramwajowe.json')
    captured = capsys.readouterr()

    # Sprawdź czy format jest poprawny
    assert "linia 1: 28" in captured.out
    assert "linia 10: 36" in captured.out
    assert "linia 11: 18" in captured.out

    # Sprawdź czy jest posortowane malejąco (10 przed 1, bo 36 > 28)
    lines = captured.out.strip().split('\n')
    tram_lines = [line for line in lines if line.startswith('linia')]

    stop_counts = []
    for line in tram_lines:
        parts = line.split(': ')
        if len(parts) == 2:
            stop_counts.append(int(parts[1]))

    assert stop_counts == sorted(stop_counts, reverse=True), \
        "Linie powinny być posortowane malejąco po liczbie przystanków"

