from owmeta_core.context import Context
from owmeta_core.command import OWM

conn = OWM().connect()
ctx = conn(Context)(ident='http://openworm.org/data')

from owmeta.network import Network
from owmeta.worm import Worm
from owmeta.neuron import Neuron

with ctx.stored(Worm, Neuron, Network) as cctx:
    print(cctx)
    print(ctx.stored(Worm))
    nn = ctx.stored(Worm).query().neuron_network()
    w = cctx.Worm()
    net = cctx.Network()
    w.neuron_network(net)
    neur = cctx.Neuron.query()
    net.neuron(neur)
    print()
    print(nn)
    print(neur, neur.count())

conn.disconnect()
