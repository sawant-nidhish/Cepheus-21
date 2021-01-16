### DO NOT change or use any part of the code below. Doing so might get you disqualified.
 
import random
def info(a):
    cords={}
    mapp={"arduinos_trail":"Event_0001",
        "circuital_dilemma":"Event_0021",
        "fizzbuzz":"Event_0003",
        "hackoverflow":"Event_0004",
        "pandoras_box_ctf":"Event_0005",
        "unite_for_unity":"Event_0006",
        "frame_the_crane":"Event_0007",
        "cool_your_engine":"Event_0008",
        "fiducia":"Event_0009",
        "take_charge":"Event_0010",
        "chit_chat_with_chat_bot":"Event_0011",
        "pythonize_everything":"Event_0012",
        "ar_and_vr":"Event_0013",
        "iceev_hybrid":"Event_0014",
        "cyber_expert":"Event_0015",

        }
    generic="Event_"
    b=[]
    random.seed(134567)
    ##for those nerds who might want to hardcode the SEED will be changed before evaluation so make yor code generic
    for i in range(1,11):
        for j in range(1,11):
            b.append(generic + str(10000+(i-1)+(j-1)*10 +1)[1:]) 
    random.shuffle(b)
    for i in range(1,11):
        for j in range(1,11):
            cords[b[(i-1)+(j-1)*10]] = (i,j)
    try:
       return(cords[mapp[a]])
    except :
        return((-1,-1))
