documentary = "'Behind The Curve'"
drama = "'A Walk To Remember'"
comedy = "'Just Friends'"
dramedy = "'Love Simon'"

print("Between 1 and 5 (5 being AMAZING), what would you rate documentaries?")
doc_answer = int(input())

if doc_answer >= 4:
    print("I recommend watching {}".format(documentary))
elif doc_answer < 4:
    print("What would you rate dramas?")
    dram_answer = int(input())

    print("What would you rate comedies?")
    com_answer = int(input())
        
    if dram_answer >= 4 and com_answer < 4:
        print("I recommend watching {}".format(drama))

    elif dram_answer < 4 and com_answer >= 4:
        print("I recommend watching {}".format(comedy))
    
    elif dram_answer >= 4 and com_answer >= 4:
        print("I recommend watching {}".format(dramedy)) 

    else:
        print("..maybe read a book.")
