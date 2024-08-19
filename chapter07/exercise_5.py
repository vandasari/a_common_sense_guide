"""
Exercise 5
Time complexity: O(log n)
"""


def pick_resume(resumes):
    eliminate = 'top'
    
    while len(resumes) > 1:
        if eliminate == 'top':
            resumes = resumes[len(resumes)//2:]
            print(f'eliminate = {eliminate}; resumes = {resumes}')
            eliminate = 'bottom'
        elif eliminate == 'bottom':
            resumes = resumes[:len(resumes)//2]
            print(f'eliminate = {eliminate}; resumes = {resumes}')
            eliminate = 'top'
            
    return resumes[0]



if __name__ == '__main__':    
    arr = ['Jim Halpert', 'Pam Beesley', 'Michael Scott', 'Dwight Schrute', 
           'Angela Martin', 'Oscar Martinez', 'Stanley Hudson', 'Ryan Howard',
           'Jan Levinson', 'Phyllis Lapin-Vance', 'Toby Flanderson',
           'Meredith Palmer', 'Roy Anderson', 'David Wallace', 'Kelly Kapoor']
    
    print(f'Winner of Dundee Award: {pick_resume(arr)}')
    
    
    