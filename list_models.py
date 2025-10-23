import asyncio
from agent.providers import get_embedding_client

async def list_models():
    client = get_embedding_client()
    print('Available models:')
    models = client.models.list()
    model_ids = []
    async for model in models:
        model_ids.append(model.id)
    print(model_ids)

if __name__ == "__main__":
    asyncio.run(list_models())