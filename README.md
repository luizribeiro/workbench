# luizribeiro/workbench

An example workbench for [`labby`](https://github.com/luizribeiro/labby)

## Setup

```
git clone https://github.com/luizribeiro/workbench
cd workbench
poetry install
```

## Usage

First make sure you're in the workbench virtual environment:
```
poetry shell
```

Once you're done with that, you can simply run any `labby` command, such
as:

```
labby devices
```

## Experiments

### noop

This is a "noop" (no operation) experiment. You can run it without any
hardware.

```
labby run sequences/noop.yml
```
