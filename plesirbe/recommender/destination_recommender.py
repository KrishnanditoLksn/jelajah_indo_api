import logging

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from plesirbe.models.destination import Destination
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

    "Mapped id as a key and index for value"
    destination_travels = {destination.id: idx for idx, destination in enumerate(destinations)}
    idx_target = destination_travels.get(travels.id)

    """Count Cosine Similarity for every items"""
    cosine_sim = cosine_similarity(tfidf[idx_target], tfidf).flatten()
    logger.info(cosine_sim)
    
    "Sort from small to big idx based on similarity"
    sorted_idx = cosine_sim.argsort()
    
    """Delete Target Elemet"""
    top_sim_idx = sorted_idx[:-1]
    
    """Retrieve rest of TOP N"""
    top_sim_idx = top_sim_idx[-top_n:]
    
    "Invert list from most similar to least similar"
    sim_idx = top_sim_idx[::-1]
    
    "Filter idx from self"
    filtered_idx = []
    for i in sim_idx:
        if i != idx_target:
            filtered_idx.append(i)
            
    sim_idx = filtered_idx
    
    "Insert similarity idx into sim travel list "
    sim_travels = []
    for idx in sim_idx:
        sim_travels.append(destinations[idx])
    return sim_travels

def get_cosine_sim_score(ids,top_n)->list:    
    destinations = list(Destination.objects.all())

    lists = []
    for destination in destinations:
        all_destinations = f"{destination.place_name}"
        all_destinations += f"{destination.description}"
        all_destinations += f"{destination.city}"
        all_destinations += f"{destination.price}"
        lists.append(all_destinations)
        
    vector = TfidfVectorizer(stop_words='english')
    tfidf = vector.fit_transform(lists)

    try:
        travels = Destination.objects.get(id=ids)
    except Destination.DoesNotExist:
        return []
    
    destination_travels = {destination.id: idx for idx, destination in enumerate(destinations)}
    idx_target = destination_travels.get(travels.id)
    cosine_sim = cosine_similarity(tfidf[idx_target], tfidf).flatten()
    
    sorted_idx = cosine_sim.argsort()
    
    top_sim_idx = sorted_idx[:-1]
    
    top_sim_idx = top_sim_idx[-top_n:]
    
    sim_idx = top_sim_idx[::-1]
    
    
    filtered_idx = []
    for i in sim_idx:
        if i != idx_target:
            filtered_idx.append(i)
            
    sim_idx = filtered_idx
    
    return [float(cosine_sim[i]) for i in sim_idx]