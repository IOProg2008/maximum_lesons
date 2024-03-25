# def element_sum(NUM):
#     SUM=0
#     NUM_str=str(NUM)
#     for i in NUM_str:
#         SUM+=int(i)
#     print(SUM)
#
# element_sum(123)


def element_sum(NUM):
    SUM=0
    NUM_str=str(NUM)
    for i in NUM_str:
        SUM+=int(i)
    return SUM

print(element_sum(123))