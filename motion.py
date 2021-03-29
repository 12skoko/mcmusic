


def motion(start,end,tick):
    delta=[end[0]-start[0],end[1]-start[1],end[2]-start[2]]
    v=[]
    v.append((0.02*delta[0])/(1-0.98**tick))
    v.append((0.02*delta[1]+0.04*(tick-1))/(1-0.98**(tick-1))-1.96)
    v.append((0.02*delta[2])/(1-0.98**tick))
    return v



v=motion([-99.5,70,585.5],[-105.5,66,631.5],100)

print(v)