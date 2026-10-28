# neuryx-release

Identificação da distribuição.

## Conteúdo previsto

- `/etc/os-release` (via `/usr/lib/os-release`) com `NAME="Neuryx"`,
  `ID=neuryx` e `ID_LIKE` apontando para o Lyra OS e o openSUSE.
- Branding mínimo em texto: `/etc/issue` e `/etc/motd`.

Nenhum elemento gráfico; os logos ficam em
[`neuryx-os/brand`](https://github.com/neuryx-os/brand).

## Origem do código

Este repositório.

## Dependências

Precisa substituir (`Conflicts`/`Provides`) o pacote de release do Lyra OS
Server. O nome desse pacote e os valores de `ID_LIKE` devem ser confirmados com
o projeto Lyra (tópico
[04](https://github.com/neuryx-os/research/blob/main/topics/04-dependencia-da-base-lyra.md)).
