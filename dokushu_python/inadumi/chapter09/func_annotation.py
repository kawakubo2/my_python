def get_triangle(base:float=1, height:float=1) -> float: 
    return base * height / 2

ann = get_triangle.__annotations__
print(ann)
print(ann['base'])

print(get_triangle('abc', 4.8))