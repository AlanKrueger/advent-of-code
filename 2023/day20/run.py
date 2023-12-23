# pylint: disable=missing-module-docstring, missing-class-docstring, missing-function-docstring, invalid-name, redefined-outer-name, too-few-public-methods, redefined-builtin

from __future__ import annotations
import argparse
import sys
from typing import List
from enum import Enum

parser = argparse.ArgumentParser()
parser.add_argument('--verbose', action='store_true')
parser.add_argument('--debug', action='store_true')
parser.add_argument('--push-button', type=int, default=1)
parser.add_argument('--part2', action='store_true')
parser.set_defaults(verbose=False, debug=False, part2=False)
args = parser.parse_args()

if args.debug:
    args.verbose = True


BROADCASTER = 'broadcaster'
BUTTON = 'button'
RECEIVER = 'rx'
FLIPFLOP = '%'
CONJUNCTION = '&'

modules = {}
pulses = []


class PulseType(Enum):
    LOW = 0
    HIGH = 1

    def __str__(self) -> str:
        return super().__str__().split('.')[-1].lower()

    def __repr__(self) -> str:
        return self.__str__()


class Pulse:
    def __init__(self, sender: Module, pulse: PulseType, receiver: Module) -> None:
        self.sender = sender
        self.pulse = pulse
        self.receiver = receiver

    def __str__(self) -> str:
        return f'{self.sender.name} -{self.pulse}-> {self.receiver.name}'

    def queue(self) -> None:
        pulses.append(self)

    @staticmethod
    def process_queued_pulses() -> None:
        while pulses:
            pulse = pulses.pop(0)
            if args.verbose:
                print(pulse)
            pulse.receiver.receive(pulse.sender, pulse.pulse)


class Module:
    def __init__(self, name: str, destinations: List[str]) -> None:
        self.name = name
        self.upstreams = {}
        self.destinations = destinations

    def __str__(self) -> str:
        dest_names = [dest.name for dest in self.destinations]
        return f'{self.prefix()}{self.name} -> {", ".join(dest_names)}'

    def prefix(self) -> str:
        return ''

    def link(self) -> None:
        for name in self.destinations:
            if name not in modules:
                modules[name] = Unspecified(name)
        self.destinations = [modules[name] for name in self.destinations]
        for destination in self.destinations:
            destination.upstream(self)

    def upstream(self, upstream: Module) -> None:
        self.upstreams[upstream.name] = upstream

    def send(self, pulse: PulseType) -> None:
        for destination in self.destinations:
            Pulse(self, pulse, destination).queue()

    def receive(self, sender: Module, pulse: PulseType) -> None:
        pass

    @staticmethod
    def parse_from(line: str) -> None:
        (name, destinations) = line.strip().split(" -> ")
        destinations = [dest.strip() for dest in destinations.split(",")]
        if name.startswith(FLIPFLOP):
            return FlipFlop(name[len(FLIPFLOP):], destinations)
        if name.startswith(CONJUNCTION):
            return Conjunction(name[len(CONJUNCTION):], destinations)
        if name == BROADCASTER:
            return Broadcaster(name, destinations)
        raise ValueError(f'Unknown module type: {name}')


class FlipFlop(Module):
    def __init__(self, name: str, destinations: List[Module]) -> None:
        super().__init__(name, destinations)
        self.state = FlipFlop.State.OFF

    class State(Enum):
        OFF = 0
        ON = 1

        def inverse(self) -> FlipFlop.State:
            return FlipFlop.State.ON if self == FlipFlop.State.OFF else FlipFlop.State.OFF

    def prefix(self) -> str:
        return FLIPFLOP

    def receive(self, sender: Module, pulse: PulseType) -> None:
        if pulse == PulseType.LOW:
            self.toggle()

    def toggle(self) -> None:
        pulse = PulseType.HIGH if self.state == FlipFlop.State.OFF else PulseType.LOW
        self.state = self.state.inverse()
        self.send(pulse)


class Conjunction(Module):
    def __init__(self, name: str, destinations: List[Module]) -> None:
        super().__init__(name, destinations)
        self.last_received = {}

    def prefix(self) -> str:
        return CONJUNCTION

    def receive(self, sender: Module, pulse: PulseType) -> None:
        self.last_received[sender.name] = pulse
        last_received = [self.last_received.get(
            upstream, PulseType.LOW) for upstream in self.upstreams]
        pulse = PulseType.LOW if all(
            pulse == PulseType.HIGH for pulse in last_received) else PulseType.HIGH
        self.send(pulse)


class Broadcaster(Module):
    def receive(self, sender: Module, pulse: PulseType) -> None:
        self.send(pulse)


class Button(Module):
    def __init__(self) -> None:
        super().__init__(BUTTON, [BROADCASTER])

    def push(self) -> None:
        self.send(PulseType.LOW)
        Pulse.process_queued_pulses()


class Receiver(Module):
    def __init__(self, name: str) -> None:
        super().__init__(name, [])
        self.received = False

    def receive(self, sender: Module, pulse: PulseType) -> None:
        if pulse == PulseType.LOW:
            self.received = True


class Unspecified(Module):
    def __init__(self, name: str) -> None:
        super().__init__(name, [])

    def receive(self, sender: Module, pulse: PulseType) -> None:
        pass


for line in sys.stdin:
    module = Module.parse_from(line)
    modules[module.name] = module

if args.part2:
    receiver = Receiver(RECEIVER)
    modules[RECEIVER] = Receiver(RECEIVER)

for module in list(modules.values()):
    module.link()

button = Button()
button.link()

if not args.part2:
    args.verbose = True
    for _ in range(args.push_button):
        button.push()
