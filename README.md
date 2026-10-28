# neuryx-packages

Specs e serviços OBS dos pacotes do Neuryx (llama.cpp, patterns, release).

**Status:** Planejado

## Propósito

Este repositório reúne a fonte dos pacotes RPM do Neuryx publicados no
[Open Build Service](https://build.opensuse.org). Os pacotes formam a camada de
IA que, somada à base do Lyra OS Server, compõe a distribuição
([ADR 0001](https://github.com/neuryx-os/research/blob/main/adr/0001-edicao-do-lyra-server.md)).

Os specs são **esqueletos comentados** e ainda não compilam.

## Projeto OBS previsto

`home:rodrigosbrito:lyra:Neuryx` (nome provisório), como subprojeto do projeto
OBS do Lyra, de onde vêm a base e o pattern do Lyra Server. O projeto ainda não
foi criado.

## Pacotes

| Diretório | Pacote | Fonte do código |
| --- | --- | --- |
| [`llama-cpp/`](llama-cpp/) | `llama-cpp` e subpacotes `-cpu`, `-cuda`, `-vulkan` | Upstream [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp), versão fixada |
| [`neuryx-release/`](neuryx-release/) | `neuryx-release` | Este repositório |
| [`patterns-neuryx/`](patterns-neuryx/) | `patterns-neuryx` | Este repositório |
| [`neuryx-tuning/`](neuryx-tuning/) | `neuryx-tuning` | [`neuryx-os/neuryx-tuning`](https://github.com/neuryx-os/neuryx-tuning) |
| [`neuryxctl/`](neuryxctl/) | `neuryxctl` | [`neuryx-os/neuryxctl`](https://github.com/neuryx-os/neuryxctl) |

## Regras

- **llama.cpp sem fork:** o pacote compila o código upstream em versão fixada
  e testada ([ADR 0003](https://github.com/neuryx-os/research/blob/main/adr/0003-llama-cpp-sem-fork.md)).
- **Sem driver NVIDIA nem CUDA:** nenhum spec declara o driver NVIDIA ou o
  CUDA como dependência, nem os redistribui
  ([ADR 0004](https://github.com/neuryx-os/research/blob/main/adr/0004-driver-nvidia-no-primeiro-boot.md)).
- Tudo o que pertence à base do sistema fica no Lyra, não aqui.

## Relação com outros repositórios

- [`neuryx-server`](https://github.com/neuryx-os/neuryx-server): consome `patterns-neuryx` na imagem.
- [`neuryx-tuning`](https://github.com/neuryx-os/neuryx-tuning) e [`neuryxctl`](https://github.com/neuryx-os/neuryxctl): fontes dos pacotes de mesmo nome.
- [`research`](https://github.com/neuryx-os/research): ADRs 0001, 0003 e 0004; tópicos 01 e 03.

## Licença

Os specs e arquivos deste repositório estão sob [GPL-3.0](LICENSE). Cada
pacote mantém a licença do seu código de origem (o llama.cpp, por exemplo, é MIT).
