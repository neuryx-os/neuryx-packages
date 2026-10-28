# patterns-neuryx

Pattern que define a camada de IA do Neuryx.

## Conteúdo

O pattern puxa:

- o **pattern do Lyra Server** (base do sistema — ADR 0001);
- `llama-cpp` (variante CPU por padrão; CUDA e Vulkan conforme o hardware);
- `neuryx-tuning`;
- `neuryxctl`;
- `neuryx-release`.

**Não** puxa driver NVIDIA nem CUDA
([ADR 0004](https://github.com/neuryx-os/research/blob/main/adr/0004-driver-nvidia-no-primeiro-boot.md)).

## Origem do código

Este repositório.

## Dependências

Depende de existir no Lyra um pattern reutilizável do Server. O nome usado no
spec é provisório.
