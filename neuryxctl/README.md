# neuryxctl (pacote)

Empacotamento da CLI do Neuryx.

## Origem do código

Repositório [`neuryx-os/neuryxctl`](https://github.com/neuryx-os/neuryxctl),
em Go ([ADR 0005](https://github.com/neuryx-os/research/blob/main/adr/0005-neuryxctl-em-go.md)).
O spec será adicionado aqui quando houver a primeira versão marcada (tag).

## Dependências

- Build: `go` (versão mínima conforme `go.mod`).
- Runtime: `systemd`. O `neuryxctl` instala o driver da GPU no primeiro boot,
  mas não o declara como dependência (ADR 0004).
