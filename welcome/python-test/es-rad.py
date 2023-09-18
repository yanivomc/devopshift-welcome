from datetime import datetime, timedelta
from elasticsearch import Elasticsearch

# Initialize Elasticsearch client
es = Elasticsearch("http://rad-elasticsearch-url:9200/")

def generate_index_name(base, date, hour_minute):
    """Generate the index name based on base, date, and hour_minute."""
    return f"{base}-{date.strftime('%d-%m-%Y')}-%{hour_minute}"

def manage_last_30_days_alias(reprocessed_day=None):
    """Manage the last-30-days alias."""
    today = datetime.now()
    alias_name = "last-30-days"
    indices_to_add = []
    
    for i in range(30):
        current_day = today - timedelta(days=i)
        hour_minute = "+HH.mm"  # you can modify this based on your actual naming scheme
        
        # If the current_day is the reprocessed_day, use the reprocessed index
        if reprocessed_day and current_day.strftime('%d-%m-%Y') == reprocessed_day:
            index_name = generate_index_name("stats-reprocessed", current_day, hour_minute)
        else:
            index_name = generate_index_name("stats-processed", current_day, hour_minute)
        
        indices_to_add.append(index_name)

    # Update the alias
    # First, remove the current indices associated with the alias
    if es.indices.exists_alias(name=alias_name):
        current_indices = list(es.indices.get_alias(name=alias_name).keys())
        actions = [{"remove": {"index": index, "alias": alias_name}} for index in current_indices]
    else:
        actions = []

    # Add the new set of indices to the alias
    actions.extend([{"add": {"index": index, "alias": alias_name}} for index in indices_to_add])

    es.indices.update_aliases({"actions": actions})

# Example Usage
# To manage the alias without any reprocessed day
# manage_last_30_days_alias()

# To manage the alias considering 15th day as reprocessed
# manage_last_30_days_alias(reprocessed_day="15-09-2023")
