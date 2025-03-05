import logging

from infrahub_sdk.generator import InfrahubGenerator

class TagDuplicator(InfrahubGenerator):
    async def generate(self, data: dict) -> None:
        log = logging.getLogger("infrahub.tasks")

        name = data["BuiltinTag"]["edges"][0]["node"]["name"]["value"]

        for i in range(1, 206):
            tag = await self.client.create("BuiltintTag", name=f"{name}{i}")
            await tag.save(allow_upsert=True)
            log.info(f"Created {name}{i}")
       
