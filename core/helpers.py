MASTER_URL = {
    "B. Tech.": "scheme",
    "B. Tech. + M. Tech. (Dual Degree)": "dualdegree",
    "MT": "mtech",
    "MSC": "msc",
    "MBA": "mba",
}

branch = {
    "EE": "Electrical Engineering",
    "EC": "Electronics & Communication Engineering",
    "CE": "Civil Engineering",
    "MS": "Material Science Engineering",
    "CS": "Computer Science & Engineering",
    "CH": "Chemical Engineering",
    "ME": "Mechanical Engineering",
    "AR": "Architecture",
}

grade_map = {
    "A": 10,
    "AB": 9,
    "B": 8,
    "BC": 7,
    "C": 6,
    "CD": 5,
    "D": 4,
    "F": 0,
    "UMC": 0,
}

columns_sem = ["semester", "sub_name", "sub_code", "credits", "grade_letter", "grade"]
columns_sum = [
    "semester",
    "sgpi",
    "sem_credits",
    "cgpi",
    "total_credits",
]

STATES = [
    ("Rajasthan", "Rajasthan"),
    ("Madhya Pradesh", "Madhya Pradesh"),
    ("Maharashtra", "Maharashtra"),
    ("Uttar Pradesh", "Uttar Pradesh"),
    ("Gujarat", "Gujarat"),
    ("Karnataka", "Karnataka"),
    ("Andhra Pradesh", "Andhra Pradesh"),
    ("Odisha", "Odisha"),
    ("Chhattisgarh", "Chhattisgarh"),
    ("Tamil Nadu", "Tamil Nadu"),
    ("Telangana", "Telangana"),
    ("Bihar", "Bihar"),
    ("West Bengal", "West Bengal"),
    ("Arunachal Pradesh", "Arunachal Pradesh"),
    ("Jharkhand", "Jharkhand"),
    ("Assam", "Assam"),
    ("Ladakh", "Ladakh"),
    ("Himachal Pradesh", "Himachal Pradesh"),
    ("Uttarakhand", "Uttarakhand"),
    ("Punjab", "Punjab"),
    ("Haryana", "Haryana"),
    ("Jammu and Kashmir", "Jammu and Kashmir"),
    ("Kerala", "Kerala"),
    ("Meghalaya", "Meghalaya"),
    ("Manipur", "Manipur"),
    ("Mizoram", "Mizoram"),
    ("Nagaland", "Nagaland"),
    ("Tripura", "Tripura"),
    ("Andaman and Nicobar Islands", "Andaman and Nicobar Islands"),
    ("Sikkim", "Sikkim"),
    ("Goa", "Goa"),
    ("Delhi", "Delhi"),
    (
        "Dadra and Nagar Haveli and Daman and Diu",
        "Dadra and Nagar Haveli and Daman and Diu",
    ),
    ("Puducherry", "Puducherry"),
    ("Chandigarh", "Chandigarh"),
    ("Lakshadweep", "Lakshadweep"),
]
BRANCHES = [
    ("Electrical Engineering", "Electrical Engineering"),
    (
        "Electronics & Communication Engineering",
        "Electronics & Communication Engineering",
    ),
    ("Civil Engineering", "Civil Engineering"),
    ("Material Science Engineering", "Material Science Engineering"),
    ("Computer Science & Engineering", "Computer Science & Engineering"),
    ("Chemical Engineering", "Chemical Engineering"),
    ("Mechanical Engineering", "Mechanical Engineering"),
    ("Architecture", "Architecture"),
]
DEGREES = [
    ("B. Tech.", "B. Tech."),
    ("B. Tech. + M. Tech. (Dual Degree)", "B. Tech. + M. Tech. (Dual Degree)"),
    ("B. Arch", "B. Arch"),
]


def intt(x):
    try:
        return int(x)
    except:
        return -1


def capitalize_each_word(word: str) -> str:
    t = type(word).__name__
    if t != "str":
        raise TypeError(f"Expected str got {t}")
    word = word.strip()
    word = word.lower()
    word = word.split()
    result = ""
    for i in word:
        result += i.capitalize() + " "
    return result.strip()


def clean_email(email: str) -> str:
    t = type(email).__name__
    if t == "NoneType":
        return None
    if t != "str":
        raise TypeError(f"Expected str got {t}")
    try:
        email_name, domain_part = email.strip().rsplit("@", 1)
    except ValueError:
        pass
    else:
        email = email_name + "@" + domain_part.lower()
    return email
