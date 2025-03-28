"""Behavior tests of `ipywidgets`."""
import os

import pytest
from ipywidgets.widgets import FloatSlider


@pytest.mark.skipif("GITHUB_ACTION" in os.environ, reason="ipywidgets instable")
class TestFloatSlider:
    def test_continuous_update(self) -> None:
        slider = FloatSlider()
        assert slider.continuous_update is True
        slider.continuous_update = False
        assert slider.continuous_update is False

    def test_step(self) -> None:
        slider = FloatSlider(min=5, max=7)
        assert slider.step == 0.1
        slider.min = 6
        assert slider.step == 0.1

    def test_value(self) -> None:
        slider = FloatSlider(min=5, max=7, step=0.1)
        assert slider.value == slider.min
