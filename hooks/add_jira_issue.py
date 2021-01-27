import sys
import re
from subprocess import check_output


def main(argv):
    branch = check_output(['git', 'symbolic-ref', '--short', 'HEAD']).strip()
    m = re.match(r'feature/(?P<issue>HDS-\d+)', branch)
    if not m:
        return 0

    issue = m.groupdict()['issue']
    with open(argv[0], 'rw') as f:
        commit_message = f.read()
        if not commit_message.startswith(issue):
            f.seek(0)
            f.write(issue + " " + commit_message.strip())
            f.truncate()
    return 0


if __name__ == '__main__':
    exit(main(sys.argv))
