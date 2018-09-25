from dataclasses import dataclass
from plug.abstract import Transform

from crypto_kiwis.model import KiwiModel, KiwiCollectionModel

import crypto_kiwis.error

@dataclass
class ClaimKiwi(Transform):
    fqdn = "cryptokiwi.GainKiwi"
    claimer: str
    kiwi_id: str

    def required_authorizations(self):
        return {self.claimer}

    @staticmethod
    def required_models():
        return {KiwiModel.fqdn, KiwiCollectionModel.fqdn}

    def required_keys(self):
        return {self.claimer, '_unclaimed'}

    @staticmethod
    def pack(registry, obj):
        #print("obj", obj)
        return {
            "kiwi_id": obj.kiwi_id,
            "claimer": obj.claimer,
            "name": obj.name,
        }

    @classmethod
    def unpack(cls, registry, payload):
        #print("payload", payload)
        return cls(
            kiwi_id=payload["kiwi_id"],
            claimer=payload["claimer"],
            name=payload["name"],
        )

    def verify(self, state_slice):
        kiwis = state_slice[KiwiModel.fqdn]

    def apply(self, state_slice):
        collection = state_slice[KiwiCollectionModel.fqdn]

        unclaimed = collection["_unclaimed"]
        kiwiDict = next(x for x in unclaimed.kiwis if x['id'] == self.kiwi_id)

        if kiwiDict:
            id = kiwiDict['id']
            name = kiwiDict['name']
            state_slice[KiwiModel.fqdn][id] = KiwiModel(id, name, self.claimer)

