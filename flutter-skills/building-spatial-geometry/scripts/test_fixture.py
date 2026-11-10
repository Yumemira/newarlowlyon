"""Execute baseline and six intentional defects in separate Blender processes."""
import argparse
import json
from pathlib import Path
import subprocess


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--blender',required=True)
    parser.add_argument('--out',required=True)
    args = parser.parse_args()
    root = Path(__file__).resolve().parent.parent
    out = Path(args.out).resolve()
    out.mkdir(parents=True,exist_ok=True)
    results = []
    for fault, expected in [(None,None),('floating-roof','eave does not meet'),
                            ('floating-post','not grounded'),('missing-roof','missing'),
                            ('clipped','frame margin'),('squashed','non-rigid deformation'),
                            ('swapped-annex','parts changed relative')]:
        target = out/(fault or 'baseline')
        target.mkdir(exist_ok=True)
        reportfile = target/'report.json'
        if reportfile.exists():
            reportfile.unlink()  # Do not accept a stale report from a crashed run.
        cmd = [args.blender,'-b','--factory-startup','--python-exit-code','1','--python',
               str(root/'scripts/build_fixture.py'),'--','--config',str(root/'assets/house.json'),'--out',str(target)]
        if fault:
            cmd.extend(['--audit-only','--fault',fault])
        run = subprocess.run(cmd,capture_output=True,text=True,timeout=60)
        (target/'run.log').write_text(run.stdout+run.stderr)
        report = json.loads(reportfile.read_text())
        if fault:
            assert run.returncode != 0 and report['status']=='fail',fault
            assert any(expected in e for v in report['views'] for e in v['errors']),fault
        else:
            assert run.returncode == 0 and report['status']=='pass',run.stdout+run.stderr
            assert len({v['mesh_sha256'] for v in report['views']}) == 1
            assert all(v['visible_pixels']>1000 and v['transparent_pixels']>1000 for v in report['views'])
            assert all(v['projection_max_error_normalized'] < 1e-6 for v in report['views'])
        results.append({'case':fault or 'baseline','expected_failure_detected':bool(fault),
                        'status':report['status'],'exit_code':run.returncode})
        print(results[-1],flush=True)
    (out/'test-summary.json').write_text(json.dumps(results,indent=2))


if __name__ == '__main__':
    main()
