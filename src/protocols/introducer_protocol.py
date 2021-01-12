from dataclasses import dataclass
from typing import List

from src.types.peer_info import TimestampedPeerInfo
from src.util.streamable import streamable, Streamable

"""
Protocol to introducer
"""


@dataclass(frozen=True)
@streamable
class RequestPeersIntroducer(Streamable):
    """
    Return full list of peers
    """


@dataclass(frozen=True)
@streamable
class RespondPeersIntroducer(Streamable):
    peer_list: List[TimestampedPeerInfo]
