# Oh man, 100 cats, and we gotta do something about putting them in hats or taking hats off.

# Setting up the cat ring in which none of my cats have hats.

cat_ring = []

for n in range(0, 100):
    cat_ring.append(f"Cat {n+1} has no hat. :(")

# The real work begins, in which each time I go around the ring of cats, I either place a hat if no hat
# is on a cat, or I take a hat off if the cat has a hat.

for the_pass in range(1, 101):
    for cat in range(len(cat_ring)):
        if (cat + 1) % the_pass == 0:
            if "has no hat" in cat_ring[cat]:
                cat_ring[cat] = f"Cat {cat+1} has a hat! :)"
            else:
                cat_ring[cat] = f"Cat {cat+1} has no hat. :("

for output in range(len(cat_ring)):
    print(cat_ring[output])