# Tower of Hanoi

# defining function
def toh(n, source, destination, aux):
    if n == 1:
        print('Move disk 1 from ', source, 'to ', destination)
        return
    else:
        toh(n-1, source, aux, destination)
        print("Move disk", n, "from ", source, "to ", destination)
        toh(n-1, aux, destination, source)


# Taking input from user
n = int(input('Enter no. of disks: '))
print('Here is the following Steps: ')
toh(n, 'A', 'B', 'C')  # here A-source, B-Destination, C-Auxiliary

