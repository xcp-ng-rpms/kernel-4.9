%define uname 4.9.0+0
%define short_uname 4.9
%define srcpath /usr/src/kernels/%{uname}-%{_arch}

# Control whether we perform a compat. check against published ABI.
# Default enabled: (to override: --without kabichk)
%define do_kabichk  %{?_without_kabichk: 0} %{?!_without_kabichk: 1}
# Default disabled: (to override: --with kabichk)
#%define do_kabichk  %{?_with_kabichk: 1} %{?!_with_kabichk: 0}

#
# Adjust debuginfo generation to suit building a kernel:
#
# Don't run dwz.
%undefine _find_debuginfo_dwz_opts
# Don't try to generate minidebuginfo.
%undefine _include_minidebuginfo
# Resolve trivial relocations in debug sections.
# This reduces the size of debuginfo.
%define _find_debuginfo_opts -r

Name: kernel-exp
License: GPLv2
Version: 4.9
Release: 144.1
ExclusiveArch: x86_64
ExclusiveOS: Linux
Summary: The Linux kernel
BuildRequires: kmod
BuildRequires: bc
BuildRequires: hostname
%if %{do_kabichk}
BuildRequires: python
%endif
AutoReqProv: no
Provides: kernel-uname-r = %{uname}
Provides: kernel = %{version}-%{release}
Provides: kernel-%{_arch} = %{version}-%{release}
Requires(post): coreutils kmod
Requires(posttrans): coreutils dracut

Source0: %{name}-%{version}.135.tar.gz

# *** kernel.org incremental patches
Patch0: patch-4.9.135-136
Patch1: patch-4.9.136-137
Patch2: patch-4.9.137-138
Patch3: patch-4.9.138-139
Patch4: patch-4.9.139-140
Patch5: patch-4.9.140-141
Patch6: patch-4.9.141-142
Patch7:	patch-4.9.142-143
Patch8: patch-4.9.143-144

# *** XCP-NG patches.
Patch100: abi-version-4.9
Patch101: 4.9-kernel-blktap2-driver.patch

