def conversion(cm):
    total_inches = cm / 2.54
    feet = int(total_inches // 12)
    inches = total_inches % 12
    return feet, inches

cm = float(input("Enter length in centimeters: "))

feet, inches = conversion(cm)

print(f"{cm} cm is approximately {feet} feet and {inches:.2f} inches.")