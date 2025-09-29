# 7sim

Simulation and statistics engine for 7 wonders

## Release

The latest release provides a compiled pdf and pptx of the latest commit version of the slides

## Development

### Dependencies

Dependencies are tracked using Nix.

To enter the development environment run:

```sh
nix develop
```

Also marp should be installed seperately for slides compilation to work.

The easiest way to install marp is through npm:

```sh
npm install -g @marp-team/marp-cli@latest
```

### Usage

Commands are simplified using just.

To see all available commands run:

```
just
```

Use the following command to compile slides and open a preview of the slides on the browser:

```sh
./preview.sh
```

Use the following command to compile slides into a pdf file:

```sh
marp --pdf slides.md
```
