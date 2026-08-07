from google.cloud import bigquery

def query_public_dataset():
    """Queries a public dataset in BigQuery."""
    client = bigquery.Client(project="gcp-data-engineer-course03")

    # Example query: Get the top 10 most popular baby names in the US
    query = """
        SELECT order_items.id, order_items.order_id, products.name
        FROM `bigquery-public-data.thelook_ecommerce.order_items` as order_items
        JOIN `bigquery-public-data.thelook_ecommerce.products` as products
        ON order_items.product_id = products.id
    """
    results= client.query(query).to_dataframe()[:20]    

    print(results)

if __name__=="__main__":
    query_public_dataset()
 