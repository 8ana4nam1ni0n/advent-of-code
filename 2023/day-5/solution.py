
def parse_data(data: list[str]) -> tuple[list[int], list[list[list[int]]]]:
    seeds = [int(d) for d in data[0].split(':')[1].split()]
    maps = []
    current = -1
    for d in data[1:]:
        if d[0].isalpha():
            maps.append([])
            current += 1
        else:
            maps[current].append([int(x) for x in d.split()])
    return seeds, maps

# solution 1
def get_minimum_location(seeds: list[int], maps: list[list[list[int]]]):
    minloc = []

    for seed in seeds:
        current = seed
        for map in maps:
            for ranges in map:
                dst, src, rang = ranges
                if src <= current < (src + rang):
                    current = dst + abs(src - current)
                    break
        minloc.append(current)

    return min(minloc)

# solution 2
def get_locations_by_range(seeds, maps):
    min_loc_ranges = []
    for seed, seed_range in seeds:
        # calculate current range using seed_range
        current = [seed, seed + seed_range - 1]
        for i, ranges in enumerate(maps):
            for dst, src, rang in ranges:
                # determine if current is within a range
                next_start = max(current[0], src)
                next_end = min(current[1], src + rang - 1)
                if next_start < next_end:
                    # check if we are partially in when start to next_start - start is not part of that range
                    # ex. start 10 end 15 but range is dst 5 src 12 range 20
                    if next_start > current[0]:
                        # we recurse to find range that is not part of current range
                        s = get_locations_by_range([[current[0], next_start - current[0]]], maps[i:])
                        min_loc_ranges.append(s[0])

                    # check if we are partially in when next-end + 1 to end is not part of that range
                    # ex. start 10 end 15 but range is dst 5 src 8 range 5
                    if next_end < current[1]:
                        # we recurse to find range that is not part of current range
                        e = get_locations_by_range([[next_end + 1, current[1] - next_end]], maps[i:])
                        min_loc_ranges.append(e[0])
                    # update current to corresponding dst
                    current[0] = next_start - src + dst
                    current[1] = next_end - src + dst
                    break
        min_loc_ranges.append(current)
    return min_loc_ranges


def get_minimum_location_by_range(seeds, maps):
    return min(map(tuple, get_locations_by_range(seeds, maps)))[0]


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Error: Missing input")
        exit(1)

    data_file = sys.argv[1]

    with open(data_file, "r") as f:
        data = [line for line in f.read().splitlines() if line != '']

    seeds, maps = parse_data(data)
    print(get_minimum_location(seeds, maps))

    seeds = [(seeds[i], seeds[i+1]) for i in range(0, len(seeds), 2)]
    print(get_minimum_location_by_range(seeds, maps))
