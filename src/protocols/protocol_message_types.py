from enum import Enum


class ProtocolMessageTypes(Enum):
    # Shared protocol (all services)
    handshake = 1
    handshake_ack = 2

    # Harvester protocol (harvester <-> farmer)
    harvester_handshake = 3
    new_signage_point_harvester = 4
    new_proof_of_space = 5
    request_signatures = 6
    respond_signatures = 7

    # Farmer protocol (farmer <-> full_node)
    new_signage_point = 8
    declare_proof_of_space = 9
    request_signed_values = 10
    signed_values = 11

    # Timelord protocol (timelord <-> full_node)
    new_peak_timelord = 12
    new_unfinished_sub_block_timelord = 13
    new_infusion_point_vdf = 14
    new_signage_point_vdf = 15
    new_end_of_sub_slot_vdf = 16

    # Full node protocol (full_node <-> full_node)
    new_peak = 17
    new_transaction = 18
    request_transaction = 19
    respond_transaction = 20
    request_proof_of_weight = 21
    respond_proof_of_weight = 22
    request_sub_block = 23
    respond_sub_block = 24
    request_sub_blocks = 25
    respond_sub_blocks = 26
    reject_sub_blocks = 27
    new_unfinished_sub_block = 28
    request_unfinished_sub_block = 29
    respond_unfinished_sub_block = 30
    new_signage_point_or_end_of_sub_slot = 31
    request_signage_point_or_end_of_sub_slot = 32
    respond_signage_point = 33
    respond_end_of_sub_slot = 34
    request_mempool_transactions = 35
    request_compact_vdfs = 36
    respond_compact_vdfs = 37
    request_peers = 38
    respond_peers = 39

    # Wallet protocol (wallet <-> full_node)
    request_puzzle_solution = 40
    respond_puzzle_solution = 41
    reject_puzzle_solution = 42
    send_transaction = 43
    transaction_ack = 44
    new_peak_wallet = 45
    request_sub_block_header = 46
    respond_sub_block_header = 47
    reject_header_request = 48
    request_removals = 49
    respond_removals = 50
    reject_removals_request = 51
    request_additions = 52
    respond_additions = 53
    reject_additions_request = 54
    request_header_blocks = 55
    reject_header_blocks = 56
    respond_header_blocks = 57

    # Introducer protocol (introducer <-> full_node)
    request_peers_introducer = 58
    respond_peers_introducer = 59
