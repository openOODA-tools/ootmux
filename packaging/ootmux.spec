Name:           ootmux
Version:        0.1.0
Release:        1%{?dist}
Summary:        Capability-bounded terminal session multiplexer with split panes and stdio sockets.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/ootmux
Source0:        ootmux-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
ootmux is a sovereign, capability-bounded SURFACE MULTIPLEX written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/ootmux
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/ootmux-uninstall

%files
/usr/bin/ootmux
/usr/bin/ootmux-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
