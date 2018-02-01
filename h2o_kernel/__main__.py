from ipykernel.kernelapp import IPKernelApp
from . import H2OKernel

IPKernelApp.launch_instance(kernel_class=H2OKernel)