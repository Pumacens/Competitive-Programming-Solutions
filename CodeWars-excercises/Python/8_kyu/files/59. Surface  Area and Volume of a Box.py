def get_size(w,h,d):
    return [2*(w*h + d*h + d*w), w * h * d]


# def get_size(w, h, d):
#     area = 2*(w*h + h*d + w*d)
#     volume = w*h*d
#     return [area, volume]