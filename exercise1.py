documentary = "'Behind The Curve'"
drama = "'A Walk To Remember'"
comedy = "'Just Friends'"
dramedy = "'Love Simon'"

print("Do you enjoy watching documentaries?")
answer = input()

if answer == "yes":
    print("I recommend watching {}".format(documentary))
    # break
else:
    print("Do you enjoy watching dramas?")
    answer = input()

    if answer == "yes":
        print("Do you enjoy watching comedies?")
        answer = input()

        if answer == "yes":
            print("I recommend watching {}".format(dramedy))
            # break
        else:
            print("I recommend watching {}".format(drama))
            # break

    else:
        print("Do you enjoy watching comedies?")
        answer = input()

        if answer == "yes":
            print("I recommend watching {}".format(comedy))
            # break
        else:
            print("There's a Chapters down the road.")
            # break

