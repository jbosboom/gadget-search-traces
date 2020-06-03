#!/bin/bash

databases=(/data/ssd?/door-*.mdb)
for d in ${databases[@]}; do
  g=${d:11}
  g=${g%%.mdb}
  toggles-report.exe --db-path /data/ssd?/$g.mdb --threads 64 --skip-mirror $g diode 3-split | tee $g-split.txt
  toggles-report.exe --db-path /data/ssd?/$g.mdb --threads 64 --skip-mirror ${g}-r diode 3-split | tee ${g}r-split.txt
  toggles-report.exe --db-path /data/ssd?/$g.mdb --threads 64 --skip-mirror ${g}-s diode 3-split | tee ${g}s-split.txt
  toggles-report.exe --db-path /data/ssd?/$g.mdb --threads 64 --skip-mirror $g diode | tee $g.txt
  toggles-report.exe --db-path /data/ssd?/$g.mdb --threads 64 --skip-mirror ${g}-r diode | tee ${g}r.txt
  toggles-report.exe --db-path /data/ssd?/$g.mdb --threads 64 --skip-mirror ${g}-s diode | tee ${g}s.txt
done
