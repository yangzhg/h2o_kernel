from ipykernel.ipkernel import IPythonKernel


class H2OKernel(IPythonKernel):
    implementation = 'H2O'
    implementation_version = '1.0.1'
    language = 'python'
    language_version = '3.6'
    language_info = {
        'name': 'python',
        'mimetype': 'text/x-python',
        'file_extension': '.py',
    }
    banner = "H2O kernel"

    def start(self):
        self.shell.run_cell(self.get_init(), store_history=False, silent=True)
        super().start()

    def get_init(self):
        """
        generate init code
        :return:
        """
        init_code = """
import h2o
def reload_h2o():
    from os.path import expanduser
    from os.path import join
    from os.path import exists
    from os import getenv
    try:
        import configparser as ConfigParser  # py3
    except Exception as e:
        import ConfigParser  # py2
    default_conf = '/etc/h2okernelrc'
    user_conf = join(expanduser("~"), '.h2okernelrc')
    config = ConfigParser.ConfigParser()
    conf = dict()
    if exists(default_conf):
        config.read(default_conf)
        conf = dict(config['h2o'])
    if exists(user_conf):
        config.read(user_conf)
        conf.update(config['h2o'])
    if getenv('H2O_IP') is not None:
        conf['ip'] = getenv('H2O_IP')
    if getenv('H2O_PORT') is not None:
        conf['port'] = getenv('H2O_PORT')
    if getenv('H2O_URL') is not None:
        conf['url'] = getenv('H2O_URL')
    h2o.connect(**conf)
    del conf
    del config
    del default_conf
    del user_conf
    del join
    del expanduser
    del exists
    del ConfigParser
reload_h2o()
"""
        return init_code

if __name__ == '__main__':
    from ipykernel.kernelapp import IPKernelApp
    IPKernelApp.launch_instance(kernel_class=H2OKernel)
