# import whatever you need here
import time

# Part 1 -- Write weight_on_cacheless() method
def weight_on_cacheless(r,c):
    # Top row has no wieght on
    if r == 0:
        result = 0.00
        return result
    # outer left
    elif c == 0:
        result = (200 + weight_on_cacheless(r - 1, c)) / 2
        return result
    # outer right
    elif c == r:
        result = (200 + weight_on_cacheless(r, c)) / 2
    # middle columns
    else:
        result = 200 + ((weight_on_cacheless(r - 1, c -1) + weight_on_cacheless(r - 1, c)) / 2)

# Part 3 -- Write weight_on_with_caching() method
def weight_on_with_caching(r,c):
    pass

def main():
    # Part 2 -- Use weight_on_cacheless() method
    # Cacheless
    print("Cacheless:")
    start = time.perf_counter()
    i = 0
    num = int(sys.argv[1])
    f = open("cacheless.txt","w")
    while i < num:
        j = 0
        row = ""
        while j <= i:
            row += '{:.2f}'.format((weight_on_cacheless(i,j))) + " "
            j+=1
        print(row)
        f.write(row + '\n')
        i+=1
    elapsed = time.perf_counter() - start
    print("\nElapsed time: " + str(elapsed) + " seconds.")
    f.write("\nElapsed time: " + str(elapsed) + " seconds." + '\n')
    f.close()
    
    # Part 3 -- Use weight_on_with_caching() method, with your HashMap ADT
    pass

if __name__=="__main__":
    main()

