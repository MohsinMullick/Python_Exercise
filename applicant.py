"""If applicant has high income and good credit Eligible for loan"""
has_high_income=True
good_credit=True
if has_high_income and good_credit:
    print("Eligible for loan")



    """
    If applicant has high income or good credit Eligible for loan"""
    has_high_income=True
    good_credit=False
    if has_high_income or good_credit:
        print("Eligible for loan")

        """If applicant has good credit and dosen't have a criminal record 
        then Eligible for loan"""
        good_credit=True
        criminal_record=False
        if good_credit and not criminal_record:
            print("Eligible for loan")