# *** XenServer patches. Unmodified unless stated otherwise.
Patch102: 0001-xen-privcmd-return-ENOTTY-for-unimplemented-IOCTLs.patch
# Patch103 modified to make it apply to newer kernel: removed ARM part.
Patch103: 0001-xen-privcmd-Add-IOCTL_PRIVCMD_DM_OP.patch
Patch104: 0001-xen-privcmd-add-IOCTL_PRIVCMD_RESTRICT.patch
Patch105: restricted-privcmd.patch
Patch106: 0001-libfc-Revisit-kref-handling.patch
Patch107: 0001-scsi-libfc-Fixup-disc_mutex-handling.patch
Patch108: 0001-scsi-libfc-Do-not-take-rdata-rp_mutex-when-processin.patch
Patch109: 0001-scsi-libfc-Do-not-drop-down-to-FLOGI-for-fc_rport_lo.patch
Patch110: 0001-scsi-libfc-Do-not-login-if-the-port-is-already-start.patch
Patch111: 0001-scsi-libfc-don-t-advance-state-machine-for-incoming-.patch
Patch112: 0001-scsi-fcoe-Harden-CVL-handling-when-we-have-not-logge.patch
Patch113: 0001-netfilter-ipset-Null-pointer-exception-in-ipset-list.patch
Patch114: 0085-block-fs-untangle-fs.h-and-blk_types.h.patch
Patch115: 0090-Replace-asm-uaccess.h-with-linux-uaccess.h-globally.patch
Patch116: 0103-sched-headers-Prepare-to-remove-linux-cred.h-inclusi.patch
Patch117: 0168-License-cleanup-add-SPDX-GPL-2.0-license-identifier-.patch
Patch118: 0169-License-cleanup-add-SPDX-license-identifier-to-uapi-.patch
Patch119: 0012-dlm-make-genl_ops-const.patch
Patch120: 0014-dlm-don-t-save-callbacks-after-accept.patch
Patch121: 0015-dlm-remove-lock_sock-to-avoid-scheduling-while-atomi.patch
Patch122: 0016-dlm-don-t-specify-WQ_UNBOUND-for-the-ast-callback-wo.patch
Patch123: 0017-dlm-fix-error-return-code-in-sctp_accept_from_sock.patch
Patch124: 0018-genetlink-no-longer-support-using-static-family-IDs.patch
Patch125: 0021-Replace-asm-uaccess.h-with-linux-uaccess.h-globally.patch
Patch126: 0027-dlm-Fix-kernel-memory-disclosure.patch
Patch127: 0028-dlm-Make-dismatch-error-message-more-clear.patch
Patch128: 0029-dlm-Replace-six-seq_puts-calls-by-seq_putc.patch
Patch129: 0030-dlm-Add-spaces-for-better-code-readability.patch
Patch130: 0031-dlm-Improve-a-size-determination-in-table_seq_start.patch
Patch131: 0032-dlm-Use-kcalloc-in-dlm_scan_waiters.patch
Patch132: 0033-dlm-Improve-a-size-determination-in-dlm_recover_wait.patch
Patch133: 0035-dlm-Use-kmalloc_array-in-make_member_array.patch
Patch134: 0036-dlm-Use-kcalloc-in-two-functions.patch
Patch135: 0037-dlm-Improve-a-size-determination-in-two-functions.patch
Patch136: 0038-dlm-Delete-an-unnecessary-variable-initialisation-in.patch
Patch137: 0039-dlm-print-log-message-when-cluster-name-is-not-set.patch
Patch138: 0040-dlm-constify-kset_uevent_ops-structure.patch
Patch139: 0042-uapi-linux-dlm_netlink.h-include-linux-dlmconstants.patch
Patch140: 0043-dlm-use-sock_create_lite-inside-tcp_accept_from_sock.patch
Patch141: 0044-License-cleanup-add-SPDX-GPL-2.0-license-identifier-.patch
Patch142: 0045-License-cleanup-add-SPDX-license-identifier-to-uapi-.patch
Patch143: 0001-DLM-Eliminate-CF_CONNECT_PENDING-flag.patch
Patch144: 0005-DLM-fix-double-list_del.patch
Patch146: 0008-DLM-retry-rcom-when-dlm_wait_function-is-timed-out.patch
Patch147: 0010-DLM-fix-race-condition-between-dlm_recoverd_stop-and.patch
Patch148: 0013-DLM-fix-conversion-deadlock-when-DLM_LKF_NODLCKWT-fl.patch
Patch149: 0015-DLM-fix-overflow-dlm_cb_seq.patch
Patch150: 0018-DLM-fix-NULL-pointer-dereference-in-send_to_sock.patch
Patch151: 0019-dlm-recheck-kthread_should_stop-before-schedule.patch
Patch152: 0020-dlm-remove-dlm_send_rcom_lookup_dump.patch
Patch153: commit-info.patch
Patch154: 0001-dma-add-dma_get_required_mask_from_max_pfn.patch
Patch155: xen-balloon-hotplug-select-HOLES_IN_ZONE.patch
Patch156: xen-balloon-Only-mark-a-page-as-managed-when-it-is-r.patch
Patch157: 0001-pci-export-pci_probe_reset_function.patch
Patch158: 0002-xen-pciback-provide-a-reset-sysfs-file-to-try-harder.patch
Patch159: pciback-disable-root-port-aer.patch
Patch160: pciback-mask-root-port-comp-timeout.patch
Patch162: xen-netback-record-rx-queue-for-skb.patch
Patch163: 0001-xen-netback-don-t-populate-the-hash-cache-on-XenBus-.patch
Patch164: block-loop-only-flush-on-close-if-attached.patch
Patch165: CA-135938-nfs-disconnect-on-rpc-retry.patch
Patch166: sunrpc-force-disconnect-on-connection-timeout.patch
Patch167: cifs__queue_reconnect_thread_with_a_delay.patch
Patch168: tg3-alloc-repeat.patch
Patch169: 0001-netfilter-ipset-Fix-race-between-dump-and-swap.patch
Patch170: 0001-scsi-devinfo-Add-Microsoft-iSCSI-target-to-1024-sect.patch
Patch171: dlm__increase_socket_backlog_to_avoid_hangs_with_16_nodes.patch
Patch172: net-core__order-3_frag_allocator_causes_swiotlb_bouncing_under_xen.patch
Patch173: idle_cpu-return-0-during-softirq.patch
Patch174: call-kexec-before-offlining-noncrashing-cpus.patch
Patch175: fnic-disable-tracing-by-default.patch
Patch176: bnx2-disable-gro.patch
Patch177: x86-apic-disable-physflat-under-xen.patch
Patch178: map-1MiB-1-1.patch
Patch179: default-xen-swiotlb-size-128MiB.patch
Patch180: x86-xen-add-cpuid-est-flag-if-present-on-host-hw.patch
Patch181: make-dev_load-noop.patch
Patch184: silence-xen-watchdog.patch
Patch185: disable-pm-timer.patch
Patch186: xen-evtchn-Bind-dyn-evtchn-qemu-dm-interrupt-to-next-online-VCPU.patch
Patch187: net-Do-not-scrub-ignore_df-within-the-same-name-spac.patch
Patch188: 0001-libiscsi-Fix-race-between-iscsi_xmit_task-and-iscsi_.patch
Patch189: CP-13181-net-openvswitch-add-dropping-of-fip-and-lldp.patch
Patch190: build-mipi-dsi-as-a-module.patch
Patch191: intel-gvt-g-enable-out-of-tree-compile.patch
Patch192: debug-pwq-null-point-deref.patch


