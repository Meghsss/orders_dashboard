def validate_customers(df):
    return df.drop_duplicates(subset='customer_id')

def validate_orders(df, existing_customer_ids):
    df = df[df['amount'] >= 0]
    df = df[df['customer_id'].isin(existing_customer_ids)]
    df = df.drop_duplicates(subset='order_id')
    return df
