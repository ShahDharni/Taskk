df["Total Score"] = df["math score"] + df["reading score"] + df["writing score"]
df["Percentage"] = (df["Total Score"] / 300) * 100

def get_grade(percentage):
    if percentage >= 90:
        return "A"
    elif 80 <= percentage < 90:
        return "B"
    elif 70 <= percentage < 80:
        return "C"
    elif 60 <= percentage < 70:
        return "D"
    else:
        return "F"

df["Grade"] = df["Percentage"].apply(get_grade)
