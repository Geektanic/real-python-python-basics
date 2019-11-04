# Oh man, 100 cats, and we gotta do something about putting them in hats or taking hats off.

# Setting up the cat ring in which none of my cats have hats.

cat_ring = []

for n in range(0, 100):
    cat_ring.append(f"Cat {n+1} has no hat. :(")

# The real work begins, in which each time I go around the ring of cats, I either place a hat if no hat
# is on a cat, or I take a hat off if the cat has a hat.
# The instructions only call for printing out the list of cats with hats after the last pass.
# I have played around with a few different ways to output the ring of cats.

for the_pass in range(1, 101):
    for cat in range(len(cat_ring)):
        if (cat + 1) % the_pass == 0:
            if "has no hat" in cat_ring[cat]:
                cat_ring[cat] = f"Cat {cat+1} has a hat! :)"
            else:
                cat_ring[cat] = f"Cat {cat+1} has no hat. :("

print("")
print("The full ring of cats looks like this:")

for output in range(len(cat_ring)):
    print(cat_ring[output])

print("")
print("Only the cats below have hats:")

for new_out in range(len(cat_ring)):
    if "has a hat" in cat_ring[new_out]:
        print(cat_ring[new_out])

cats_with_hats = []

for summary_out in range(0, 100):
    if "has a hat" in cat_ring[summary_out]:
        cats_with_hats.append(f"{summary_out + 1}")

summary = ""

for new_summary_out in range(0, 100):
    if "has a hat" in cat_ring[new_summary_out]:
        summary = summary + f"{new_summary_out+ 1}, "

summary = summary[0:len(summary)-2]

print("")
print(f"Finally, to summarize, cats {summary} have hats! :)))")