#!/usr/bin/env python3
"""
Module defining an abstract Animal class and its subclasses Dog and Cat.
"""

from abc import ABC, abstractmethod

class Animal(ABC):
    """Abstract class representing an animal."""

    @abstractmethod
    def sound(self):
        """
        Abstract method for animal sound.
        Must be implemented in subclasses.
        """
        pass


class Dog(Animal):
    """Dog subclass of Animal."""

    def sound(self):
        """Return the sound of a dog."""
        return "Bark"


class Cat(Animal):
    """Cat subclass of Animal."""

    def sound(self):
        """Return the sound of a cat."""
        return "Meow"
