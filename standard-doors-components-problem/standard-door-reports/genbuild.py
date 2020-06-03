#!/usr/bin/env python3

from pathlib import Path

root = Path('/')
databases = sorted(root.glob('data/ssd?/door-*.mdb'))

wanted_reports = [
    ('${gadget} diode 3-split', '${gadget}-split.txt'),
    ('${gadget}-r diode 3-split', '${gadget}r-split.txt'),
    ('${gadget}-s diode 3-split', '${gadget}s-split.txt'),
    ('${gadget} diode', '${gadget}.txt'),
    ('${gadget}-r diode', '${gadget}r.txt'),
    ('${gadget}-s diode', '${gadget}s.txt'),
]

command_template = 'toggles-report.exe --db-path $database --threads 64 --skip-mirror {sources} | tee {output}'
ninja_commands = [command_template.format(sources=sources, output=output) for sources, output in wanted_reports]
print('rule report')
print('  command =', ' && '.join(ninja_commands))
print('  pool = console') # also has serializing effect

for d in databases:
    g = d.name[:-4]
    all_outputs = [output.replace("${gadget}", g) for _, output in wanted_reports]
    print('build', ' '.join(all_outputs), ': report', str(d / 'data.mdb'))
    print('  gadget =', g)
    print('  database =', d)
