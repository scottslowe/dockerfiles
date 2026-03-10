# Docker Container for `na` CLI Tool

This directory contains a `Dockerfile` for containerizing [the `na` tool](https://brettterpstra.com/projects/na/) from Brett Terpstra (here's [the GH repo](https://github.com/ttscoff/na_gem/) for `na`).

## Building

No special commands or flags needed, just a standard `docker build` command.

## Usage

This is a _very_ opinionated build that makes assumptions about filesystem paths that are specific to my environment. You'll need to adjust both the `Dockerfile` and the associated `docker container run` command accordingly.

On my systems, I use:

```bash
docker container run --user 1000:1000 --rm -it -v ~/Sync:/home/slowe/Sync -v ~/.config/na-cli/.na.rc:/home/slowe/.na.rc -v ~/.config/na-cli/.local:/home/slowe/.local slowe/na-cli:0.0.0.10
```

I'll typically alias this as `na`, so that I can simply run `na <subcommand>`.
