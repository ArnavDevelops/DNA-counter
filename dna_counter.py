dna = input("Enter the sequence: ").upper()

if all(base in "ATGC" for base in dna) and len(dna) > 0:
    a_count = dna.count('A')
    t_count = dna.count('T')
    g_count = dna.count('G')
    c_count = dna.count('C')

    total = len(dna)

    GC_percent = ((g_count + c_count) / total) * 100
    AT_percent = ((a_count + t_count) / total) * 100

    print("\n===== DNA Counter Results =====")
    print(f"Length of sequence: {total}")
    print(f"A: {a_count}")
    print(f"T: {t_count}")
    print(f"G: {g_count}")
    print(f"C: {c_count}")
    print(f"GC Content: {GC_percent:.2f}%")
    print(f"AT Content: {AT_percent:.2f}%")
    print("===============================")
else:
    print("Invalid sequence!")