documentary = "'Behind The Curve'"
drama = "'A Walk To Remember'"
comedy = "'Just Friends'"
dramedy = "'Love Simon'"

print("Between 1 and 5 (5 being AMAZING), what would you rate documentaries?")
answer = int(input())

if answer >= 4:
    print("I recommend watching {}".format(documentary))
else:
    print("What would you rate dramas?")
    answer = int(input())

    if answer >= 4:
        print("What would you rate comedies?")
        answer = int(input())

        if answer >= 4:
            print("I recommend watching {}".format(dramedy))
        else:
            print("I recommend watching {}".format(drama))

    else:
        print("What would you rate comedies?")
        answer = int(input())

        if answer >= 4:
            print("I recommend watching {}".format(comedy))
        else:
            print("There's a Chapters down the road.")
