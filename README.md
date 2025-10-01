# 7sim

Wannabe simulation and statistics engine for 7 wonders

As of now it only generates funny slides for a presentation on the subject :)

## Release

This project generates slides in ITALIAN for a slides night with friends

The latest release provides a compiled pdf and pptx of the latest commit version of the slides

Also the slides are available on [gh-pages](https://oldranda1414.github.io/7sim/)

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

```sh
just
```

To print stats and generate graphs:

```sh
just stats
```

To open slides in watch mode:

```sh
just slides
```