Source1: kernel-%{version}-%{_arch}.config
Source2: macros.kernel
%if %{do_kabichk}
Source3: check-kabi
Source4: Module.kabi-4.9
%endif

%description
The kernel package contains the Linux kernel (vmlinuz), the core of any
Linux operating system.  The kernel handles the basic functions of the
operating system: memory allocation, process allocation, device input
and output, etc.


%package headers
License: GPLv2
Summary: Header files for the Linux kernel for use by glibc
Group: Development/System
Obsoletes: glibc-kernheaders < 3.0-46
Provides: glibc-kernheaders = 3.0-46
Provides: kernel-headers = %{uname}
Conflicts: kernel-headers < %{uname}

%description headers
Kernel-headers includes the C header files that specify the interface
between the Linux kernel and userspace libraries and programs.  The
header files define structures and constants that are needed for
building most standard programs and are also needed for rebuilding the
glibc package.

%package devel
License: GPLv2
Summary: Development package for building kernel modules to match the %{uname} kernel
Group: System Environment/Kernel
AutoReqProv: no
Provides: kernel-devel-%{_arch} = %{version}-%{release}
Provides: kernel-devel-uname-r = %{uname}

%description devel
This package provides kernel headers and makefiles sufficient to build modules
against the %{uname} kernel.

%prep

%autosetup -p1

make mrproper
cp -f %{SOURCE1} .config

%build

# This override tweaks the kernel makefiles so that we run debugedit on an
# object before embedding it.  When we later run find-debuginfo.sh, it will
# run debugedit again.  The edits it does change the build ID bits embedded
# in the stripped object, but repeating debugedit is a no-op.  We do it
# beforehand to get the proper final build ID bits into the embedded image.
# This affects the vDSO images in vmlinux, and the vmlinux image in bzImage.
export AFTER_LINK='sh -xc "/usr/lib/rpm/debugedit -b %{buildroot} -d /usr/src/debug -i $@ > $@.id"'

make silentoldconfig
make %{?_smp_mflags} bzImage
make %{?_smp_mflags} modules

#
# Check the kernel ABI (KABI) has not changed.
#
# The format of kernel ABI version is V.P.0+A.
#
#   V - kernel version (e.g., 3)
#   P - kernel patch level (e.g., 10)
#   A - KABI version.
#
# Note that the version does not include the sub-level version used in
# the stable kernels.  This allows the kernel updates to include the
# latest stable release without changing the KABI.
#
# ABI checking should be disabled by default for development kernels
# (those with a "0" ABI version).
#
# If this check fails you can:
#
# 1. Remove or edit patches until the ABI is the same again.
#
# 2. Remove the functions from the KABI file (if those functions are
#    guaranteed to not be used by any driver or third party module).
#    Be careful with this option.
#
# 3. Increase the ABI version (in the abi-version patch) and copy
#    the Module.symvers file from the build directory to the root of
#    the patchqueue repository and name it Module.kabi.
#
%if %{do_kabichk}
    echo "**** kABI checking is enabled in kernel SPEC file. ****"
    %{SOURCE3} -k %{SOURCE4} -s Module.symvers || exit 1
%endif

