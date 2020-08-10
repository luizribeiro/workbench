from dataclasses import dataclass

from labby.experiment import (
    BaseInputParameters,
    BaseOutputData,
    Experiment,
)


@dataclass(frozen=True)
class OutputData(BaseOutputData):
    target_voltage: float
    target_current: float
    actual_voltage: float
    actual_current: float


@dataclass(frozen=True)
class InputParameters(BaseInputParameters):
    pass


class SimpleExperiment(Experiment[InputParameters, OutputData]):
    SAMPLING_RATE_IN_HZ: float = 1.0
    DURATION_IN_SECONDS: float = 30.0

    def start(self) -> None:
        power_supply = self.get_power_supply("zup-6-132")
        power_supply.open()
        power_supply.set_target_voltage(5)
        power_supply.set_target_current(0.100)
        power_supply.set_output_on(True)

    def measure(self) -> OutputData:
        power_supply = self.get_power_supply("zup-6-132")

        target_voltage = power_supply.get_target_voltage()
        target_current = power_supply.get_target_current()
        actual_voltage = power_supply.get_actual_voltage()
        actual_current = power_supply.get_actual_current()

        return OutputData(
            actual_voltage=actual_voltage,
            actual_current=actual_current,
            target_voltage=target_voltage,
            target_current=target_current,
        )

    def stop(self) -> None:
        power_supply = self.get_power_supply("zup-6-132")
        power_supply.set_output_on(False)
        power_supply.close()
