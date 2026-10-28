#
# spec file for package neuryx-release
#
# ESQUELETO — este spec não compila. Valores provisórios.
#

Name:           neuryx-release
Version:        0
Release:        0
Summary:        Identificação da distribuição Neuryx
License:        GPL-3.0-only
URL:            https://github.com/neuryx-os/neuryx-packages
BuildArch:      noarch

# Substitui o pacote de release do Lyra OS Server.
# Provides:       distribution-release
# Conflicts:      otherproviders(distribution-release)
# nome do pacote de release do Lyra a confirmar no projeto Lyra

%description
Arquivos de identificação do Neuryx: os-release, issue e motd.

# %install
# install -Dm0644 os-release %{buildroot}%{_prefix}/lib/os-release
# ln -s ..%{_prefix}/lib/os-release %{buildroot}%{_sysconfdir}/os-release
#
# Conteúdo previsto de os-release:
#   NAME="Neuryx"
#   ID=neuryx
#   ID_LIKE="lyraos opensuse-leap opensuse suse"   # a confirmar
#   PRETTY_NAME="Neuryx"
#   HOME_URL="https://github.com/neuryx-os"
#   BUG_REPORT_URL="https://github.com/neuryx-os/neuryx-packages/issues"

# %files
# %{_prefix}/lib/os-release
# %{_sysconfdir}/os-release

# %changelog
