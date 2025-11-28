from __future__ import annotations

from typing import Any

from django import forms


class LatLonWidget(forms.MultiWidget):
    def __init__(self, *args: Any, **kwargs: Any):
        widgets = forms.TextInput(), forms.TextInput()
        super().__init__(widgets, *args, **kwargs)

    def decompress(self, value: Any) -> list[float | None]:
        if value:
            coords: tuple[float, float] = value.coords
            return [round(x, 6) for x in coords]
        return [None, None]


class LatLonField(forms.MultiValueField):
    widget = LatLonWidget
    require_all_fields = True

    def __init__(self, *args: Any, **kwargs: Any):
        fields = (
            forms.FloatField(min_value=-180, max_value=180),
            forms.FloatField(min_value=-90, max_value=90),
        )
        super().__init__(fields, *args, **kwargs)

    def compress(self, data_list: list[float]) -> str:
        return "SRID=4326;POINT({} {})".format(*data_list)
