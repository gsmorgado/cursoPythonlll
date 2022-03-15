def main():
    set1={1,4,5,6,7, True, "Hola"}
    set2={1,3,6,7, False, "Pedro"}

    my_list = [ 11, 55, 2, 2, 55]
    my_set = set(my_list)
    print(my_set)  #output {1, 2, 3, 4, 5}
    
    print(f"set1 = {1,4,5,6,7, True, 'Hola'}")
    print(f"set2 = {1,3,6,7, False, 'Pedro'}")

    #union
    print(f"set1 + set2 = {set1 |set2}")

    #diferencia
    print(f"set1 - set2 = {set1 - set2}")

    #symetric difference
    print(f"set1 ^ set2 = {set1^set2}")

    #intersección
    print(f"set1 & set2 = {set1 & set2}")

if __name__== '__main__':
    main()