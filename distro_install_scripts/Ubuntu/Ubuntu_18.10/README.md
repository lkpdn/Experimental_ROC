## Scripts for Installing ROCm on Ubuntu 18.10

This directory contains directions and scripts for installing ROCm on Ubuntu 18.10.
There are two options for installing and building ROCm available in this toolkit.

- [./deb_install](deb_install) will install ROCm from the AMD binary packages downloaded from AMD's `apt` repository
- [./src_install](src_install) will download, build, and install ROCm from source code downloaded from AMD's ROCm GitHub repositories
    - These scripts can also be used to build custom versions of any one of the ROCm software packages after installing the rest of the ROCm software system from binary packages.
    - These scripts can also be used to build binary packages of any of the ROCm software.

Note that both of these installation mechanisms will, by default, attempt to update system-wide software (such as your kernel) in order to allow ROCm to successfully install.
You will need sudo access in order to complete those steps.
The source code installation method can optionally install all of the user-space components into local folders and thus avoid the need for sudo or root access.

### ROCm on Ubuntu 18.10 is Experimental
Please note that Ubuntu 18.10 is not a ROCm platform that AMD officially supports or tests against at this time.
As such, tools that target this distribution should be considered experimental.
Bug reports and pull requests for Ubuntu 18.10 are welcome, but AMD does not guarantee any level of support for this setup.
