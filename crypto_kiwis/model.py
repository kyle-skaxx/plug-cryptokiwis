from dataclasses import dataclass
from plug.abstract import Model

@dataclass
class KiwiModel(Model):
    fqdn = "cryptokiwi.KiwiModel"
    id:str
    name:str
    owner_address:str

    def __init__(self, id, name, owner_address):
        self.id = id
        self.name = name
        self.owner_address = owner_address

    @classmethod
    def default_factory(cls):
        return cls()

    @staticmethod
    def pack(registry, obj):
        #print('kiwi', obj)
        return {
            "id": obj.id,
            "name": obj.name,
            "owner_address": obj.owner_address,
        }

    @classmethod
    def unpack(cls, registry, payload):
        #print('kiwi', payload)
        return cls(
            id=paylaod["id"],
            name=payload["name"],
            owner_address=payload["owner_address"]
        )

@dataclass
class KiwiCollectionModel(Model):
    fqdn = "cryptokiwi.KiwiCollectionModel"
    kiwis = []

    def __init__(self, kiwis=[]):
        self.kiwis = kiwis

    @classmethod
    def default_factory(cls):
        return cls()

    @staticmethod
    def pack(registry, obj):
        return {
            "kiwis": obj.kiwis
        }

    @classmethod
    def unpack(cls, registry, payload):
        return cls(
            kiwis=payload['kiwis']
        )
