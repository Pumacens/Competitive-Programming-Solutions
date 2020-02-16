def get_grade(s1, s2, s3):
    mean = (s1 + s2 + s3) / 3
    return {90 <= mean <= 100: 'A',
            80 <= mean < 90: 'B',
            70 <= mean < 80: 'C',
            60 <= mean < 70: 'D',
            0  <= mean < 60: 'F'     
            }[True]