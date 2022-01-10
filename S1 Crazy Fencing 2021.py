#Problem Description:

#You need to paint a wooden fence between your house and your neighbour’s house. You
#want to determine the area of the fence, in order to determine how much paint you will use.
# However, the fence is made out of N non-uniform pieces of wood, and your neighbour believes
# that they have an artistic flair. In particular, the pieces of wood may be of various widths.
# The bottom of each piece of wood will be horizontal, both sides will be vertical, but its top
# may be cut on an angle. Two such pieces of wood are shown below:
# Thankfully, the fence has been constructed so that adjacent pieces of wood have the same
# height on the sides where they touch, which makes the fence more visually appealing.


n = int(input())
set1 = list(map(int,input().split()))
set2 = list(map(int,input().split()))


total = 0
for i in range(n):
  total +=((set1[i]+set1[i+1])*set2[i])/2
print(total)
