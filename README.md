# Bridge Trainer

Python Project to develop training tools for Contract Bridge. This will include a tool to deal hands for practicing bidding and play, and explorations into bidding system evaluation.

## Developer Guide

The repository is configured with a simple Python 3.12 DevContainer that provides pipx for managing development tooling. Poetry is used for managing python package dependencies and has been pre-installed. If you don't have access to a machine with Docker and Virtualization capabilties, you can open this workspace in GitPod by clicking the badge below.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/bar-raisers/bridge-trainer)

### Running Trunk Superlinter

`trunk check`

### Running Unit Tests

`python3 -m unittest discover`

## Generating Deals

To generate deals you will need to checkout the repository, open the DevContainer, install the third party dependencies via Poetry, and then run the program with the appropriate command line arguments.

```bash
poetry install
python3 main.py <criteria_input_path>.json <pbn_output_path>.pbn --deal_quantity=<desired_quantity>
```

You can find sample criteria files in the `examples` directory.
