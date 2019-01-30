# Uses python3

from itertools import chain
import sys


def touches(point, segment):
    start, end = segment
    return (start <= point) and (point <= end)


def optimal_points(segments):
    points = []
    segments = sorted(segments)
    while segments:
        print("segments:", segments, file=sys.stderr)
        _, maximun = segments.pop(0)
        print("maximun:", maximun, file=sys.stderr)
        while segments and segments[0][0] <= maximun:
            _, right = segments.pop(0)
            maximun = min(maximun, right)
        points.append(maximun)
    return points


def stdin():
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = ((start, end) for start, end in zip(data[::2], data[1::2]))
    points = optimal_points(segments)
    print(len(points))
    for point in points:
        print(point, end=" ")


def equal_enough(left, right):
    return abs(left - right) < 0.0001


def test(case, expected):
    print("\nTest:", file=sys.stderr)
    obtained = optimal_points(case)
    for pos, (start, end) in enumerate(case, 1):
        for point in obtained:
            if (start <= point) and (point <= end):
                break
        else:
            raise ValueError("for case:\n%s,\ngot:\n%s\n, not covering #%d: %s" % (case,
                obtained, pos, (start, end)))
    if len(expected) != len(obtained):
        raise ValueError("for case:\n%s,\nresult:\n%s was expected, got:\n%s" % (case,
            len(expected), len(obtained)))



def tests():
    cases = {
                ((1, 3), (2, 5), (3, 6)): (3,),
                ((4, 7), (1, 3), (2, 5), (5, 6)): (3, 6),
                (('41', '42'), ('52', '52'), ('63', '63'), ('80', '82'),
                ('78', '79'), ('35', '35'), ('22', '23'), ('31', '32'),
                ('44', '45'), ('81', '82'), ('36', '38'), ('10', '12'), ('1',
                '1'), ('23', '23'), ('32', '33'), ('87', '88'), ('55', '56'),
                ('69', '71'), ('89', '91'), ('93', '93'), ('38', '40'),
                ('33', '34'), ('14', '16'), ('57', '59'), ('70', '72'),
                ('36', '36'), ('29', '29'), ('73', '74'), ('66', '68'),
                ('36', '38'), ('1', '3'), ('49', '50'), ('68', '70'), ('26',
                '28'), ('30', '30'), ('1', '2'), ('64', '65'), ('57', '58'),
                ('58', '58'), ('51', '53'), ('41', '41'), ('17', '18'),
                ('45', '46'), ('4', '4'), ('0', '1'), ('65', '67'), ('92',
                '93'), ('84', '85'), ('75', '77'), ('39', '41'), ('15',
                '15'), ('29', '31'), ('83', '84'), ('12', '14'), ('91',
                '93'), ('83', '84'), ('81', '81'), ('3', '4'), ('66', '67'),
                ('8', '8'), ('17', '19'), ('86', '87'), ('44', '44'), ('34',
                '34'), ('74', '74'), ('94', '95'), ('79', '81'), ('29',
                '29'), ('60', '61'), ('58', '59'), ('62', '62'), ('54',
                '56'), ('58', '58'), ('79', '79'), ('89', '91'), ('40',
                '42'), ('2', '4'), ('12', '14'), ('5', '5'), ('28', '28'),
                ('35', '36'), ('7', '8'), ('82', '84'), ('49', '51'), ('2',
                '4'), ('57', '59'), ('25', '27'), ('52', '53'), ('48', '49'),
                ('9', '9'), ('10', '10'), ('78', '78'), ('26', '26'), ('83',
                '84'), ('22', '24'), ('86', '87'), ('52', '54'), ('49',
                '51'), ('63', '64'), ('54', '54')): ('1', '4', '5', '8', '9',
                '10', '14', '15', '18', '23', '26', '28', '29', '30', '32',
                '34', '35', '36', '40', '41', '44', '46', '49', '52', '54',
                '56', '58', '61', '62', '63', '65', '67', '70', '74', '77',
                '78', '79', '81', '84', '87', '91'),
            }
    for case, result in cases.items():
        test(case, result)


if __name__ == '__main__':
#     tests()
    stdin()
