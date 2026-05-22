# Spielbaumsuche im Vergleich: Minimax vs. Alpha-Beta-Pruning

*Hinweis: Dieses Projekt wurde für das Proseminar Fortgeschrittene Programmierkonzepte: Basic AI in Game Theory entwickelt und mit Unterstützung von KI-Assistenzsystemen optimiert.*

Dieses Projekt bietet eine Python-basierte Benchmark-Umgebung, um die Effizienz und Funktionsweise des klassischen Minimax-Algorithmus mit der optimierten Alpha-Beta-Suche zu vergleichen.

## Features
* **Dynamische Baumgenerierung:** Erzeugt Spielbäume basierend auf frei wählbarem Verzweigungsfaktor (Branching-Faktor) und maximaler Suchtiefe.
* **Messwerte & Performance:** Präzise Messung der Rechenzeit (in Mikrosekunden), der Anzahl besuchter Knoten sowie der durchgeführten Cutoffs.
* **Effizienz-Analyse:** Automatische Auswertung des prozentualen Performance-Gewinns durch Alpha-Beta-Pruning.

## Voraussetzungen
* Python 3.x
* Es werden keine externen Bibliotheken benötigt (reine Standard-Bibliotheken: `random`, `time`, `sys`).

## Verwendung
Das Skript kann direkt über das Terminal gestartet werden. Nach dem Start können der gewünschte Branching-Faktor und die Suchtiefe interaktiv eingegeben werden:

```bash
python benchmark.py
