# luizribeiro/workbench

An example workbench for [`labctl`](https://github.com/luizribeiro/labctl)

## Setup

```
git clone https://github.com/luizribeiro/workbench
cd workbench
pipenv install
```

## Usage

First make sure you're in the workbench virtual environment:
```
pipenv shell
```

Once you're done with that, you can simply run any `labctl` command, such
as:

```
labctl devices
```

## Experiments

### noop

This is a "noop" (no operation) experiment. You can run it without any
hardware.

```
labctl run sequences/noop.yml
```
