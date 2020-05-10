import pp
from pp.ports import add_port_markers
from ubc.layers import LAYER


@pp.autoname
def waveguide(layer=LAYER.WG, layers_cladding=[], **kwargs):
    c = pp.c.waveguide(layer=layer, layers_cladding=layers_cladding, **kwargs)
    add_port_markers(c)
    return c


if __name__ == "__main__":
    c = waveguide()
    pp.show(c)
