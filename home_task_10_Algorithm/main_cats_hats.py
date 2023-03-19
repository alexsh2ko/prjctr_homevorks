import cat_in_hat as cih
cih.cats_in_hats(100, 100)
print(f"In the hats, the cats are numbered "
     f"{', '.join(str(x) for x in cih.cats_in_hats(100, 100))}") 