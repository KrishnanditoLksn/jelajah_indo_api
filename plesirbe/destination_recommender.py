import logging

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from plesirbe.models import Destination
logger = logging.getLogger(__name__)

def get_similar_destinations(dest_id, top_n=5):
    destinations = list(Destination.objects.all())

    lists = []
    for destination in destinations:
        all_destinations = f"{destination.place_name}"
        all_destinations += f"{destination.description}"
        all_destinations += f"{destination.city}"
        all_destinations += f"{destination.price}"
        lists.append(all_destinations)
    """Vectorize document"""

    vector = TfidfVectorizer(stop_words='english')
    tfidf = vector.fit_transform(lists)

    """Handle when Travel Destination is Null"""
    try:
        travels = Destination.objects.get(id=dest_id)
    except Destination.DoesNotExist:
        return []

    destination_travels = {destination.id: idx for idx, destination in enumerate(destinations)}
    idx_target = destination_travels.get(travels.id)

    """Count Cosine Similarity for every items"""
    cosine_sim = cosine_similarity(tfidf[idx_target], tfidf).flatten()
    logger.info(cosine_sim)
    sim_idx = cosine_sim.argsort()[-top_n - 1:-1][::-1]
    sim_idx = [i for i in sim_idx if i != idx_target]
    sim_travels = [destinations[idx] for idx in sim_idx]

    return sim_travels
