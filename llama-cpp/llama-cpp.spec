#
# spec file for package llama-cpp
#
# ESQUELETO — este spec não compila. Ele registra a estrutura prevista do
# pacote e será completado após as pesquisas 01 e 03 do repositório research.
#
# ADR 0003 (https://github.com/neuryx-os/research/blob/main/adr/0003-llama-cpp-sem-fork.md):
# o llama.cpp NÃO é bifurcado. Este pacote compila o código upstream de
# https://github.com/ggml-org/llama.cpp em uma versão FIXADA e testada.
# Atualizar a versão é uma decisão explícita, com build e testes no OBS.
#
# ADR 0004: nenhum componente proprietário da GPU é declarado como
# dependência nem redistribuído por este pacote. Ele é instalado no
# primeiro boot pelo neuryxctl.
#

Name:           llama-cpp
# Versão upstream fixada (tag bNNNN). A definir pelo tópico 03.
Version:        0
Release:        0
Summary:        Inferência de modelos de linguagem em C/C++
License:        MIT
URL:            https://github.com/ggml-org/llama.cpp
# Source0:      %{url}/archive/refs/tags/b%{version}.tar.gz#/llama.cpp-b%{version}.tar.gz

# BuildRequires:  cmake
# BuildRequires:  gcc-c++
# BuildRequires:  pkgconfig
# Variante Vulkan:
# BuildRequires:  pkgconfig(vulkan)
# BuildRequires:  shaderc
# Variante de GPU NVIDIA: dependências de build a definir pelo tópico 01.

%description
llama.cpp compila e executa modelos de linguagem no formato GGUF em CPU e GPU.
Inclui llama-server, com API HTTP compatível com a da OpenAI, e llama-bench.

# %package cpu
# Summary:        llama.cpp com backend de CPU
#
# %description cpu
# Build do llama.cpp com backend de CPU.

# %package cuda
# Summary:        llama.cpp com backend CUDA
#
# %description cuda
# Build do llama.cpp com backend CUDA. Requer o driver da GPU instalado com
# "neuryxctl gpu setup"; este pacote não o declara como dependência.

# %package vulkan
# Summary:        llama.cpp com backend Vulkan
#
# %description vulkan
# Build do llama.cpp com backend Vulkan.

# %prep
# %autosetup -n llama.cpp-b%{version}

# %build
# Um diretório de build por variante. Flags a definir pelo tópico 03:
#   cpu:    -DGGML_NATIVE=OFF
#   cuda:   -DGGML_CUDA=ON -DCMAKE_CUDA_ARCHITECTURES=<lista>
#   vulkan: -DGGML_VULKAN=ON

# %install

# %files cpu
# %files cuda
# %files vulkan

# %changelog
