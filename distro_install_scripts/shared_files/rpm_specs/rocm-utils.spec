# rpmrebuild autogenerated specfile

%define defaultbuildroot /
AutoProv: no
%undefine __find_provides
AutoReq: no
%undefine __find_requires
# Do not try autogenerate prereq/conflicts/obsoletes and check files
%undefine __check_files
%undefine __find_prereq
%undefine __find_conflicts
%undefine __find_obsoletes
# Be sure buildpolicy set to do nothing
%define __spec_install_post %{nil}
# Something that need for rpm-4.1
%define _missing_doc_files_terminate_build 0
#dummy
#dummy

#OS:           linux
#SIZE:           7
#ARCHIVESIZE:           528
#ARCH:         x86_64
BuildArch:     x86_64
Name:          rocm-utils
Version:       ROCM_PKG_VERSION
Release:       1
License:       unknown
Group:         unknown
Summary:       Utilities for the Radeon Open Compute (ROCm) software stack

Source: %{expand:%%(pwd)}
BuildRoot: %{expand:%%(pwd)}

Vendor:        AMD






Prefix:        ROCM_OUTPUT_DIR
Provides:      rocm-utils = ROCM_PKG_VERSION-1
Provides:      rocm-utils(x86-64) = ROCM_PKG_VERSION-1
Requires:      /bin/sh
Requires:      /bin/sh
Requires:      /bin/sh
Requires:      /bin/sh
Requires:      rocm-clang-ocl
Requires:      rocminfo
#Requires:      rpmlib(CompressedFileNames) <= 3.0.4-1
#Requires:      rpmlib(FileDigests) <= 4.6.0-1
#Requires:      rpmlib(PayloadFilesHavePrefix) <= 4.0-1
#Requires:      rpmlib(PayloadIsXz) <= 5.2-1
#suggest
#enhance
%description
DESCRIPTION
===========

%prep
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
cd $RPM_BUILD_ROOT
cp -R %{SOURCEURL0}/* .

%clean
rm -r -f "$RPM_BUILD_ROOT"

%files
%dir %attr(0755, root, root) "ROCM_OUTPUT_DIR"
%dir %attr(0755, root, root) "ROCM_OUTPUT_DIR/.info"
%attr(0644, root, root) "ROCM_OUTPUT_DIR/.info/version-utils"
%pre -p /bin/sh
%post -p /bin/sh
%preun -p /bin/sh
%postun -p /bin/sh
%changelog
* Sun Jul 04 2010 Eric Noulard <eric.noulard@gmail.com> - ROCM_PKG_VERSION-1
Generated by CPack RPM (no Changelog file were provided)