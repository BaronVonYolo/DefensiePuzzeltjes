

blue = 'oh6pw1umstpepjkiwotcpn1wi1beshamgqezmakk2pbkcwne'
yellow = 'o19k1wetygptepikng6bpalpsvoxosapl2triieks1e6hwle'
black = 'olv9ke16dnweryil1egotp2sci1lx2wf1yaltsddss16prre'
green = 'lybewewe2risdvs0k216maoumeld1n9lipzlrc1ppscfqodm'
red = 'zpqw91wnllobwp1admpieceytcn1sv930mamp0mu1wmwl2ku'

def find_combos(list1, list2):
    result = []
    for offset in range(0, len(list2)):
        for i, letter in enumerate(list1):
            if letter == list2[(i + offset)%len(list2)] and list1[(i+10)%len(list1)] == list2[(i + offset + 10)%len(list2)]:
                result.append(([i, (i+10)%len(list1)], [(i + offset)%len(list2), (i + offset + 10)%len(list2)]))

    return result

def red_blue():
    red2 = red[::-1]
    print(red2)
    combs = find_combos(blue, red)
    print(combs)

    for pair in combs:
        print('{}{}'.format(blue[pair[0][0]], blue[pair[0][1]]))


def sequence():

    blue_yellow = find_combos(blue, yellow)

    for pair in blue_yellow:
        yellow_coords = pair[1]
        yellow_coords[0] = ((yellow_coords[0] - 2) + len(yellow))%len(yellow)
        yellow_coords[1] = ((yellow_coords[0] - 10) + len(yellow))%len(yellow)
        yellow_black = find_combos(yellow, black)

        yellow_black_pair = []
        for yb_pair in yellow_black:
            if yb_pair[0][0] == yellow_coords[1] and yb_pair[0][1] == yellow_coords[0]:
                yellow_black_pair = yb_pair
                break

        if len(yellow_black_pair) == 0:
            continue
                
        black_coords = yellow_black_pair[1]
        black_coords[0] = ((black_coords[0] - 2) + len(yellow))%len(yellow)
        black_coords[1] = ((black_coords[0] - 10) + len(yellow))%len(yellow)

        black_green = find_combos(black, green)
        black_green_pair = []
        for bg_pair in black_green:
            if bg_pair[0][0] == black_coords[1] and bg_pair[0][1] == black_coords[0]:
                black_green_pair = bg_pair
                break

        if len(black_green_pair) == 0:
            continue

        green_coords = black_green_pair[1]
        green_coords[0] = ((green_coords[0] - 2) + len(yellow))%len(yellow)
        green_coords[1] = ((green_coords[0] - 10) + len(yellow))%len(yellow)
        green_red = find_combos(green, red)
        green_red_pair = []
        for gr_pair in green_red:
            if gr_pair[0][0] == green_coords[1] and gr_pair[0][1] == green_coords[0]:
                green_red_pair = gr_pair
                break
        
        if len(green_red_pair) == 0:
            continue
        
        print('{}{}{}{}{}{}{}{}'.format(blue[pair[0][0]], yellow[yellow_black_pair[0][1]], black[black_green_pair[0][0]], green[green_red_pair[0][1]], blue[pair[0][1]], yellow[yellow_black_pair[0][0]], black[black_green_pair[0][1]], green[green_red_pair[0][0]]))

if __name__ == '__main__':
    red_blue()



