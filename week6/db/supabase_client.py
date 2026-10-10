
# db/supabase_client.py
#
# Sets up one Supabase client, using credentials from config.py.
# Every other file that needs to talk to Supabase should import
# `supabase` from here nothing else should call create_client()
# directly, so there's only ever one client in the whole app.

from supabase import create_client, Client
from config import SUPABASE_URL, SUPABASE_KEY

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


if __name__ == "__main__":
    # Quick manual test confirms the client can actually reach
    # Supabase b
    try:
        response = supabase.table("resources").select("id").limit(1).execute()
        print("Connected successfully.")
        print(f"Sample query result: {response.data}")
    except Exception as e:
        print("Connection failed:")
        print(e)