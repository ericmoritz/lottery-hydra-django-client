from hydraclient.contrib.django.hydraclient import views
from hydraclient.core import client as hydra_client
from rdflib import Namespace, URIRef


lottery = Namespace("http://vocab-ld.org/vocabs/lottery#")


def resource(request, path_info, cfg_irl=None, **kwargs):
    r = hydra_client.get(views.session, cfg_irl, request.build_absolute_uri())
    for (_, _, base_irl) in r.graph.triples((None, lottery.viewSummary, None)):
        kwargs['base_irl'] = base_irl
        return views.resource(request, path_info, **kwargs)
    
    assert False, "{} could not be found".format(lottery.viewSummary)
