import asyncio
from ingestion.embedder import create_embedder

async def test():
    embedder = create_embedder()
    embedding = await embedder.embed_query('test query')
    print('Test embedding successful, dimensions:', len(embedding))

if __name__ == "__main__":
    asyncio.run(test())