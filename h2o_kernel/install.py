import argparse
import json
import os
import sys

from jupyter_client.kernelspec import KernelSpecManager
from IPython.utils.tempdir import TemporaryDirectory

kernel_json = {
    "argv": [sys.executable, "-m", "h2o_kernel", "-f", "{connection_file}"],
    "display_name": "H2O",
    "language": "python",
}


def install_h2o_kernel_spec(user=True, prefix=None):
    with TemporaryDirectory() as td:
        os.chmod(td, 0o755) # Starts off as 700, not user readable
        with open(os.path.join(td, 'kernel.json'), 'w') as f:
            json.dump(kernel_json, f, sort_keys=True)
        print('Installing H2O kernel Jupyter kernel spec')
        KernelSpecManager().install_kernel_spec(td, 'h2o', user=user, replace=True, prefix=prefix)

def _is_root():
    try:
        return os.geteuid() == 0
    except AttributeError:
        return False # assume not an admin on non-Unix platforms

def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument('--user', action='store_true',
        help="Install H2O kernel to the per-user kernels registry. Default if not root.")
    ap.add_argument('--sys-prefix', action='store_true',
        help="Install H2O kernel to sys.prefix (e.g. a virtualenv or conda env)")
    ap.add_argument('--prefix',
        help="Install H2O kernel to the given prefix. "
             "Kernelspec will be installed in {PREFIX}/share/jupyter/kernels/")
    args = ap.parse_args(argv)

    if args.sys_prefix:
        args.prefix = sys.prefix
    if not args.prefix and not _is_root():
        args.user = True

    install_h2o_kernel_spec(user=args.user, prefix=args.prefix)


if __name__ == '__main__':
    main()