%install
# Install kernel
install -d -m 755 %{buildroot}/boot
install -m 644 .config %{buildroot}/boot/config-%{uname}
install -m 644 System.map %{buildroot}/boot/System.map-%{uname}
install -m 644 arch/x86/boot/bzImage %{buildroot}/boot/vmlinuz-%{uname}
truncate -s 20M %{buildroot}/boot/initrd-%{uname}.img
ln -sf vmlinuz-%{uname} %{buildroot}/boot/vmlinuz-%{short_uname}-xen
ln -sf initrd-%{uname}.img %{buildroot}/boot/initrd-%{short_uname}-xen.img

# Install modules
# Override $(mod-fw) because we don't want it to install any firmware
# we'll get it from the linux-firmware package and we don't want conflicts
make INSTALL_MOD_PATH=%{buildroot} modules_install mod-fw=
# mark modules executable so that strip-to-file can strip them
find %{buildroot}/lib/modules/%{uname} -name "*.ko" -type f | xargs chmod u+x

install -d -m 755 %{buildroot}/lib/modules/%{uname}/extra
install -d -m 755 %{buildroot}/lib/modules/%{uname}/updates

make INSTALL_MOD_PATH=%{buildroot} vdso_install

# Save debuginfo
install -d -m 755 %{buildroot}/usr/lib/debug/lib/modules/%{uname}
install -m 755 vmlinux %{buildroot}/usr/lib/debug/lib/modules/%{uname}

# Install -headers files
make INSTALL_HDR_PATH=%{buildroot}/usr headers_install

# Install -devel files
install -d -m 755 %{buildroot}/usr/src/kernels/%{uname}-%{_arch}
install -d -m 755 %{buildroot}%{_rpmconfigdir}/macros.d
install -m 644 %{SOURCE2} %{buildroot}%{_rpmconfigdir}/macros.d
echo '%%kernel_version %{uname}' >> %{buildroot}%{_rpmconfigdir}/macros.d/macros.kernel

# Setup -devel links correctly
ln -nsf %{srcpath} %{buildroot}/lib/modules/%{uname}/source
ln -nsf %{srcpath} %{buildroot}/lib/modules/%{uname}/build

# Copy Makefiles and Kconfigs except in some directories
paths=$(find . -path './Documentation' -prune -o -path './scripts' -prune -o -path './include' -prune -o -type f -a \( -name "Makefile*" -o -name "Kconfig*" \) -print)
cp --parents $paths %{buildroot}%{srcpath}
cp Module.symvers %{buildroot}%{srcpath}
cp System.map %{buildroot}%{srcpath}
cp .config %{buildroot}%{srcpath}
cp -a scripts %{buildroot}%{srcpath}
find %{buildroot}%{srcpath}/scripts -type f -name '*.o' -delete

cp -a --parents arch/x86/include %{buildroot}%{srcpath}
cp -a include %{buildroot}%{srcpath}/include

# files for 'make prepare' to succeed with kernel-devel
cp -a --parents arch/x86/entry/syscalls/syscall_32.tbl %{buildroot}%{srcpath}
cp -a --parents arch/x86/entry/syscalls/syscalltbl.sh %{buildroot}%{srcpath}
cp -a --parents arch/x86/entry/syscalls/syscallhdr.sh %{buildroot}%{srcpath}
cp -a --parents arch/x86/entry/syscalls/syscall_64.tbl %{buildroot}%{srcpath}
cp -a --parents arch/x86/tools/relocs_32.c %{buildroot}%{srcpath}
cp -a --parents arch/x86/tools/relocs_64.c %{buildroot}%{srcpath}
cp -a --parents arch/x86/tools/relocs.c %{buildroot}%{srcpath}
cp -a --parents arch/x86/tools/relocs_common.c %{buildroot}%{srcpath}
cp -a --parents arch/x86/tools/relocs.h %{buildroot}%{srcpath}
cp -a --parents tools/include/tools/le_byteshift.h %{buildroot}%{srcpath}
cp -a --parents arch/x86/purgatory/purgatory.c %{buildroot}%{srcpath}
cp -a --parents arch/x86/purgatory/sha256.h %{buildroot}%{srcpath}
cp -a --parents arch/x86/purgatory/sha256.c %{buildroot}%{srcpath}
cp -a --parents arch/x86/purgatory/stack.S %{buildroot}%{srcpath}
cp -a --parents arch/x86/purgatory/string.c %{buildroot}%{srcpath}
cp -a --parents arch/x86/purgatory/setup-x86_64.S %{buildroot}%{srcpath}
cp -a --parents arch/x86/purgatory/entry64.S %{buildroot}%{srcpath}
cp -a --parents arch/x86/boot/string.h %{buildroot}%{srcpath}
cp -a --parents arch/x86/boot/string.c %{buildroot}%{srcpath}
cp -a --parents arch/x86/boot/ctype.h %{buildroot}%{srcpath}

