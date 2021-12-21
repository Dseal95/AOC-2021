from functools import reduce
from operator import mul

map = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111'}


def bits_from_hex(hex_input):
    bits = ''.join([map[i] for i in hex_input])
    len_data = len(bits)
    if len_data % 4 != 0:
        bits = "0" * (4 - len_data % 4) + bits
    return bits


def make_packet_tree(bits):
    packet = {
        "version": int(bits[0:3], 2),
        "type_id": int(bits[3:6], 2),
        "children": []
    }
    if packet["type_id"] == 4:
        # handle type 4s
        packet["value"], bit_remainder = handle_type_4(bitstring=bits[6:])
        return packet, bit_remainder

    return handle_non_4_type(bits, packet)


def handle_type_4(bitstring):
    bit_remainder = bitstring
    not_last = True
    binary_digits = ""
    while not_last:
        not_last = bit_remainder[0] != "0"
        digit_chunk = bit_remainder[1:5]
        bit_remainder = bit_remainder[5:]
        binary_digits = binary_digits + digit_chunk
    return int(binary_digits, 2), bit_remainder

   
def handle_non_4_type(bitstring, packet):
    lid = bitstring[6]
    if lid == "0":
        # 15 digits after 1st 7 represent bit value for subpacket length 
        offset = 15 
        length_of_sub_packets = int(bitstring[7: 7 + offset], 2)
        sub_remainder = bitstring[7 + offset: 7 + offset + length_of_sub_packets]
        bit_remainder = bitstring[7 + offset + length_of_sub_packets:]
        while len(sub_remainder) > 0:
            # recursively find subpackets
            sub_packet, sub_remainder = make_packet_tree(bits=sub_remainder)
            packet["children"].append(sub_packet)
    elif lid == "1":
        # 11 digits after 1st 7 represent bit value for number of subpackets
        offset = 11
        number_of_sub_packets = int(bitstring[7:(7+offset)], 2)
        bit_remainder = bitstring[7 + offset:]
        for _ in range(number_of_sub_packets):
            sub_packet, bit_remainder = make_packet_tree(bit_remainder)
            packet["children"].append(sub_packet)
    else:
        raise AssertionError(f"lid: {lid} not handled.")

    return packet, bit_remainder


def get_version_sum(packet):
    return (
        packet["version"]
        + sum(get_version_sum(child) for child in packet["children"])
    )


def get_value(packet_tree):
    if packet_tree["type_id"] == 0:
        return sum(get_value(child) for child in packet_tree["children"])
    if packet_tree["type_id"] == 1:
        return reduce(mul, (get_value(child) for child in packet_tree["children"]), 1)
    if packet_tree["type_id"] == 2:
        return min(get_value(child) for child in packet_tree["children"])
    if packet_tree["type_id"] == 3:
        return max(get_value(child) for child in packet_tree["children"])
    if packet_tree["type_id"] == 4:
        return packet_tree["value"]
    if packet_tree["type_id"] == 5:
        return int(get_value(packet_tree["children"][0])
                   > get_value(packet_tree["children"][1]))
    if packet_tree["type_id"] == 6:
        return int(get_value(packet_tree["children"][0])
                   < get_value(packet_tree["children"][1]))
    if packet_tree["type_id"] == 7:
        return int(get_value(packet_tree["children"][0])
                   == get_value(packet_tree["children"][1]))
    
    raise RuntimeError(f"Invalid type id {packet_tree['type_id']}")


s = '8054F9C95F9C1C973D000D0A79F6635986270B054AE9EE51F8001D395CCFE21042497E4A2F6200E1803B0C20846820043630C1F8A840087C6C8BB1688018395559A30997A8AE60064D17980291734016100622F41F8DC200F4118D3175400E896C068E98016E00790169A600590141EE0062801E8041E800F1A0036C28010402CD3801A60053007928018CA8014400EF2801D359FFA732A000D2623CADE7C907C2C96F5F6992AC440157F002032CE92CE9352AF9F4C0119BDEE93E6F9C55D004E66A8B335445009E1CCCEAFD299AA4C066AB1BD4C5804149C1193EE1967AB7F214CF74752B1E5CEDC02297838C649F6F9138300424B9C34B004A63CCF238A56B71520142A5A7FC672E5E00B080350663B44F1006A2047B8C51CC80286C0055253951F98469F1D86D3C1E600F80021118A124261006E23C7E8260008641A8D51F0C01299EC3F4B6A37CABD80252211221A600BC930D0057B2FAA31CDCEF6B76DADF1666FE2E000FA4905CB7239AFAC0660114B39C9BA492D4EBB180252E472AD6C00BF48C350F9F47D2012B6C014000436284628BE00087C5D8671F27F0C480259C9FE16D1F4B224942B6F39CAF767931CFC36BC800EA4FF9CE0CCE4FCA4600ACCC690DE738D39D006A000087C2A89D0DC401987B136259006AFA00ACA7DBA53EDB31F9F3DBF31900559C00BCCC4936473A639A559BC433EB625404300564D67001F59C8E3172892F498C802B1B0052690A69024F3C95554C0129484C370010196269D071003A079802DE0084E4A53E8CCDC2CA7350ED6549CEC4AC00404D3C30044D1BA78F25EF2CFF28A60084967D9C975003992DF8C240923C45300BE7DAA540E6936194E311802D800D2CB8FC9FA388A84DEFB1CB2CBCBDE9E9C8803A6B00526359F734673F28C367D2DE2F3005256B532D004C40198DF152130803D11211C7550056706E6F3E9D24B0'
packet, _ = make_packet_tree(bits_from_hex(s))

# part 1:
print(f'part1: {get_version_sum(packet)}')

# part 2 
print(f'part2: {get_value(packet)}')