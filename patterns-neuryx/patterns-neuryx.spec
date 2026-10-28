#
# spec file for package patterns-neuryx
#
# ESQUELETO — este spec não compila. Nomes provisórios.
#
# ADR 0001: o Neuryx é uma edição do Lyra OS Server. A base vem do pattern
# do Lyra; este pattern acrescenta apenas a camada de IA.
# ADR 0004: este pattern não inclui driver NVIDIA nem CUDA.
#

Name:           patterns-neuryx
Version:        0
Release:        0
Summary:        Patterns do Neuryx
License:        GPL-3.0-only
URL:            https://github.com/neuryx-os/neuryx-packages
BuildArch:      noarch

%description
Patterns de instalação do Neuryx.

%package ai
Summary:        Neuryx: camada de IA sobre o Lyra OS Server
# Base do sistema: pattern do Lyra Server.
# nome a confirmar no projeto Lyra
Requires:       patterns-lyraos-server
Requires:       neuryx-release
Requires:       neuryxctl
Requires:       neuryx-tuning
Requires:       llama-cpp-cpu
Recommends:     llama-cpp-vulkan
# Provides:       pattern() = neuryx_ai
# Provides:       pattern-category() = Neuryx
# Provides:       pattern-order() = 1000
# Provides:       pattern-visible()

%description ai
Pacotes da camada de IA do Neuryx: llama.cpp, ferramenta neuryxctl e perfis
de ajuste do sistema.

# %files ai
# %dir %{_defaultdocdir}/patterns
# %{_defaultdocdir}/patterns/neuryx_ai.txt

# %changelog
