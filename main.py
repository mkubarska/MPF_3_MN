def calfp(frates, fac_rate):
    # Tablice pomocnicze (zachowane dla odwzorowania struktury z C++)
    fun_units = [
        "External Inputs",
        "External Outputs",
        "External Inquiries",
        "Internal Logical Files",
        "External Interface Files",
    ]
    wt_rates = ["Low", "Average", "High"]

    # Wagi czynników (Weight Factors)
    wt_factors = [
        [3, 4, 6],  # External Inputs
        [4, 5, 7],  # External Outputs
        [3, 4, 6],  # External Inquiries
        [7, 10, 15],  # Internal Logical Files
        [5, 7, 10],  # External Interface Files
    ]

    ufp = 0

    # Obliczanie UFffP (Unadjusted Function Point)
    for i in range(5):
        for j in range(3):
            freq = frates[i][j]
            ufp += freq * wt_factors[i][j]

    # 14 czynników charakterystyki systemu (GSC)
    aspects = [
        "reliable backup and recovery required ?",
        "data communication required ?",
        "are there distributed processing functions ?",
        "is performance critical ?",
        "will the system run in an existing heavily utilized operational environment ?",
        "on line data entry required ?",
        "does the on line data entry require the input transaction to be built over multiple screens or operations ?",
        "are the master files updated on line ?",
        "is the inputs, outputs, files or inquiries complex ?",
        "is the internal processing complex ?",
        "is the code designed to be reusable ?",
        "are the conversion and installation included in the design ?",
        "is the system designed for multiple installations in different organizations ?",
        "is the application designed to facilitate change and ease of use by the user ?",
    ]

    # Sumowanie oceny czynników
    sum_f = 0
    for _ in range(14):
        rate = fac_rate
        sum_f += rate

    # Obliczanie CAF (Value Adjustment Factor)
    caf = 0.65 + 0.01 * sum_f

    # Obliczanie ostatecznych Punktów Funkcyjnych (FP)
    fp = ufp * caf

    # Wyświetlanie wyników
    print("Function Point Analysis :-")
    print(f"Unadjusted Function Points (UFP) : {ufp}")
    print(f"Complexity Adjustment Factor (CAF) : {caf:.2f}")
    print(f"Function Points (FP) : {fp:.2f}")


# Funkcja główna (odpowiednik main)
if __name__ == "__main__":
    # Macierz częstości występowania elementów
    frates = [[1, 4, 6], [0, 0, 6], [3, 1, 0], [4, 2, 2], [1, 0, 0]]

    fac_rate = 2

    calfp(frates, fac_rate)
