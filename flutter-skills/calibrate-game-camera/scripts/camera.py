"""Orthographic, zero-roll camera calibration. Python standard library only.

Input JSON: x_edges/y_edges/z_edges: lists of [[u0,v0],[u1,v1]].
X/Y must be horizontal, mutually perpendicular WORLD axes (not roof slopes).
At least two edges per family. Pixel coordinates have v downward.
"""
import argparse
import json
import math
import statistics


def project(p, azimuth, elevation, scale=1, origin=(0, 0)):
    a, e = map(math.radians, (azimuth, elevation))
    x, y, z = p
    return (origin[0] + scale * (-math.sin(a)*x + math.cos(a)*y),
            origin[1] + scale * (math.sin(e)*(math.cos(a)*x + math.sin(a)*y)-math.cos(e)*z))


def angle_delta(a, b):
    return abs((a-b+90) % 180-90)


def family(edges, vertical=False, min_length=12):
    if len(edges) < 2:
        raise ValueError('Need at least two separate structural edges per axis family')
    angles, slopes = [], []
    for start, end in edges:
        dx, dy = end[0]-start[0], end[1]-start[1]
        if math.hypot(dx, dy) < min_length:
            raise ValueError('Edge too short for reliable calibration')
        angles.append(math.degrees(math.atan2(dy, dx)) % 180)
        if not vertical:
            if abs(dx) < 1e-6:
                raise ValueError('Near-vertical floor axis: calibration ill-conditioned; use another view')
            slopes.append(dy/dx)
    # Circular mean of unoriented lines, not median across the 0/180 seam.
    mean = math.degrees(math.atan2(sum(math.sin(math.radians(2*a)) for a in angles),
                                   sum(math.cos(math.radians(2*a)) for a in angles)))/2 % 180
    return {'angle_deg': mean,
            'max_deviation_deg': max(angle_delta(a, mean) for a in angles),
            'slope': None if vertical else statistics.median(slopes),
            'count': len(edges)}


def calibrate(data, tolerance=2):
    groups = {key: family(data[key+'_edges'], key == 'z') for key in ('x', 'y', 'z')}
    failures = []
    for key, value in groups.items():
        if value['max_deviation_deg'] > tolerance:
            failures.append(key+': nonparallel family; perspective or inconsistent drawing')
    if angle_delta(groups['z']['angle_deg'], 90) > tolerance:
        failures.append('Verticals show roll, shear, perspective or inconsistent drawing')
    mx, my = groups['x']['slope'], groups['y']['slope']
    k = -mx*my
    if mx >= 0 or my <= 0 or not 0 < k < 1:
        failures.append('Unsupported axes: require X negative slope, Y positive slope, 0 < -mx*my < 1')
    result = {'status': 'reject' if failures else 'candidate', 'families': groups,
              'tolerance_deg': tolerance, 'failures': failures,
              'limitations': ['Orthographic hypothesis only; weak perspective can look identical',
                             'Azimuth relative to annotated axes, canonical first-quadrant solution',
                             'No world scale, hidden structure or handedness inferred from lines']}
    if not failures:
        result.update(azimuth_deg=math.degrees(math.atan(math.sqrt(-my/mx))),
                      elevation_deg=math.degrees(math.asin(math.sqrt(k))))
        if 'scale_reference' in data:
            ref = data['scale_reference']
            length = float(ref['world_length'])
            if length <= 0:
                raise ValueError('world_length must be positive')
            # Reference must be a true vertical of known world length.
            pix = math.dist(*ref['edge'])
            result['pixels_per_world_unit'] = pix/(length*math.cos(math.radians(result['elevation_deg'])))
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input')
    parser.add_argument('--out', required=True)
    parser.add_argument('--tolerance', type=float, default=2)
    parser.add_argument('--overlay', help='Optional reference PNG; Pillow required only for overlay')
    args = parser.parse_args()
    if not 0 < args.tolerance <= 10:
        parser.error('tolerance must be in (0,10] degrees')
    try:
        data = json.load(open(args.input))
        result = calibrate(data, args.tolerance)
        if args.overlay:
            from PIL import Image, ImageDraw
            img = Image.open(args.overlay).convert('RGBA')
            draw = ImageDraw.Draw(img)
            for key, color in (('x','red'),('y','lime'),('z','cyan')):
                for i, edge in enumerate(data[key+'_edges']):
                    draw.line([tuple(p) for p in edge],fill=color,width=3)
                    draw.text(tuple(edge[0]),key+str(i),fill=color,stroke_width=1,stroke_fill='black')
            img.save(args.out+'.overlay.png')
    except (ValueError, KeyError, TypeError) as error:
        result = {'status': 'reject', 'failures': [str(error)]}
    with open(args.out, 'w') as handle:
        json.dump(result, handle, indent=2)
    print(json.dumps(result, indent=2))
    return int(result['status'] == 'reject')


if __name__ == '__main__':
    raise SystemExit(main())
