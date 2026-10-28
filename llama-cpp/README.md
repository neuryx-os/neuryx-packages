# llama-cpp

Pacote do [llama.cpp](https://github.com/ggml-org/llama.cpp), motor de
inferência principal do Neuryx.

## Origem do código

Código **upstream**, sem fork, em uma **versão fixada e testada** (tag
`bNNNN`) — [ADR 0003](https://github.com/neuryx-os/research/blob/main/adr/0003-llama-cpp-sem-fork.md).
A política de atualização será definida no
[tópico 03](https://github.com/neuryx-os/research/blob/main/topics/03-versoes-do-llama-cpp.md).

## Variantes

As variantes são subpacotes do mesmo spec, cada uma com um build do backend:

| Subpacote | Backend | Observação |
| --- | --- | --- |
| `llama-cpp-cpu` | CPU | Funciona em qualquer máquina |
| `llama-cpp-cuda` | CUDA | Exige driver NVIDIA instalado pelo `neuryxctl gpu setup` |
| `llama-cpp-vulkan` | Vulkan | GPUs com driver Vulkan (Mesa, NVIDIA) |

## Dependências

- Build: `cmake`, `gcc-c++`, `pkgconfig`, `vulkan-devel`/`shaderc` (Vulkan).
  As dependências de build da variante CUDA dependem da conclusão do
  [tópico 01](https://github.com/neuryx-os/research/blob/main/topics/01-licenciamento-nvidia-cuda.md).
- Runtime: nenhuma dependência de pacotes NVIDIA é declarada (ADR 0004).
