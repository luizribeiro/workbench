from dataclasses import dataclass

from labby.experiment import (
    BaseInputParameters,
    BaseOutputData,
    Experiment,
)


@dataclass(frozen=True)
class OutputData(BaseOutputData):
    pass


@dataclass(frozen=True)
class InputParameters(BaseInputParameters):
    pass


class NoopExperiment(Experiment[InputParameters, OutputData]):
    SAMPLING_RATE_IN_HZ: float = 1.0
    DURATION_IN_SECONDS: float = 5.0

    def start(self) -> None:
        pass

    def measure(self) -> OutputData:
        return OutputData()

    def stop(self) -> None:
        pass