# Copy .config to include/config/auto.conf so "make prepare" is unnecessary.
cp -a %{buildroot}%{srcpath}/.config %{buildroot}%{srcpath}/include/config/auto.conf

# Make sure the Makefile and version.h have a matching timestamp so that
# external modules can be built
touch -r %{buildroot}%{srcpath}/Makefile %{buildroot}%{srcpath}/include/generated/uapi/linux/version.h

find %{buildroot} -name '.*.cmd' -type f -delete

%post
> %{_localstatedir}/lib/rpm-state/regenerate-initrd-%{uname}

depmod -ae -F /boot/System.map-%{uname} %{uname}

mkdir -p %{_rundir}/reboot-required.d/%{name}
> %{_rundir}/reboot-required.d/%{name}/%{version}-%{release}

%posttrans
if [ -e %{_localstatedir}/lib/rpm-state/regenerate-initrd-%{uname} ]; then
    rm %{_localstatedir}/lib/rpm-state/regenerate-initrd-%{uname}
    dracut -f /boot/initrd-%{uname}.img %{uname}
fi

%files
/boot/vmlinuz-%{uname}
/boot/vmlinuz-%{short_uname}-xen
/boot/initrd-%{short_uname}-xen.img
%ghost /boot/initrd-%{uname}.img
/boot/System.map-%{uname}
/boot/config-%{uname}
%dir /lib/modules/%{uname}
/lib/modules/%{uname}/extra
/lib/modules/%{uname}/kernel
/lib/modules/%{uname}/modules.order
/lib/modules/%{uname}/modules.builtin
/lib/modules/%{uname}/updates
/lib/modules/%{uname}/vdso
%exclude /lib/modules/%{uname}/vdso/.build-id
%ghost /lib/modules/%{uname}/modules.alias
%ghost /lib/modules/%{uname}/modules.alias.bin
%ghost /lib/modules/%{uname}/modules.builtin.bin
%ghost /lib/modules/%{uname}/modules.dep
%ghost /lib/modules/%{uname}/modules.dep.bin
%ghost /lib/modules/%{uname}/modules.devname
%ghost /lib/modules/%{uname}/modules.softdep
%ghost /lib/modules/%{uname}/modules.symbols
%ghost /lib/modules/%{uname}/modules.symbols.bin

%files headers
/usr/include/*

%files devel
/lib/modules/%{uname}/build
/lib/modules/%{uname}/source
%verify(not mtime) /usr/src/kernels/%{uname}-%{_arch}
%{_rpmconfigdir}/macros.d/macros.kernel

%changelog
* Mon Dec 10 2018 Rushikesh Jadhav <rushikesh7@gmail.com> - 4.9-144.1
- Added kernel incremental patch to 4.9.144
- Separated XCP-NG & XenServer patches with comments about modified ones.

* Sun Dec 07 2018 Rushikesh Jadhav <rushikesh7@gmail.com> - 4.9-143.1
- Added patches 106-192 and kernel incremental patch to 4.9.143.

* Sun Dec 02 2018 Rushikesh Jadhav <rushikesh7@gmail.com> - 4.9-0.0.6
- Changed kernel versioning to base 4.9. 
- It uses 4.9.135 as base and applies incremental patches from there till 4.9.142.

* Sat Oct 27 2018 Rushikesh Jadhav <rushikesh7@gmail.com> - 4.9.135-0.0.5
- Enabled kernel support for NFS Client 4.2, CephFS & NTFS write support

* Wed Oct 24 2018 Rushikesh Jadhav <rushikesh7@gmail.com> - 4.9.135-0.0.4
- Changed Package name to kernel-exp

* Sat Oct 20 2018 Rushikesh Jadhav <rushikesh7@gmail.com> - 4.9.135-0.0.3
- Updated to recent stable 4.9.135
- Added Patch2 to Patch4

* Wed Oct 17 2018 Rushikesh Jadhav <rushikesh7@gmail.com> - 4.9.133-0.0.2
- Added Patch1

* Tue Oct 16 2018 Rushikesh Jadhav <rushikesh7@gmail.com> - 4.9.133-0.0.1
- First version with ABI fixes (Patch99) & Patch0 for blktap
