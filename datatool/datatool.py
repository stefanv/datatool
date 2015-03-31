import os
import json
import errno
import jsonpath_rw as jsonpath


HOME = os.path.expanduser('~')
CONFIG = os.path.join(HOME, '.config/datatool')
PATH_STORE = os.path.join(CONFIG, 'paths.txt')


def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc: # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else: raise


mkdir_p(CONFIG)

if not os.path.exists(PATH_STORE):
    with open(PATH_STORE, 'w') as f:
        f.write('\n')


def add(path):
    path = os.path.abspath(path)
    paths = get_paths()
    if os.path.isdir(path):
        paths.append(path)
        with open(PATH_STORE, 'w') as f:
            f.writelines(set(paths))
    else:
        print("Error: {0} is not a valid directory".format(dir))


def get_paths():
    with open(PATH_STORE, 'r') as f:
        paths = [l.strip() for l in f.readlines() if l.strip()]

    return paths


def get_packages():
    package_candidates = []
    for p in get_paths():
        package_candidates.extend(
            (d, os.path.join(p, d)) for d in os.listdir(p) if os.path.isdir(p))

    loadable_packages = []
    for (pkg_name, pkg_path) in package_candidates:
        datapackage = os.path.join(pkg_path, 'datapackage.json')
        if os.path.exists(datapackage):
            try:
                data = json.load(open(datapackage, 'r'))
                loadable_packages.append((pkg_path, data))
            except (FileNotFoundError, ValueError, KeyError) as e:
                print("Warning: invalid datapackage.json in {0}".format(p))
                print("  ->", e)

    return loadable_packages


def fetch(package, group=None):
    print("fetching {0}".format(package))
    if group:
        print("group {0}".format(group))


def status(package=None):
    print("Package paths:")
    for p in get_paths():
        print(" -", p)
    print()

    packages = get_packages()
    print("Found {0} package(s):".format(len(packages)))
    print()

    for (path, data) in packages:
        expr = jsonpath.parse('$..file')
        files = [match.value for match in expr.find(data)]

        print("{0} : {1} [{2} files]".format(os.path.basename(path),
                                           data['name'], len(files)))
