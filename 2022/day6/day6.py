def read_input(filename):
    with open(filename) as o:
        input_data = o.readlines()
    return input_data


def get_start_of_packet(input_line, lookup_item):
    if lookup_item == "marker":
        PROTOCOL_BUFFER = 4
    elif lookup_item == "message":
        PROTOCOL_BUFFER = 14
    START_OF_PACKET = PROTOCOL_BUFFER
    PACKET_VALUE = 0
    while True:
        substring = input_line[PACKET_VALUE:START_OF_PACKET]
        if len(set(substring)) == PROTOCOL_BUFFER:
            break
        else:
            PACKET_VALUE += 1
            START_OF_PACKET += 1
    
    return START_OF_PACKET



if __name__ == "__main__":
    assert get_start_of_packet("mjqjpqmgbljsphdztnvjfqwrcgsmlb", "marker") == 7
    assert get_start_of_packet("bvwbjplbgvbhsrlpgdmjqwftvncz", "marker") == 5
    assert get_start_of_packet("nppdvjthqldpwncqszvftbrmjlhg", "marker") == 6
    assert get_start_of_packet("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", "marker") == 10
    assert get_start_of_packet("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", "marker") == 11
    input_data = read_input("input6.txt")[0]
    input_data = input_data.strip()
    # print(len(input_data))
    print(get_start_of_packet(input_data, "marker"))
    
    assert get_start_of_packet("mjqjpqmgbljsphdztnvjfqwrcgsmlb", "message") == 19
    assert get_start_of_packet("bvwbjplbgvbhsrlpgdmjqwftvncz", "message") == 23
    assert get_start_of_packet("nppdvjthqldpwncqszvftbrmjlhg", "message") == 23
    assert get_start_of_packet("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", "message") == 29
    assert get_start_of_packet("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", "message") == 26
    print(get_start_of_packet(input_data, "message"))