def front_cw(rotated_front, front, rotated_left, down, rotated_up, left, rotated_right, up, rotated_down, right):
    # front
    rotated_front[0][0] = front[2][0]
    rotated_front[0][1] = front[1][0]
    rotated_front[0][2] = front[0][0]

    rotated_front[1][2] = front[0][1]

    rotated_front[2][2] = front[0][2]
    rotated_front[2][1] = front[1][2]
    rotated_front[2][0] = front[2][2]

    rotated_front[1][0] = front[2][1]

    #left
    rotated_left[0][2] = down[0][0]
    rotated_left[1][2] = down[0][1]
    rotated_left[2][2] = down[0][2]

    #up
    rotated_up[2][0] = left[2][2]
    rotated_up[2][1] = left[1][2]
    rotated_up[2][2] = left[0][2]

    #right
    rotated_right[0][0] = up[2][0]
    rotated_right[1][0] = up[2][1]
    rotated_right[2][0] = up[2][2]

    #down
    rotated_down[0][0] = right[2][0]
    rotated_down[0][1] = right[1][0]
    rotated_down[0][2] = right[0][0]

    return rotated_front, front, rotated_left, down, rotated_up, left, rotated_right, up, rotated_down, right

def back_cw(rotated_back, back, rotated_left, down, rotated_up, left, rotated_right, up, rotated_down, right):
    # back
    rotated_back[0][0] = back[2][0]
    rotated_back[0][1] = back[1][0]
    rotated_back[0][2] = back[0][0]

    rotated_back[1][2] = back[0][1]

    rotated_back[2][2] = back[0][2]
    rotated_back[2][1] = back[1][2]
    rotated_back[2][0] = back[2][2]

    rotated_back[1][0] = back[2][1]

    #right
    rotated_right[0][2] = down[2][2]
    rotated_right[1][2] = down[2][1]
    rotated_right[2][2] = down[2][0]

    #up
    rotated_up[0][0] = right[2][2]
    rotated_up[0][1] = right[1][2]
    rotated_up[0][2] = right[0][2]

    #left
    rotated_left[0][0] = up[0][2]
    rotated_left[1][0] = up[0][1]
    rotated_left[2][0] = up[0][0]

    #down
    rotated_down[2][2] = left[2][0]
    rotated_down[2][1] = left[1][0]
    rotated_down[2][0] = left[0][0]

    return rotated_back, back, rotated_left, down, rotated_up, left, rotated_right, up, rotated_down, right

def left_cw(rotated_back, back, rotated_left, down, rotated_up, left, rotated_front, up, rotated_down, front):
    #left
    rotated_left[0][0] = left[2][0]
    rotated_left[0][1] = left[1][0]
    rotated_left[0][2] = left[0][0]

    rotated_left[1][2] = left[0][1]

    rotated_left[2][2] = left[0][2]
    rotated_left[2][1] = left[1][2]
    rotated_left[2][0] = left[2][2]

    rotated_left[1][0] = left[2][1]

    return rotated_back, back, rotated_left, down, rotated_up, left, rotated_front, up, rotated_down, front

def right_cw(rotated_back, back, rotated_right, down, rotated_up, right, rotated_front, up, rotated_down, front):
    # right
    rotated_right[0][0] = right[2][0]
    rotated_right[0][1] = right[1][0]
    rotated_right[0][2] = right[0][0]

    rotated_right[1][2] = right[0][1]

    rotated_right[2][2] = right[0][2]
    rotated_right[2][1] = right[1][2]
    rotated_right[2][0] = right[2][2]

    rotated_right[1][0] = right[2][1]

    return rotated_back, back, rotated_right, down, rotated_up, right, rotated_front, up, rotated_down, front