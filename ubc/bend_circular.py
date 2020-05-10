import pp
from pp.ports import add_port_markers
from ubc.layers import LAYER


@pp.autoname
def bend_circular(layer=LAYER.WG, layers_cladding=[], **kwargs):
    c = pp.c.bend_circular(layer=layer, layers_cladding=layers_cladding, **kwargs)
    add_port_markers(c)
    return c


if __name__ == "__main__":
    c = bend_circular()
    pp.show(c)
